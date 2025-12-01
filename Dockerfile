FROM python:alpine3.22

COPY . /app/

WORKDIR /app/

RUN pip install -r requirements.txt

CMD ["uvicorn", "uk.formcloud.feedback.api:app", "--host", "0.0.0.0", "--port", "50000"]