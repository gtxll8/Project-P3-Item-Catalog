# config.py

from authomatic.providers import oauth2, oauth1

CONFIG = {

    'tw': { # Your internal provider name

        # Provider class
        'class_': oauth1.Twitter,

        # Twitter is an AuthorizationProvider so we need to set several other properties too:
        'consumer_key': 'wM0LNsBC6W0VOwIEaZuMxsP5d',
        'consumer_secret': 'aXtrzZHC3kbQKHsm0EX9DnvIOJeg8ZugU8o1IP2txDjnM6YG2K',
    },

    'fb': {

        'class_': oauth2.Facebook,

        # Facebook is an AuthorizationProvider too.
        'consumer_key': '########################',
        'consumer_secret': '########################',

        # But it is also an OAuth 2.0 provider and it needs scope.
        'scope': ['user_about_me', 'email', 'publish_stream'],
    },


}