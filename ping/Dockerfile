FROM python:3.10

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN pip3 install httpx

COPY ./ping /code/ping

CMD ["uvicorn", "ping.main:app", "--host", "0.0.0.0", "--port", "8080"]

# docker build -t ping_image . -f ping/Dockerfile 
# docker run --name my_ping_container -p 8080:8080 ping_image
# docker rm my_ping_container  
