# exchange
crypto_exchange

## Запуск проекта

- Клонировать репозиторий https://github.com/Kaya94/exchange

- Установить и активировать виртуальное окружение    
```
Для пользователей Windows:
python -m venv venv
source venv/Scripts/activate
python -m pip install --upgrade pip
```
- Установить зависимости из файла requirements.txt
```
pip install -r requirements.txt
```
 - Создать .env и записать в него следующие значения:
 ```
# Datababse
DB_USER=postgres
DB_HOST=localhost
DB_PASS=WW9JUQhP
DB_NAME=new_exchange
DB_PORT=5432

# Redis
REDIS_DATABASE=1
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_PASSWORD=WW9JUQhP
REDIS_USERNAME=kaya

# Debug and logging
LOGGING_LEVEL=1

# Admin secret_key
SECRET_KEY=Ezjell

# Binance API
BINANCE_API_KEY=PWQDSzJhG5jsBMSpdZr9GHPOi92yJUVIYrVenOxd8O4iK0WlO94pvOAoDOoQauRl
SECRET_KEY_BINANCE=s9X6SeUSXwBH7ZyVxYNTVkCwPxOlpqACqM3gw1uDlKdmTksg6zRoJIPgU7uuXCLn

# Yadisk token
YADISKTOKEN=y0_AgAAAABOb2CTAApu8AAAAADrtyYe9s_WCX40S7CE91tdAnRnrGvMXG8

#AdminAuth
ADMIN_AUTH=WW9JUQhP

# JWT
# A constant secret which is used to encode the token.
SECRET_JWT=SECRET

#User Menager secret
SECRET_USER_MENAGER=WW9JUQhP
```
- Заресторить дамп бд через pgadmin
- Установить и запустить редис на ubuntu
```
redis-server --daemonize yes
```
- переходим в src и запускаем main.py
```
py main.py
```
И полюбому что то пойдет не так
