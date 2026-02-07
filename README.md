# EM Docker Task

Простое веб-приложение с Python backend и Nginx reverse proxy в Docker контейнерах.
   
**curl http://localhost** → **"Hello from Effective Mobile!"**

## Технологии

<img src="https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white" /> <img src="https://img.shields.io/badge/Docker%20Compose-2496ED?style=for-the-badge&logo=docker&logoColor=white" /> <img src="https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white" /> <img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" />

- Python 3.11 (http.server)
- Nginx 1.25 (reverse proxy)
- Docker + Docker Compose
- Отдельная Docker сеть

## Запуск

```bash
git clone https://github.com/ssavboy/em-test-task.git
cd em-test-task
cp .env.example .env
docker compose up -d
curl http://localhost/
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
