FROM locustio/locust

WORKDIR /mnt/locust

COPY . .

RUN pip3 install locust==2.10.1

RUN echo locust --version

EXPOSE 8089

EXPOSE 5557

#ENTRYPOINT ["locust","-f","locustfile.py","--host","https://restful-booker.herokuapp.com","--master"]

ENTRYPOINT ["locust","-f","locustfile.py","--worker","--master-host","65.0.131.240","--master-port","5557"]

