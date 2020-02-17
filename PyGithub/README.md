# cogitate_tool
Tool to analyze contributions when working in a team.

## About PyGithub

It's a Python library which utilizes the Github API. It enables you to
interact with repositories, user profiles, organizations and many more.

## Install PyGithub

Run the command `pip install PyGithub`. For more information please see the
[link](https://github.com/PyGithub/PyGithub)

## Run PyGithub

* Generate personal access token. Please see the [link](https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line) and follow the instructions.

* Replace the access token in `demo.py` with the personal access token that you generated. Remember not to push out an update containing your personal access token!

* Install the development dependencies: `pipenv install --dev`

* Run `pipenv run python demo.py`

## PyGithub Features

* Get user information such as names and current user.

* Get repository information such as open issues, labels, read notifications, etc.

* List all branches and their protection status.

* Get, create, and close issues.

* Get and create Milestones.

To see more sample features please see the [link](https://pygithub.readthedocs.io/en/latest/examples.html)

## Documentation

More information can be found on the [PyGitHub documentation site.](https://pygithub.readthedocs.io/en/latest/introduction.html)