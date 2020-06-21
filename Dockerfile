FROM continuumio/anaconda3:4.4.0
COPY . /usr/app/
EXPOSE 5000
WORKDIR /usr/app/
RUN pip install -r requirements.txt
RUN pip install --upgrade pip
RUN pip install pickle-mixin
CMD python app.py
