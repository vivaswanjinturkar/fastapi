FROM python:3.7
RUN pip install fastapi uvicorn

EXPOSE 80
COPY ./app /app
WORKDIR /app
COPY /app/requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]