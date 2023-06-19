from urllib.parse import parse_qs

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.db import close_old_connections

from channels.auth import AuthMiddlewareStack
from rest_framework_simplejwt.tokens import AccessToken

User = get_user_model()

from channels.db import database_sync_to_async

class TokenAuthMiddleware:
    def __init__(self, inner):
        self.inner = inner

    async def __call__(self, scope, receive, send):
        close_old_connections()
        query_string = parse_qs(scope['query_string'].decode())
        token = query_string.get('token')
        if not token:
            scope['user'] = AnonymousUser()
            return await self.inner(scope, receive, send)
        try:
            access_token = AccessToken(token[0])
            user = await database_sync_to_async(User.objects.get)(id=access_token['id'])
        except Exception as exception:
            scope['user'] = AnonymousUser()
            return await self.inner(scope, receive, send)
        if not user.is_active:
            scope['user'] = AnonymousUser()
            return await self.inner(scope, receive, send)
        scope['user'] = user
        return await self.inner(scope, receive, send)


def TokenAuthMiddlewareStack(inner):
    return TokenAuthMiddleware(AuthMiddlewareStack(inner))