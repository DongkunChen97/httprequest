FROM python:3-slim

WORKDIR /

RUN pip install requests
COPY Func.py /Func.py

STOPSIGNAL SIGINT
CMD ["python", "/Func.py"]
