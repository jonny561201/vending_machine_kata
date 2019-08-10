from svc.manager import create_app


class TestRouteIntegration:
    test_client = None

    def setup_method(self):
        flask_app = create_app('__main__')
        self.test_client = flask_app.test_client()

    def test_health_check__should_return_success(self):
        response = self.test_client.get('healthCheck')

        assert response.status_code == 200
        assert response.data == 'Success'
