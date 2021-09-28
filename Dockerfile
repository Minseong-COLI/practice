FROM python:3.9.0

WORKDIR /home/

RUN echo 'ashasegahdsg'

RUN git clone https://github.com/Minseong-COLI/practice.git

WORKDIR /home/practice

#RUN echo "SECRET_KEY=django-insecure-3&1ujxrsg353so%&$+q__2o$-*9_xnp$e($7@(c(q!$wiqgvzr" > .env

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

#RUN python manage.py migrate --settings=practice.settings.deploy
#
#RUN python manage.py collectstatic --noinput --settings=practice.settings.deploy

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=practice.settings.deploy && python manage.py migrate --settings=practice.settings.deploy && gunicorn --env DJANGO_SETTINGS_MODULE=practice.settings.deploy practice.wsgi --bind 0.0.0.0:8000"]