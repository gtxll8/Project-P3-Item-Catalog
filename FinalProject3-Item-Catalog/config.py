from authomatic.providers import oauth2, oauth1
import authomatic


CONFIG = {

    'tw': { # Your internal provider name

        # Provider class
        'class_': oauth1.Twitter,

        # Twitter is an AuthorizationProvider so we need to set several other properties too:
        'consumer_key': '5BPsGA0dUIPdFjWO3rs8r2BAP',
        'consumer_secret': 'ja8ztbL11o9GaR6ljElviM3Fz2i67PXosaEbZjPSTXfldg4DAc',
    },

    'github': { # Your internal provider name

        # Provider class
        'class_': oauth2.GitHub,

        # GitHub is an AuthorizationProvider yoo, so we need to set several other properties again:
        'consumer_key': '36ee18c6a4ab61e50cc4',
        'consumer_secret': '90b523efa0f80d4faef6f3ebab6d0efa9a0697a4',
        'access_headers': {'User-Agent': 'Awesome-Octocat-App'},
        'scope': ['id', 'email', 'name'],
    },

    'fb': {

        'class_': oauth2.Facebook,

        # Facebook is an AuthorizationProvider too.
        'consumer_key': '########################',
        'consumer_secret': '########################',

        # But it is also an OAuth 2.0 provider and it needs scope.
        'scope': ['user_about_me', 'email', 'publish_stream'],
    },

    'google': {
        'class_': oauth2.Google,
        'consumer_key': '720789354184-aokdhm5b8m2bjk6vtsb1aal83p1u0pgv.apps.googleusercontent.com',
        'consumer_secret': 'dW3onhfvmsEIKXWq668OJdK1',
        'id': authomatic.provider_id(),
        'scope': oauth2.Google.user_info_scope + [
            'email',
            'https://www.googleapis.com/auth/calendar',
            'https://mail.google.com/mail/feed/atom',
            'https://www.googleapis.com/auth/drive',
            'https://gdata.youtube.com'],
        '_apis': {
            'List your calendars': ('GET', 'https://www.googleapis.com/calendar/v3/users/me/calendarList'),
            'List your YouTube playlists': ('GET', 'https://gdata.youtube.com/feeds/api/users/default/playlists?alt=json'),
            },
    },

}
