FROM python:3.12.8-alpine3.21

RUN apk update && \
    apk add curl

RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"

WORKDIR /opt/web_fastapi
COPY . .
RUN poetry install --with main

EXPOSE 8000

HEALTHCHECK --interval=5s --timeout=10s --retries=3 CMD curl -sS http://localhost:8000/api/ping | grep -q pong || exit 1

ENTRYPOINT [ "poetry" ]

CMD [ "run", "python", "main.py" ]
