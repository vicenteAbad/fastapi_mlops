import unittest

import requests

INFERENCE_ENDPOINT = "http://localhost:3000/inference"


class TestStationService(unittest.TestCase):
    def test_successful_inference_response(self):
        example_data = [1, 2, 3, 4]
        input_data = {"input_data": example_data}

        response = requests.post(INFERENCE_ENDPOINT, json=input_data)
        status_code = response.status_code
        body = response.json()
        assert status_code == 200
        assert "id" in body
        assert "created_at" in body
        assert "prediction" in body
        assert len(body["prediction"]) == len(example_data)

    def test_fail_three_elements_inference_response(self):
        example_data = [1, 2, 3]
        input_data = {"input_data": example_data}
        response = requests.post(INFERENCE_ENDPOINT, json=input_data)
        status_code = response.status_code
        response.json()
        assert status_code == 422

    def test_fail_five_elements_inference_response(self):
        example_data = [1, 2, 3, 4, 5]
        input_data = {"input_data": example_data}
        response = requests.post(INFERENCE_ENDPOINT, json=input_data)
        status_code = response.status_code
        response.json()
        assert status_code == 422


if __name__ == "__main__":
    unittest.main()
