FROM python:3.7
WORKDIR /app
Add ./requirements /app/requirements
Add ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
ADD . /app
RUN flask db upgrade 
ENV FLASK_ENV development
CMD ["flask", "run", "--host", "0.0.0.0"]
