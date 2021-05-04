FROM python:3.9-slim
ENV FIREBASE_CREDENTIAL_FILE_PATH /app/.env/ticketter-firebase-adminsdk-ld1je-dafb5ab713.json
ENV IDPLATFORM_API_KEY_FILE_PATH /app/.env/IDPlatform.json
ENV CLOUD_MYSQL_IDPASS_FILE_PATH /app/.env/Mysqlidpass.json
ENV APP_HOME /app
ENV PYTHONPATH "${PYTHONPATH}:${APP_HOME}"

WORKDIR $APP_HOME
COPY . ./
RUN pip install -r requirements.txt

CMD exec gunicorn --bind :$PORT --workers 1 --worker-class uvicorn.workers.UvicornWorker  --threads 8 main:app