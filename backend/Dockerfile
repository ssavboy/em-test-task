FROM python:3.11-slim

RUN groupadd -r appuser && useradd -r -g appuser appuser

WORKDIR /app

COPY app.py .

RUN chown -R appuser:appuser /app && chmod +x app.py

USER appuser

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD python -c "import http.client; \
    conn = http.client.HTTPConnection('localhost', 8080); \
    conn.request('GET', '/health'); \
    res = conn.getresponse(); \
    exit(0 if res.status == 200 else 1)"

CMD ["python", "-u", "app.py"]