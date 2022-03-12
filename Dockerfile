FROM python:buster

COPY . /blockchain

WORKDIR /blockchain

RUN pip install -r requirements.txt

WORKDIR /blockchain

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
