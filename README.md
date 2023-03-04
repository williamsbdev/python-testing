# python-testing

I wanted to know how I might be able to tell if certain code was being run from
a test (pytest) vs production invocation. This provides a very basic example of
how to do that.

- Create a `virtualenv` with your Python setup (however you'd like).
- Install `pytest` from requirements.
- Run the script `python script.py`
    - The output should be:
        ```
        do something
        ```
- Run the tests with `pytest`
    - The test should fail and the output should be:
        ```
        do something
        blah
        ```

We set some arbitrary property on the `pytest` module within the
`tests/__init__.py` that we can leverage to ensure that code is run/not run
during tests.
