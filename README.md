# Ticketter
 
<u>Private certificate</u>(* Hereinafter referred to as a "ticket") creating & sending application.

[Ticketter](https://ticketter.web.app "link to Ticketter")
 

# Features
 
* Authenticate user ( thanks to Google Identity Platform and Firebase Authentication )
  * Users are able to connect their account with twitter account.
  * This strengthens the proof of the account and, as a result, increases the value of the certificate.
  * we have plan to prepare more provider for authentication, like facebook or Instagram... .
* Limits of number
  * User can create their ticket up to 3
  * User can have up to 100 volume for each their ticket. 
  * These restrictions allow the creator to freely determine the value of the ticket.
 
# Requirements
 
* Backend

  Langage: python
  
  Framework: FastAPI
  ```Pipfile
  [packages]
  fastapi = "*"
  firebase-admin = "*"
  pydantic = "*"
  sqlalchemy = "*"
  pymysql = "*"
  async-exit-stack = "*"
  async-generator = "*"
  gunicorn = "*"
  uvicorn = {extras = ["standard"], version = "*"}

  [dev-packages]
  pytest = "*"

  [requires]
  python_version = "3.9"
  ```
  
  
* Frontend

  Langage: Javascript
  
  Framework: Vue
  ```json
  "dependencies": {
      "axios": "^0.21.1",
      "bootstrap": "^4.6.0",
      "bootstrap-vue": "^2.21.2",
      "core-js": "^3.6.5",
      "firebase": "^8.5.0",
      "firebase-admin": "^9.7.0",
      "firebaseui": "^4.8.0",
      "vue": "^2.6.12",
      "vue-axios": "^3.2.4",
      "vue-router": "^3.5.1"
    },
    "devDependencies": {
      "@vue/cli-plugin-babel": "~4.5.0",
      "@vue/cli-plugin-eslint": "~4.5.0",
      "@vue/cli-plugin-router": "^4.5.12",
      "@vue/cli-service": "~4.5.0",
      "babel-eslint": "^10.1.0",
      "eslint": "^6.7.2",
      "eslint-plugin-vue": "^6.2.2",
      "vue-template-compiler": "^2.6.11"
    },
  ```

# Installation
* Backend
 
  ```bash
  $(home) cd ${Project dir}
  $(Project dir) pipenv install
  ```

* Frontend

  ```bash
  $(home) cd ${Project dir}
  $(Project dir) npm install
  ```

# Usage

* Backend
  
  serve as development
  ```bash
  $(Project dir) python main.py
  ``` 
  or
  ```bash
  $(Project dir) uvicorn app:main --host 0.0.0.0 --port 8080
  ```
  
* Frontend
  
  serve as development
  ```bash
  $(Project dir) npm run serve
  ```
  
  build
  ```bash
  $(Project dir) npm run build
  ```
  
  hosting with firebase
  ```bash
  $(Project dir) firebase init
  ... init configs(set hosting directory from public(default) to dist)
  $(Project dir) firebase deploy
  
  ```

# Points
* Backend

  <img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" width="200px"></img>
  * [FastAPI](https://fastapi.tiangolo.com/ja/ "FastAPI") for RESTAPI server 
  
    Thanks to FastAPI, we can quickly develop endpoints and release submit specifications based on swagger ui. [here](https://ticketter-fi7wohnrcq-an.a.run.app/docs)
  
    Furthermore, it provides easy implementation of idToken validation
  
  
  
  <img src="https://www.gstatic.com/devrel-devsite/prod/v1674d466be3b1154327dd11cf186e748303b1e92ae31ff35df0f5192fbd777ea/cloud/images/cloud-logo.svg" width="200px"></img>
  
  * gcloud SDK
  
    Using gcloudSDK for validation of idToken, we can create safe connection with frontend.
  
    We create idToken with Firebase for now. In the future, we will implement custome idToken for less dependency.
  
  * cloudSQL (MySQL)
  
    We choose cloudSQL for our database. Just for easy setup, reliability, scalability and affinity for GPC.
    
* Frontend

  <img src="https://www.gstatic.com/devrel-devsite/prod/va16bb1b8e431a4d4f63ff4fba8ff7086a1107b3790bb14961ea206ea5eda2218/firebase/images/lockup.png" width="200px"></img>
  
  * Firebase Authentication
  
    We use this for User management and idToken.
    
    In addition, it is relatively easy for the application based on Firebase to add some application provided by google. like GA or so.

 
# Author

* Author: Yoshiki Hirata
 
# License
 
Ticketter is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).
