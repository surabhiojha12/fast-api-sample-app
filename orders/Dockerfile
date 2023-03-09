FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./orders /code/orders

CMD ["uvicorn", "orders.main:app", "--host", "0.0.0.0", "--port", "8080"]

# run - command -> docker build -t order_image . -f orders/Dockerfile 
# docker run --name my_order_container -p 8080:8080 order_image
