import requests

API_URL = "https://api-inference.huggingface.co/models/prithivMLmods/Deep-Fake-Detector-Model"
API_TOKEN = "hf_PDItqGFQnqoyerpspcXPVlzWMWRvxdyzv"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

output = query("userImage//ai-faces-01.jpg")
print(output)