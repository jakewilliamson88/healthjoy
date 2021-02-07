"""
fork.py
This is the Fork interface.
"""

from api.github import Github
from flask import Blueprint, request, render_template, redirect

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
    username = request.form.get('username')
    password = request.form.get('password')

    # Get an interface to the Github API.
    api = Github(username, password)

    # Fork the repo.
    response = api.fork()

    # Get the redirect URL.
    if response.status_code == 202:
        redirect_url = response.json().get('html_url')
        if redirect_url:
            return redirect(redirect_url)

    return get_fork()
