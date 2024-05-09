FROM python


WORKDIR /App1

COPY App1.py .
COPY record.txt .

CMD ["python3", "./App1.py"]
