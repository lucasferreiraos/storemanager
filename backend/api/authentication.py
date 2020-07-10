from rest_framework import authentication


class KeyTokenAuthentication(authentication.TokenAuthentication):
    keyword = 'key'
