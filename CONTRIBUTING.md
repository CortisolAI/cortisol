## General Guidelines
- Every new functionality should be accompanied with solid unit tests. We haven't set any threshold regarding code coverage % as we want to be pragmatic.
- Every bug that is fixed should come with related unit tests.
- Regarding coding style, we follow PEP8 by leveraging [black](https://pypi.org/project/black/)

## Branching Model
- Standard Fork & Pull Request Workflow is used in this project
- Every new functionality should be created in a branch (from develop branch) with name format `feature/new-functionality-name`
- Every bug should be fixed in a branch (from develop branch) with name format `fix/bug-name`
- All branches will be merged to develop branch

## Setup Environment
- [Poetry](https://python-poetry.org/) is used as a dependency management tool
- Run `poetry install --with test` to install dependencies 
- Ready to rock!

## Testing Locally
- `poetry run pytest --cov .`: Runs tests with code coverage

## Linting Locally
- `poetry run black . --check` to check if there's a formatting issue
- `poetry run black .` to fix the formatting issue