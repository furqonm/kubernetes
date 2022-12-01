FROM public.ecr.aws/docker/library/python:3.9.15-alpine3.16
WORKDIR /project
ADD . /project
RUN pip install -r requirements.txt
ENTRYPOINT ["python","app.py"]
