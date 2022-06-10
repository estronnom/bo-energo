FROM python

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5002

CMD gunicorn --bind 0.0.0.0:5002 app:app