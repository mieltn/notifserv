FROM python

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./start.sh .
RUN chmod +x start.sh

WORKDIR /app