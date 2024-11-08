import requests
import unittest
import json


new_measurement = {
    'sepal_length': 5.7,
    'sepal_width': 3.1,
    'petal_length': 4.9,
    'petal_width': 2.2
}

SERVER_URL = 'http://127.0.0.1:8080'


class TestMlApiRequests(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(1, 1)

    def test_post_request(self):
        response = requests.post(SERVER_URL+'/predict_iris', json=new_measurement)
        # print(response.content)
        details = json.loads(response.content)
        self.assertEqual(details["prediction"], "virginica")


if __name__ == "__main__":
    unittest.main()
