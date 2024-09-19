# E2E-UI

## 1. Описание <a id=1></a>
Тест написанный для проверки сценария. Автотест реализован на Python 3 и Selenium Webdriver. В качестве тестового framework используется pytest. Реализован паттерн PageObject. 

Cтруктура репозитория:
```
Dev
 └── E2E-UI
     ├── pages
     │   ├── base_app.py                   <- Файл с базовыми методами для работы с WebDriver
     │   ├── cart_page.py                  <- Файл с методами для работы с WebDriver в корзине
     │   ├── checkout_complete_page.py     <- Файл с методами для работы с WebDriver на странице подтверждения успешной покупки
     │   ├── login_page.py                 <- Файл с методами для работы с WebDriver на странице авторизации
     │   └── select_product_page.py        <- Файл с методами для работы с WebDriver на странице выбора продукта
     ├── tests
     │   └── test_scenario.py              <- Файл с тестами по сценарию
     ├── utilits
     │   └── words.py                      <- Файл с используемыми строками
     ├── .gitignore
     ├── chromedriver_options.py           <- Файл с опциями для работы WebDriver
     ├── conftest.py                       <- Файл с микстурами
     ├── pytest.ini                        <- Файл с настройками pytest
     ├── README.md
     └── requirements.txt                  <- Файл с зависимостями
```
---
## 2. Команды для локального запуска <a id=4></a>

Перед запуском необходимо склонировать проект:
```bash
git clone git@github.com:kekul78/E2E-UI.git

```

Cоздать и активировать виртуальное окружение:
```bash
Linux: python3 -m venv venv
Windows: python -m venv venv
```
```bash
Linux: source venv/bin/activate
Windows: source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:
```bash
Linux: python3 -m pip install --upgrade pip
Windows: python.exe -m pip install --upgrade pip
```
```bash
pip install -r requirements.txt
```

Запустить автотест:
```bash
pytest
```
---
## Стек технологий

* Python 3.11.3,
* Pytest 8.3.2,
* Selenium 4.23.1

Автор: 
* [Канцулин Данил](https://github.com/kekul78)
