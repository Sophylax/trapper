from tests.utils import assert_shell

if __name__ == "__main__":
    assert_shell(
        "pytest --cov trapper --cov-report term-missing --cov-report xml -vvv tests"
    )
