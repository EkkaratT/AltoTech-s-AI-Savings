FROM python:3.10-slim

WORKDIR /app

COPY . /app
COPY model/best_model.pkl model/

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
