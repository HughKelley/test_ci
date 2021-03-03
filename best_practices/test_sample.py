# https://sourcery.ai/blog/python-best-practices/
# https://sourcery.ai/blog/github-actions/

# content of test_sample.py
def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 5
