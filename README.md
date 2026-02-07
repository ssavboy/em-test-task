# EM Docker Task

Простое веб-приложение с Python backend и Nginx reverse proxy в Docker контейнерах.

**curl http://localhost** → **"Hello from Effective Mobile!"**
    
## Технологии

- Python 3.11 (http.server)
- Nginx 1.25 (reverse proxy)
- Docker + Docker Compose
- Отдельная Docker сеть

## Запуск

```bash
git clone https://github.com/ssavboy/em-test-task.git
cd em-test-task
docker compose up -d
curl http://localhost
```

## Структура проекта

```
.
├── backend/
│   ├── Dockerfile
│   └── app.py
├── nginx/
│   └── nginx.conf
├── docker-compose.yml
└── README.md
```

## Команды управления

```bash
docker compose up -d        # Запуск
docker compose down         # Остановка
docker compose logs -f      # Логи (em_backend, em_nginx)
docker compose ps           # Статус
```

## Архитектура

```
Клиент → Nginx:80 → Docker сеть → Backend:8080
```

Backend доступен только внутри Docker сети, Nginx — единственная точка входа.

***

**MIT License**