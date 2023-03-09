FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./users /code/users

CMD ["uvicorn", "users.main:app", "--host", "0.0.0.0", "--port", "8000"]

# run - command -> docker build -t user_image . -f users/Dockerfile 
# docker run --name my_user_container -p 8000:8000 user_image
