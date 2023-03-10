FROM python:3.10

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN pip install sqlalchemy

COPY ./users /code/users

CMD ["uvicorn", "users.main:app", "--host", "0.0.0.0", "--port", "8000"]

