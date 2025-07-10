FROM python:3.9-slim

WORKDIR /app

COPY req.txt .
RUN pip install -r req.txt

COPY . .

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
