  
FROM python:latest

RUN groupadd user && useradd --create-home --home-dir /home/user -g user user
ADD ./requirements.txt .
RUN pip install -r requirements.txt
RUN mkdir BookshopMbicycle
ADD . BookshopMbicycle
WORKDIR BookshopMbicycle
User user