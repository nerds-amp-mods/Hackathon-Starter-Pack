import nox

SOURCE_FILES = ("noxfile.py", "app/", "tests/")


@nox.session(reuse_venv=True)
def format(session) -> None:
    session.install("black", "isort")
    session.run("black", "--target-version=py38", *SOURCE_FILES)
    session.run("isort", *SOURCE_FILES)
    lint(session)


@nox.session(reuse_venv=True)
def lint(session) -> None:
    session.install("black", "flake8", "mypy", "isort")
    session.run("black", "--check", "--target-version=py38", *SOURCE_FILES)
    session.run("isort", "--check", *SOURCE_FILES)
    session.run("flake8", "--ignore=E501,W503,E402,E712,E203", *SOURCE_FILES)
    session.run("mypy", "--strict", "app/")


@nox.session(python=["3.8"])
def test(session) -> None:
    session.install("-r", "requirements.txt")
    # TODO Add flask app start
    session.run(
        "pytest", "--cov-report=xml", "--cov=app/", *(session.posargs or ("tests/",))
    )
