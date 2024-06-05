Это приложение на Python предназначено для захвата сетевых пакетов в реальном времени и выявления сетевых аномалий, таких как DNS spoofing и port scanning. Приложение также может эмулировать эти аномалии для тестирования функций обнаружения.

## Функциональные возможности

1. **Захват данных**: Приложение захватывает сетевые пакеты в реальном времени с использованием библиотеки `scapy`.
2. **Анализ и выявление аномалий**:
    - **DNS Spoofing**: Обнаружение поддельных ответов DNS.
    - **Port Scanning**: Обнаружение попыток сканирования портов.
3. **Эмуляция сетевых аномалий**:
    - Эмуляция DNS spoofing.
    - Эмуляция port scanning.

## Установка

1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/dkrimin/network4150

    ```

2. Установите необходимые зависимости:
    ```bash

    ```

## Использование

### Захват и анализ пакетов

Для запуска захвата и анализа сетевых пакетов в реальном времени, запустите index.py`:
```bash
python index.py
```



```



### Пример вывода

При обнаружении аномалий в консоли будут отображаться предупреждения:

```
[ALERT] DNS Spoofing detected: ya.ru-> 1.2.3.4

```

## Структура проекта

- `index.py`: Основной скрипт, выполняющий захват, анализ и эмуляцию сетевых пакетов.
## Требования

- Python 3.6 или выше
- Установленные библиотеки  
- Права администратора для захвата сетевых пакетов (на некоторых системах)

## Зависимости

Приложение использует следующие библиотеки Python:

- `scapy`: Для захвата и анализа сетевых пакетов
- `threading`: Для запуска захвата пакетов в отдельном потоке

Установите зависимости с помощью команды:

```bash
pip install  
```
## Замечания

1. Убедитесь, что вы имеете соответствующие права для захвата сетевых пакетов на вашем устройстве.
2. Приложение должно запускаться с правами администратора (или sudo), чтобы захватывать пакеты на сетевом интерфейсе.

Результат выполненеия программы.


Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Install the latest PowerShell for new features and improvements! https://aka.ms/PSWindows

Warning: PowerShell detected that you might be using a screen reader and has disabled PSReadLine for compatibility purposes. If you want to re-enable it, run 'Import-Module PSReadLine'.

PS C:\itmo\network4150> python .\index.py

.
Sent 1 packets.
Sent spoofed DNS response for ya.ru to 192.168.1.10 with IP 1.2.3.4
.
Sent 1 packets.
Sent SYN packet to 192.168.1.10:22
.
Sent 1 packets.
Sent SYN packet to 192.168.1.10:80
.
Sent 1 packets.
Sent SYN packet to 192.168.1.10:443
.
Sent 1 packets.
Sent SYN packet to 192.168.1.10:8080
[ALERT] DNS Spoofing detected: ya.ru-> 1.2.3.4





