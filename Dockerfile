FROM tiangolo/meinheld-gunicorn:python3.8

WORKDIR /usr/local/app

COPY ./requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

ENV LC_ALL C.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV TERM screen

CMD python3 manage.py runserver 0.0.0.0:80