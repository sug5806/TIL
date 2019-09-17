FROM python

RUN apt-get update
RUN apt-get install -y python3 python-pip 
RUN pip install django
RUN django-admin startproject config .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
