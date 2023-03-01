# Crude Oil Production Dashboard

This code is a Python script that creates a dashboard to visualize crude oil production data by country. The dashboard is built using the Dash framework, which is a Python library for building web applications with interactive user interfaces. The app contains two main components: a world map that shows the top 20 crude oil producers for a selected year, and a line chart that shows the production of one or more selected countries over time.

## Libraries Used

1. pandas: a Python library for data manipulation and analysis
2. plotly.express: a Python library for creating interactive visualizations
3. dash: a Python framework for building web applications with interactive user interfaces
4. dash_bootstrap_components: a Python library that provides Bootstrap components for use in Dash apps
5. dash_bootstrap_templates: a Python library that provides pre-built templates for use in Dash apps

## Data Sources
The script loads two CSV files that contain preprocessed crude oil production data, that are both extracted from the  Crude Oil Production by Country in kaggle "https://www.kaggle.com/datasets/mathurinache/crudeoilproductionbycountry":

1. Pre Process the data with **OilProductionByCountryCleaningAndPreprocessing.py** and save 'Crude Oil Production by Country Pre-processed.csv'
2. Use **OilProductionByCountryBubbleMapProcessing.py** on 'Crude Oil Production by Country Pre-processed.csv' to obtain 'TopProducersPerYear.csv'

## Dashboard Layout
The app layout consists of three main components:

1. A header with the title of the app ("Crude Oil Production Dashboard") and centered text alignment.
2. A world map with a slider to select the year, and a tooltip to show the selected year value. The map displays the top 20 crude oil producers for the selected year.
![OilBubbleMap](https://user-images.githubusercontent.com/55601081/222087783-935f6372-2e21-4f7d-a727-3b777eae2013.png)
3. A dropdown menu to select one or more countries to display on the line chart, and the line chart itself.
![OilLinePlot](https://user-images.githubusercontent.com/55601081/222087787-54994c22-c474-4242-a700-a5fcd5cd86b9.png)

## Callback Function
The app uses a callback function to update the line chart and the world map when the user interacts with the dropdown menu or the slider. The callback function takes two inputs:

A. The value of the country dropdown menu.

B. The value of the year slider.

The callback function filters the data based on the user's selections and creates two new figures using Plotly Express. The first figure is a line chart that shows the crude oil production over time for the selected countries. The second figure is a world map that shows the top 20 crude oil producers for the selected year.

## Conclusion
This Python script provides a simple and interactive way to explore crude oil production data by country. The app can be improved by adding more features such as data filtering, trend analysis, and more detailed information about each country.
