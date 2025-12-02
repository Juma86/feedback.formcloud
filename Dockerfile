FROM python:alpine3.22

COPY . /app/

WORKDIR /app/

RUN pip install -r requirements.txt

CMD ["hypercorn", "uk.formcloud.feedback.api:app", "--config", "hypercorn_config.toml"]