# Stage 1
FROM python:3.12-slim AS builder

WORKDIR /app

COPY app/requirements.txt .

RUN pip install -r requirements.txt

# Stage 2
FROM python:3.12-slim

RUN apt-get update && \
    apt-get install -y curl && \
    rm -rf /var/lib/apt/lists/*

RUN addgroup --system appgroup && \
    adduser --system appuser

WORKDIR /app

COPY --from=builder /usr/local /usr/local

COPY app .

RUN chown -R appuser:appgroup /app

ENV HOME=/tmp

USER appuser

EXPOSE 5000

HEALTHCHECK --interval=30s --timeout=5s \
CMD curl -f http://localhost:5000/health || exit 1

CMD ["gunicorn","-b","0.0.0.0:5000","app:app"]
