ARG PYTHON_VERSION=3.11

FROM python:${PYTHON_VERSION}-slim

# Устанавливаем curl для healthcheck и очищаем кэш
RUN apt-get update && \
    apt-get install --no-install-recommends -y curl && \
    rm -rf /var/lib/apt/lists/*

# Создаем системную группу(с низким UID/GID)
# системного пользователя(без домашней дирректории и минимальной конфигурацией)
# и назначаем ему группу
RUN groupadd -r appuser && useradd -r -g appuser appuser

WORKDIR /app

COPY app.py .

# Меняем владельца/группу для всего содержимого app/ и делаем app.py исполняемым
RUN chown -R appuser:appuser /app && chmod +x app.py

# Переключаемся на appuser, все последующие команды выполняются от appuser
USER appuser

CMD ["python", "-u", "app.py"]