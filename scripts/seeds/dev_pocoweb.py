# coding: utf-8
from development import *  # NOQA

POCOWEB_URL = 'https://pocoweb-qa.petro.intelie.net/'
SSE_PUBSUB_URL='redis://localhost:6376/3'

OIDC_AUTH = {
    'DEFAULT_PROVIDER': {
        'issuer': POCOWEB_URL,
        'authorization_endpoint': '%so/authorize/' % POCOWEB_URL,
        'token_endpoint': '%so/token/' % POCOWEB_URL,
        'userinfo_endpoint': '%so/userinfo/' % POCOWEB_URL,
        'client_id': 'SEEDS-local',
        'client_secret': 'SEEDS-local'
    },
    'VERIFY_SSL': False
}

FEATURES = {
    'IMPORT_POCOWEB': True,
    'PUBLISH_POCOWEB': True,
}

LOGIN_URL = '/oidc/login/'

AUTHENTICATION_BACKENDS = (
    'oidc_auth.auth.OpenIDConnectBackend',
    'django.contrib.auth.backends.ModelBackend',
)


import os
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
os.environ['DEBUG'] = '1'
