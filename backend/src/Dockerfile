FROM python:3.9-slim
ENV FIREBASE_CREDENTIAL_FILE_PATH /app/.venv/ticketter-firebase-adminsdk-ld1je-dafb5ab713.json
ENV IDPLATFORM_API_KEY_FILE_PATH /app/.venv/IDPlatform.json
ENV CLOUD_MYSQL_IDPASS_FILE_PATH /app/.venv/Mysqlidpass.json
ENV APP_HOME /app

WORKDIR $APP_HOME
COPY . ./
RUN pip install pipenv
run pipenv install

CMD exec gunicorn --bind :$PORT --workers 1 --worker-class uvicorn.workers.UvicornWorker  --threads 8 app.main:app