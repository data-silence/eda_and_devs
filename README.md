# Content

* [About](#about)
* [Structure](#structure)
* [Stack](#stack)
* [License](#license)
 


## About
This project is developed as part of the ["Exploratory data analysis"](https://stepik.org/course/177213) course created by [AI Education](https://stepik.org/course/177213).

The aim of the project is to investigate the consumer behavior of online shopping customers using data-science tools.

Through notebook research, an optimal predictive model of customer behavior was selected. 

An application has been developed that aggregates the research conducted in the form of an interactive ExplainerDashboard.

## Structure

Primary and processed data for analysis are stored in the .\data folder.  

The process of data exploration and model development can be seen in the files EDA.ipynb and pipeline.ipynb.

The work of the application can be viewed using the docker:
```
docker pull maxlethal/explainerdashboard:latest
```
You can also see the application dashboards in the data/dashboard.html file, or by building the application yourself from the app directory.


## Stack
Pandas

Sklearn

CatBoost

ExplainerDashboard

## License
This project is distributed under the MIT license. Please see the LICENSE file for more information.