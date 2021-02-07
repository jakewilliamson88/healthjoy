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

    import pprint
    pprint.pprint(response.json())

    # Get the redirect URL.
    if response.status_code == 202:
        print("200 OK")
        redirect_url = response.json().get('html_url')
        print("REDIRECT URL: ", redirect_url)
        if redirect_url:
            print("GOT HERE")
            return redirect(redirect_url)

    return get_fork()
