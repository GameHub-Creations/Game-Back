#### Запуск тестов локально

1. Установить библиотеки

```bash
pip install -r requirements.txt
```

2. Запустить тесты

```bash
python -m pytest -n 2 tests/test_play_chiken.py
```

#### Запуск сервиса

1. Запуск приложения

```bash
uvicorn network.server.main_server:app --reload
uvicorn network.server.socket_chicken:app --reload
```

###### (Адрес, где будет крутиться сервис)

###### (http://127.0.0.1:8000/)

###### (Адрес документации на сервис)

###### (http://127.0.0.1:8000/docs)

