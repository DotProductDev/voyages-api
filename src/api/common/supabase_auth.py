import jwt
import requests
from django.conf import settings
from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions
from functools import lru_cache
from datetime import datetime, timedelta

# Cache JWKS for 1 hour to avoid repeated requests
_jwks_cache = None
_jwks_cache_time = None
JWKS_CACHE_DURATION = timedelta(hours=1)


@lru_cache(maxsize=1)
def get_jwks():
    """
    Fetch JWKS (JSON Web Key Set) from Supabase.
    Cached to avoid repeated network requests.
    """
    global _jwks_cache, _jwks_cache_time

    now = datetime.now()
    if _jwks_cache and _jwks_cache_time and (now - _jwks_cache_time) < JWKS_CACHE_DURATION:
        return _jwks_cache

    try:
        response = requests.get(settings.SUPABASE_JWKS_URL, timeout=10)
        response.raise_for_status()
        _jwks_cache = response.json()
        _jwks_cache_time = now
        return _jwks_cache
    except Exception as e:
        raise exceptions.AuthenticationFailed(f'Failed to fetch JWKS: {str(e)}')


def get_signing_key(token):
    """
    Get the appropriate signing key from JWKS based on the token's kid (key ID).
    """
    jwks = get_jwks()

    # Decode token header without verification to get the kid
    unverified_header = jwt.get_unverified_header(token)
    kid = unverified_header.get('kid')

    if not kid:
        raise exceptions.AuthenticationFailed('Token missing kid in header')

    # Find the key with matching kid
    for key in jwks.get('keys', []):
        if key.get('kid') == kid:
            # Convert JWK to PEM format for PyJWT
            from jwt.algorithms import RSAAlgorithm
            return RSAAlgorithm.from_jwk(key)

    raise exceptions.AuthenticationFailed('Unable to find matching key in JWKS')


def verify_supabase_jwt(token):
    """
    Verify Supabase JWT using JWKS and return payload.
    """
    try:
        # Get the signing key
        signing_key = get_signing_key(token)

        # Verify and decode the token
        payload = jwt.decode(
            token,
            signing_key,
            algorithms=['RS256'],
            audience='authenticated',
            options={
                'verify_signature': True,
                'verify_exp': True,
                'verify_aud': True
            }
        )

        # Verify issuer
        expected_issuer = f'{settings.SUPABASE_URL}/auth/v1'
        if payload.get('iss') != expected_issuer:
            raise jwt.InvalidIssuerError('Invalid issuer')

        return payload
    except jwt.ExpiredSignatureError:
        raise exceptions.AuthenticationFailed('Token has expired')
    except jwt.InvalidTokenError as e:
        raise exceptions.AuthenticationFailed(f'Invalid token: {str(e)}')


class SupabaseAuthentication(authentication.BaseAuthentication):
    """
    Verifies Supabase JWTs using JWKS and maps to Django User model.
    Creates users on first authentication.
    """

    def authenticate(self, request):
        auth_header = request.META.get('HTTP_AUTHORIZATION', '')

        if not auth_header.startswith('Bearer '):
            return None

        token = auth_header.split(' ')[1]

        # Verify the token
        payload = verify_supabase_jwt(token)

        # Extract user info
        user_id = payload.get('sub')  # Supabase user ID
        email = payload.get('email')
        user_metadata = payload.get('user_metadata', {})

        if not user_id or not email:
            raise exceptions.AuthenticationFailed('Invalid token payload')

        # Get or create Django user
        user = self.get_or_create_user(user_id, email, user_metadata)

        return (user, payload)

    def get_or_create_user(self, supabase_id, email, metadata):
        """
        Map Supabase user to Django user.
        Uses Supabase ID as username for uniqueness.
        """
        # Try finding by username (supabase_id)
        try:
            user = User.objects.get(username=supabase_id)
            # Update email if changed
            if user.email != email:
                user.email = email
                user.save()
            return user
        except User.DoesNotExist:
            pass

        # Try finding by email (for backward compatibility with existing users)
        try:
            user = User.objects.get(email=email)
            # Link to Supabase ID
            user.username = supabase_id
            user.save()
            return user
        except User.DoesNotExist:
            pass

        # Create new user
        user = User.objects.create_user(
            username=supabase_id,
            email=email,
            first_name=metadata.get('firstName', ''),
            last_name=metadata.get('lastName', ''),
        )
        return user

    def authenticate_header(self, request):
        return 'Bearer realm="api"'
