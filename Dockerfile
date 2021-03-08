FROM public.ecr.aws/lambda/python:3.8

ARG UDEMY_API_KEY
ENV UDEMY_API_KEY ${UDEMY_API_KEY}

ARG DISCORD_WEBHOOK_URL
ENV DISCORD_WEBHOOK_URL ${DISCORD_WEBHOOK_URL}

WORKDIR ${LAMBDA_TASK_ROOT}

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["app.handler"]