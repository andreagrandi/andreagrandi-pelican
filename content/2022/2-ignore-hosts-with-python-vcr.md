Title: Ignoring hosts with python vcr when writing tests with pytest and generating cassettes
Date: 2022-12-02 11:30
Author: Andrea Grandi
Category: Development
Tags: python, development, python-vcr, programming, tests, pytest, vcr
Slug: ignore-hosts-with-python-vcr
Status: published
Summary: How to ignore hosts with python vcr when writing tests with pytest and generating cassettes 

If you are already using [pytest](https://pytest.org) to write your tests and are also using [vcr](https://vcrpy.readthedocs.io)
to record and replay http responses, you already know that any http request is being recorded, so the next time the same
request is made, the test won't hit the real endpoint but it will use the recorded response.

Sometimes you need to exclude `localhost` (or other hosts) from being recorded and you can do thanks to this vcr parameter:

    :::python
    @pytest.mark.vcr(ignore_hosts=["localhost"])
    def test_is_true():
        # Intentionally dumb test to make things simple
        assert True

This works, but what if you have many tests and you want to ignore `localhost` globally?

You can do it by adding this to your main `conftest.py` and all your vcr tests will ignore it by default:

    :::python
    @pytest.fixture(scope="module")
    def vcr_config():
        return {
            "ignore_hosts": ["localhost"],
        }

That's it! I hope you find this suggestion useful.
