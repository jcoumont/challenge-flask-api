import unittest
import requests


class TestApi(unittest.TestCase):
    url_status = "http://localhost:5000/status"
    url_login = "http://localhost:5000/login"

    def test_status(self):
        response = requests.request("GET", self.url_status)

        # Validate status code & content
        assert response.status_code == 200
        assert response.text == "Alive!"

    def test_login_no_body(self):
        response = requests.request("POST", self.url_login)

        # Validate status code.
        assert response.status_code == 400

    def test_login_no_username(self):
        payload = '{\n"password": "1234567"\n}'
        headers = {"Content-Type": "application/json"}

        response = requests.request(
            "POST", self.url_login, headers=headers, data=payload
        )
        # Validate status code.
        assert response.status_code == 400

    def test_login_no_password(self):
        payload = '{\n"username": "dustybot"\n}'
        headers = {"Content-Type": "application/json"}

        response = requests.request(
            "POST", self.url_login, headers=headers, data=payload
        )
        # Validate status code & content
        assert response.status_code == 400

    def test_login(self):
        payload = '{\n"username": "dustybot",\n"password": "1234567"\n}'
        headers = {"Content-Type": "application/json"}

        response = requests.request(
            "POST", self.url_login, headers=headers, data=payload
        )

        # Validate status code.
        assert response.status_code == 200
        assert (
            response.text
            == "Login success for user dustybot with password of length: 7!!"
        )

    def test_predict(self):
        url = "http://localhost:5000/predict/123/december/4"
        response = requests.request("GET", url)

        # Validate status code & content.
        assert response.status_code == 200
        assert 2000 <= int(response.text) <= 5000
