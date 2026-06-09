# Stage 1

FROM python:3.12-slim as builder

WORKDIR /app

COPY app/requirements.txt .

RUN pip install  -r requirements.txt

# Stage 2

FROM python:3.12-slim

RUN addgroup --system appgroup && \
    adduser --system appuser

WORKDIR /app

COPY --from=builder /usr/local /usr/local

COPY app .

ENV PATH=/root/.local/bin:$PATH

RUN chown -R appuser:appgroup /app

USER appuser

EXPOSE 5000

HEALTHCHECK --interval=30s \
--timeout=5s \
CMD curl -f http://localhost:5000/health || exit 1

CMD ["gunicorn","-b","0.0.0.0:5000","app:app"]
