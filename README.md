# <span style= "color: yellow">**Яндекс.Самокат Autotests**</span> 

Это учебный проект Yandex.Practicum содержит автотесты на Python содержит автотесты для учебного сервиса «Яндекс.Самокат».

## <span style= "color: cornflowerblue">Реализованные тесты:</span> 

### Выпадающий список в разделе «Вопросы о важном»

Проверка соответствия текста ответа вопросу в выпадающем списке 'Вопросы о важном' 	***`test_faq_questions_answers_match`***

### Заказ самоката

Проверка успешного оформления заказа самоката ***`test_place_order_success`***

### Редиректы

Проверка редиректа на главную страницу Дзена в новой вкладке при нажатии на логотип Яндекса ***`test_redirect_to_dzen_via_yandex_logo`***

Проверка редиректа со страницы заказа на главную страницу Самокат при нажатии на логотип Самоката ***`test_redirect_to_main_via_scooter_logo`***


## <span style= "color: cornflowerblue">Технологии</span>

+ Python 3.13.5

+ Pytest

+ Selenium

+ Faker (для генерации тестовых данных)

+ WebDriverWait + Expected Conditions

+ Random (для генерации тестовых данных)

+ Allure (отчёты о тестировании)


## <span style= "color: cornflowerblue">Запуск тестов</span>

1. Клонировать репозиторий:<br/>
    ```git clone https://github.com/hradzevich/Sprint_6.git  ```

2. Установить зависимости:<br/>
    ```pip install -r requirements.txt```

3. Запустить тесты с сохранением результатов для Allure:<br/>
    ```pytest --alluredir=allure_results```

4. Сгенерировать html-отчёт в папку allure_report:<br/>
    ```allure generate allure_results -o allure_report --clean```

5. Открыть готовый отчёт в браузере:<br/>
    ```allure open allure_report```


## <span style="color: cornflowerblue">Полезные команды</span>

Очистить результаты прошлых запусков:<br/>
    ```rm -rf allure_results allure_report```

Перегенерировать отчёт без запуска тестов (если тесты уже запускались и в папке allure_results есть данные):<br/>
    ```allure generate allure_results -o allure_report --clean```
    ```allure open allure_report```

Быстрый просмотр отчёта без сохранения (отчёт откроется во временном режиме, готовая папка не создаётся):<br/>
    ```allure serve allure_results```