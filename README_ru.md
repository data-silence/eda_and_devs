# Содержание

* [About](#about)
* [Structure](#structure)
* [Stack](#stack)
* [License](#license)
 


## About
Этот проект разработан в рамках учебного курса ["Exploritary data analysis"](https://stepik.org/course/177213), созданного [AI Education](https://stepik.org/course/177213).

Целью проекта является исследование потребительского поведения покупателей онлайн-магазина с помощью инструментов data-science.

В результате исследований, которые были проведены в ноутбуках, была выбрана оптимальная предсказательная модель поведения клиентов. 

Разработано приложение, агрегирующее сведения о проведенном исследовании в виде интерактивного дашборда ExplainerDashboard.

## Structure

Первичные и обработанные данные для анализа хранятся в папке data.  

Процесс исследования данных и разработки моделей можно увидеть в файлах EDA.ipynb и pipeline.ipynb.

Работу приложения можно посмотреть с помощью докера:
```
docker pull maxlethal/explainerdashboard:latest
```
Также дашборды приложения можно увидеть в файле data/dashboard.html, или собрав приложение самостоятельно из директории app.


## Stack
Pandas

Sklearn

CatBoost

ExplainerDashboard

## License
Этот проект распространяется под лицензией MIT. Для получения дополнительной информации см. файл LICENSE.