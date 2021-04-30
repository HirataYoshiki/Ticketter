import os, json
import requests

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

with open(os.getenv('IDPLATFORM_API_KEY_FILE_PATH'),'r') as f:
  PAYLOAD = json.load(f)
  API_KEY = PAYLOAD['API_KEY']

signin_url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={API_KEY}"
LoginData = {
  "data": {}
}

def login(email: str, password: str) -> dict:
  payload = {
    "email": email,
    "password": password,
    "returnSecureToken": True
  }
  response = requests.post(signin_url, payload)
  return response

def get_id_token(response):
  return response.get('idToken')

def test_fail_login():
  input_ = {
    "email": "xxx@sss.ss",
    "password": "password"
  }
  output = {
    "status_code": 400
  }
  response = login(input_["email"], input_["password"])
  assert response.status_code==output["status_code"]

def test_success_login():
  input_ = {
    "email": "kirryx2@yahoo.co.jp",
    "password": "a19930525"
  }
  output = {
    "status_code": 200
  }
  response = login(input_["email"], input_["password"])
  LoginData["data"] = json.loads(response.content)
  assert response.status_code == output['status_code']

def test_fail_get_user_by_uid():
  input_ = {
    "uid": "ddggheh"
  }
  headers = {
    "Authorization": LoginData["data"]['idToken']
  }
  output = {
    "status_code": 400
  }
  response = client.get(f'/users/{input_["uid"]}', headers=headers)
  assert response.status_code == 400

def test_fail_get_user_by_uid_id_token_is_invalid():
  input_ = {
    "uid": LoginData["data"]['localId']
  }
  headers = {
    "Authorization": "IDTOKEN"
  }
  output = {
    "status_code": 400
  }
  response = client.get(f'/users/{input_["uid"]}', headers=headers)
  assert response.status_code == output['status_code']

def test_success_get_user_by_uid():
  input_ = {
    "uid": LoginData["data"]['localId']
  }
  headers = {
    "Authorization": LoginData["data"]['idToken']
  }
  output = {
    "status_code": 200
  }
  response = client.get(f'/users/{input_["uid"]}', headers=headers)
  assert response.status_code == output['status_code']