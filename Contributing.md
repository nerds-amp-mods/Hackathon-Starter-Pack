# Contributing Guidelines

This is a open source project and we love to receive contributions from community --- you!. This project is currently in alpha state.

## Contributing code and documentation changes

### **DISCLAIMER**

- Please ask for clarification in issues/ pull requests to get more understanding on tasks that you are doing.
- Don't force push your branch, when changes are required / until you are asked to for latest changes.

You will need to fork the [Main Repository](https://github.com/nerds-amp-mods/Hackathon-Login-Starter-Pack.git) to your github account and clone the repository to your local machine.

Further Information for specific projects given below

## Backend

- Currently backend supports python>=3.8.5
- Create a virtual environment using `python -m virtualenv venv` and activate the virtual environment.
- Open the your IDE from `backend` as your root folder.
- Make sure you are having the latest code on your development branch, else do `git rebase origin/master`.
- Create a new branch for your development purpose using `git checkout -b your-branch-name`
- Install the requirements using `pip install -r requirements.txt`
- Make the code changes required. :)
- lint and type check the code using `nox -r -s format`
- To make sure you don't break anything test the code using `nox -r -s test-3.8`
- Submit your pull request, sit back and wait for the maintainers to respond.
