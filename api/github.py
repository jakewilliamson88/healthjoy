"""
github.py
This is the interface to the Github API.
"""

import requests


class Github:
    """
    The ``Github`` class is the interface to the Github API.
    """

    # The URI For the github API.
    uri = 'https://api.github.com'

    def __init__(self, username, password):
        """
        Initializes the ``Github`` instance.
        :param username
        :param password
        """

        self.session = requests.Session()
        self.session.auth = (username, password)

    def __call(self, endpoint, method, data=None, params=None, headers=None):
        """
        Make an API call.
        :param endpoint:
        :param method:
        :param data:
        :param params:
        :return:
        """

        method = {
            'GET': self.session.get,
            'POST': self.session.post
        }[method]

        return method(endpoint, data=data, params=params, headers=headers)

    def fork(self):
        """
        Fork this project's repo.
        :return:
        """

        # TODO
