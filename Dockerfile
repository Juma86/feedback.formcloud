FROM python:alpine3.22

COPY . /app/

WORKDIR /app/

RUN pip install -r requirements.txt

CMD ["python3", "uk.formcloud.feedback.api.py"]