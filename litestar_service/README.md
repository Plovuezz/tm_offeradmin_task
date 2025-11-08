## Що модифіковано


- Окрема версія `docker-compose.dev.yaml` для девелопменту
- Використано:
  - **Granian** — швидкий сервер для запуску Litestar
  - **Litestar** — асинхронний web-фреймворк запускається на http://localhost:5000, має ідентичний функціонал
  - **SQLAlchemy** з `AsyncSession` для асинхронної роботи з БД
  - Налаштовано Nginx для проксування `/api/` на Litestar
  - Використовую наявні параметри з файлу .env. Використав pydantic-settings для конфігурації застосунку.
  - Є власні requirements.txt, Dockerfile
---
## Структура проєкту

```
litestar_service/
├── app/
│   ├── api/
│   │   └── offerwalls/          # Роути API
│   │       └── __init__.py
│   ├── crud/
│   │   └── offer_walls.py       # Логіка взаємодії з БД
│   ├── database/
│   │   ├── db.py                # Підключення та сесії
│   │   └── models.py            # ORM моделі
│   ├── config.py                # Налаштування через pydantic-settings
│   ├── exceptions.py            # Обробники помилок
│   ├── main.py                  # Точка входу для запуску сервісу
│   ├── applications.py          # Функція build_app() для створення Litestar App
│   └── schemas.py               # Pydantic-схеми для валідації
├── requirements.txt             # Залежності проєкту
├── Dockerfile                   # Докер образ сервісу

```
## Запуск

Запуск девелопмент-версії:

```bash
docker-compose -f docker-compose.dev.yaml up --build
```


