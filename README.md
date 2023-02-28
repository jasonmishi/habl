# Habl
Help manage rewards using gacha game-esque techniques.

## Contributors guide
- DO NOT COMMIT TO MAIN - always make a branch and do a pull request.
- When making a pull request get at least 1 review.
- If you are unsure don't merge it yourself. If there are conflicts please consult the rest of the team before merging.
- Both testing and linting workflows are set up please make sure they pass in your Pull Request.
- Please try to add unit tests where possible, especially for bigger complex sections of code, tests can be found in the `src/tests` directory we use [pytest](https://docs.pytest.org/en/stable/) you can also refer the [django docs](https://docs.djangoproject.com/en/stable/topics/testing/overview/).

### Linting & Testing
We use `pre-commit` for linting, can be run as `poetry run pre-commit run --all-files`.
Testing is done through `tox` run `poetry run tox`.

## Getting Started
This repository uses [poetry](https://python-poetry.org) for package management. Install poetry and then:

```sh
poetry install
poetry shell
cd src
python manage.py runserver
```

and you would have started the django development server.

