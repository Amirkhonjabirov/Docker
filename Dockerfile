FROM python:3.10.4

WORKDIR /app

COPY requirements.txt .

RUN pip install -U pip
RUN pip install -r requirements.txt

COPY . .

CMD ["pytest", "--browser", "chrome", "--base_url", "http://192.168.100.3:8081/", "--exec", "172.18.96.1"]