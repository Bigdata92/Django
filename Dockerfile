#pull official base image
FROM python:3.9.0

WORKDIR /home/

RUN git clone https://github.com/Bigdata92/Django.git

# WORKDIR git clone 맞춰서 설정해줘야 함
WORKDIR /home/Django/

# install dependencies
RUN pip install -r requirements.txt

RUN echo "SECRET_KEY=django-insecure-4^+3d@t^y5oa4x5t%57pkxg5vgpa0m5d5r)7m_6(jwd2gb3$17" > .env

RUN python manage.py migrate

EXPOSE 8000
# run from working directory, and separate args in the json syntax
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]