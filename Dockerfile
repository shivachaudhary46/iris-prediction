FROM python:3.10-slim

WORKDIR /app

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

COPY requirements.txt . 
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["flask", "run"]

