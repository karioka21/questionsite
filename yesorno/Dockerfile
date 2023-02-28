FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN  mkdir /questionsite
WORKDIR /questionsite

COPY requirements.txt /questionsite/
RUN pip install -r requirements.txt

COPY . /questionsite/

#EXPOSE 8000
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]