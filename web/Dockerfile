FROM centos:latest
RUN yum update -y

RUN yum -y install epel-release && yum clean all
RUN yum -y install python-pip && yum clean all

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
#ENTRYPOINT ["python"]
CMD ["python", "app.py"]
