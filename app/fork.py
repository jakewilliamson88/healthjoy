"""
fork.py
This is the Fork interface.
"""

from api.github import Github
from flask import Blueprint, request, render_template

fork = Blueprint('fork', __name__)


@fork.route('/', methods=['GET'])
def get_fork():
    """
    Handle HTTP GET requests to /fork
    :return:
    """

    return render_template('fork.html')

@fork.route('/', methods=['POST'])
def post_fork():
    """
    Handle HTTP POST requests to /fork.
    Fork this project's github project.
    :return:
    """

    # Get the username and password.
    username = request.form.get('email')
    password = request.form.get('password')

    # Get an interface to the Github API.
    api = Github(username, password)

    print('\r\n\r\n')
    print('GOT HERE')
    print('\r\n\r\n')

    return get_fork()
