# Generated via docker init, simplified soon after

FROM python:3.12.2-slim as base

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# RUN adduser \
#     --disabled-password \
#     --gecos "" \
#     --home "/nonexistent" \
#     --shell "/sbin/nologin" \
#     --no-create-home \
#     --uid "UID=10001" \
#     appuser

RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python -m pip install -r requirements.txt

# USER appuser

COPY . .

EXPOSE 8000

CMD gunicorn task_project.wsgi --bind=0.0.0.0:8000
