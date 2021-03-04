FROM python:3.9-alpine

ARG UDEMY_API_KEY
ENV UDEMY_API_KEY ${UDEMY_API_KEY}

ARG DISCORD_WEBHOOK_URL
ENV DISCORD_WEBHOOK_URL ${DISCORD_WEBHOOK_URL}

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]