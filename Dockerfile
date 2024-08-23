FROM python:3.9.13

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY src/app.py /app

EXPOSE 5000

CMD [ "python", "app.py" ]
