# How to contribute to Soccer-Api-Wrapper

## Installing the development version

You need to make sure that you have installed python3

Then clone this github repository with:

```sh
git clone https://github.com/Debi-Ejeta/soccer-api-wrapper.git
```

and then go into it
```sh
cd soccer_api_wrapper
```

Then install the dependencies:
```sh
pip install requests
```

## Running the test suite

Go into the soccer_api_wrapper directory and run the tests with pytest before opening up a PR. 

```sh
python -m pytest -v soccer_api_wrapper/tests --cov=soccer_api_wrapper --cov-branch --cov-fail-under=75 --cov-report term-missing
```

If you are proposing the addition of new features in your PR, please add tests for that feature.

