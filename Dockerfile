FROM python:3.7-alpine
RUN apk add --no-cache \
        libressl-dev \
        musl-dev \
        libffi-dev \
	gcc && \
    pip3 install --no-cache-dir cryptography && \
    apk del \
        libressl-dev \
        musl-dev \
        libffi-dev \
	gcc
COPY /requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000

CMD ["python3", "./microblog.py"]
