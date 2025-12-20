import requests
import json
import time
import random


def run_inference():
    url = "http://localhost:5001/invocations"
    headers = {"Content-Type": "application/json"}

    data = {
        "dataframe_split": {
            "columns": [
                "absolute_magnitude",
                "estimated_diameter_min",
                "estimated_diameter_max",
                "relative_velocity",
                "miss_distance"
            ],
            "data": [[22.0, 0.01, 0.02, 40000, 5000000]]
        }
    }
    while True:
        try:
            response = requests.post(url, data=json.dumps(data), headers=headers)
            print(f"Status: {response.status_code}, Prediction: {response.text}")
        except Exception as e:
            print(f"Error: {e}")

        time.sleep(random.uniform(1, 3))


if __name__ == "__main__":
    run_inference()