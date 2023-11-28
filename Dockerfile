FROM python:3.8

WORKDIR /tests

COPY requirements.txt .
COPY behave.ini .
COPY assets/ assets/
COPY features/ features/
COPY steps/ steps/

RUN pip install -r requirements.txt

CMD ["behave"]