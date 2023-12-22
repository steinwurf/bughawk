import pytest_testdirectory
import bughawk


def test_run(testdirectory):
    try:
        r = testdirectory.run("bughawk --help")
        assert r.stdout.match(f"bughawk")
    except pytest_testdirectory.runresulterror.RunResultError as e:
        print(e)
        assert False
