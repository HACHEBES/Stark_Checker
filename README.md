# Stark_Checker
Чекер сатистики по проекту StarkNet. Выдает адресс аккаунта, количество транзакций, баланс всех токенов в USDT и дату последней транзакции.

**ВНИМАНИЕ! ДАННЫЙ ЧЕКЕР ВЫДАЕТ СТАТИСТИКУ МАКСИМУМ ПО 100 АККАУНТАМ ПОТОМ НУЖНО ЖДАТЬ 2 МИН ЧТОБЫ РАЗБАНИЛО IP ЗАПРОСА**

Внесите адреса StarkNet в **wallets.txt**

Установите библиотеку aiohttp

```
pip install aiohttp
```

Запустите скрипт **async.py**

Результат будет сохранен в файл **output.txt**

После чего файл можно импортировать в **Excel**
