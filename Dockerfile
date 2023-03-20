FROM python:3.8

WORKDIR /titanic-survivor-prediction-server

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 10000

CMD ["python", "./Flask_api/flask_api.py"]
