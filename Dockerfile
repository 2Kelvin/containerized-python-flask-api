FROM python:3.14-alpine
WORKDIR /python-api
COPY . .
RUN pip install flask==3.1.2
EXPOSE 5000
CMD [ "python3", "app.py" ]
