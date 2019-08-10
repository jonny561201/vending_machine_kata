import json

from mock import patch

from svc.routes.routes import health_status, purchase


def test_health_status__should_return_success():
    actual = health_status()

    assert actual == 'Success'
