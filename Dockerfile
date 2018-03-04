FROM python:3-alpine
COPY . /src
RUN pip install -r /src/requirements.txt
CMD python /src/zalgbot.py
