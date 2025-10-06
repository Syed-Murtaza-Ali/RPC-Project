# client.py
import requests

# The server URL
SERVER_URL = "http://127.0.0.1:8080"

# Function to call the server
def call_rpc(endpoint, data):
    try:
        response = requests.post(f"{SERVER_URL}/{endpoint}", json=data, timeout=2)
        response.raise_for_status()
        print(f"{endpoint}({data['x']},{data['y']}) = {response.json()['result']}")
    except requests.exceptions.Timeout:
        print("Request timed out")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    call_rpc("add", {"x": 2, "y": 3})
    call_rpc("multiply", {"x": 4, "y": 5})