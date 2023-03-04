import pytest


def do_something():
    print('do something')
    if hasattr(pytest, 'in_pytest'):
        print('blah')


if __name__ == '__main__':
    do_something()
