FROM python:3.11-slim
WORKDIR /Documents/SIT Y1T1/INF1103/lab/lab 2
COPY modular_auditor.py .
CMD ["python","modular_auditor.py"]

#docker build -t inf1103-labs-smart-auditor .
#docker run --rm -it -v "${PWD}:/usr/src/app" -w /usr/src/app python:3.11-slim python auditor.py