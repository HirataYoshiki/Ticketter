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
  
def test_create_user():
  headers = {
    "Authorization":f"Bearer {LoginData['data']['idToken']}"
  }
  output = {
    "status_code": 200
  }
  response = client.post('/users', headers = headers)
  assert response.status_code == output["status_code"]

def test_get_all_users():
  headers = {
    "Authorization":f"Bearer {LoginData['data']['idToken']}"
  }
  output = {
    "status_code": 200
  }
  response = client.get('/users', headers = headers)
  assert response.status_code == 200

def test_fail_get_user_by_uid_user_not_found():
  input_ = {
    "uid": "ddggheh"
  }
  headers = {
    "Authorization":f"Bearer {LoginData['data']['idToken']}"
  }
  output = {
    "status_code": 404
  }
  response = client.get(f'/users/{input_["uid"]}', headers=headers)
  assert response.status_code == output['status_code']

def test_fail_get_user_by_uid_id_token_is_invalid():
  input_ = {
    "uid": LoginData["data"]['localId']
  }
  headers = {
    "Authorization": "Bearer IDTOKEN"
  }
  output = {
    "status_code": 401
  }
  response = client.get(f'/users/{input_["uid"]}', headers=headers)
  assert response.status_code == output['status_code']

def test_success_get_user_by_uid():
  input_ = {
    "uid": LoginData["data"]['localId']
  }
  headers = {
    "Authorization":f"Bearer {LoginData['data']['idToken']}"
  }
  output = {
    "status_code": 200
  }
  response = client.get(f'/users/{input_["uid"]}', headers=headers)
  assert response.status_code == output['status_code']

def test_fail_create_ticket_id_token_is_invalid():
  input_ = {
    "json": {
      "name": "ticket",
      "text": "this is test ticket"
    } 
  }
  headers = {
    "Authorization":f"Bearer sgsdg"
  }
  output = {
    "status_code": 401
  }
  response = client.post('/tickets', json = input_['json'], headers = headers)
  assert response.status_code==output['status_code']

def test_fail_create_ticket_data_is_invalid():
  input_ = {
    "json": {
      "namer": "ticket",
      "text": "this is test ticket"
    } 
  }
  headers = {
    "Authorization":f"Bearer {LoginData['data']['idToken']}"
  }
  output = {
    "status_code": 422
  }
  response = client.post('/tickets', json = input_['json'], headers = headers)
  assert response.status_code == output['status_code']

def test_success_create_ticket():
  input_ = {
    "json": {
      "name": "ticket",
      "text": "this is test ticket"
    } 
  }
  headers = {
    "Authorization":f"Bearer {LoginData['data']['idToken']}"
  }
  output = {
    "status_code": 200
  }
  response = client.post('/tickets', json = input_['json'], headers = headers)
  assert response.status_code == output['status_code']

def test_success_get_tickets():
  headers = {
    "Authorization":f"Bearer {LoginData['data']['idToken']}"
  }
  output = {
    "status_code": 200
  }
  response = client.get('/tickets', headers = headers)
  assert response.status_code == output['status_code']

def test_fail_give_a_ticket_uid_is_invalid():
  input_ = {
    "uid": "fess",
    "json": {
      "ticketid": 1
    }
  }
  headers = {
    "Authorization":f"Bearer {LoginData['data']['idToken']}"
  }
  output = {
    "status_code": 404
  }
  response = client.post(f'/interactions/{input_["uid"]}',json=input_['json'], headers = headers)
  assert response.status_code == output['status_code']

def test_fail_give_a_ticket_ticketid_is_invalid():
  input_ = {
    "uid": "WRk791v2hQUFHZP9GBMcRXTqdxb2",
    "json": {
      "ticketid": 100
    }
  }
  headers = {
    "Authorization":f"Bearer {LoginData['data']['idToken']}"
  }
  output = {
    "status_code": 400
  }
  response = client.post(f'/interactions/{input_["uid"]}',json=input_['json'], headers = headers)
  assert response.status_code == output['status_code']

def test_success_give_tickets():
  input_ = {
    "json": {
      "ticketid": 1,
      "to_": ["WRk791v2hQUFHZP9GBMcRXTqdxb2"]
    }
  }
  headers = {
    "Authorization":f"Bearer {LoginData['data']['idToken']}"
  }
  output = {
    "status_code": 200
  }
  response = client.post(f'/interactions',json=input_['json'], headers = headers)
  assert response.status_code == output['status_code']

def test_success_delete_my_given_ticket():
  input_ = {
    "json": {
      "interactionidList": [1]
    }
  }
  headers = {
    "Authorization":f"Bearer {LoginData['data']['idToken']}"
  }
  output = {
    "status_code": 200
  }
  response = client.delete(f'/interactions',json=input_['json'], headers = headers)
  assert response.status_code == output['status_code']

