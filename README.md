# The Project on the module "Web Services and Applications" 


## About This Project

This project is a simple web application designed to manage family activities. It utilizes a MySQL database to store and retrieve information about various activities, including their category, name, and duration. The application is built with Python, leveraging Flask for the web framework and MySQL Connector for database interactions. It provides basic CRUD (Create, Read, Update, Delete) operations through a RESTful API.

## Use of This Project

The project can be used as a template for creating similar web applications that require a backend database for storing and managing data. It demonstrates the integration of Flask with MySQL, handling HTTP requests, and dynamically updating the web interface using JavaScript and jQuery.

## Get Started

To set up and run this project, follow these steps:

1. Install Required Packages:

* Make sure you have Python installed on your machine.

* To work with MySQL databases in the project, it needs to be installed the `mysql-connector-python` package. Use the following command to install it:

```
pip install mysql-connector-python
```
* Install Flask: 

```
pip install flask
```

2. Set up the Database: 

* Ensure you have MySQL installed and running on your machine.

* Create the database and table by running the following Python scripts:

``` 
python createDatabase.py
```
```
python createTable.py
```

3. Configure Database Connection:

* Create a `dbconfig.py` file with the following content to store your database configuration:

```python
mysql = {
  'host': "localhost",
  'user': "root",
  'password': "root",
  'database': "schedule"
}
```
4. Run the Flask server that links to an activitiesDAO: 

```
python server.py
```

5. Access the Web Interface:

* Open your web browser and go to http://localhost:5000 to access the application (open activitiesviewer.html). 


## Additionally

The table colour has been set:

```html
<table class="table" border="1" id = "activityTable" style = "background-color: pink; border-color: black">   
```

The images of activities have been added: 

```html
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Water_sports_composite.jpg/320px-Water_sports_composite.jpg" alt="Water activities">  
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Bergtocht_in_de_omgeving_van_bergdorp_S-charl_17-09-2019._%28actm.%29_01.jpg/320px-Bergtocht_in_de_omgeving_van_bergdorp_S-charl_17-09-2019._%28actm.%29_01.jpg" alt="kayaking">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/71/Mathieu_Burgaudeau_during_time_trial_training_of_Itzulia_Basque_Country_race_-_stage_1.jpg/320px-Mathieu_Burgaudeau_during_time_trial_training_of_Itzulia_Basque_Country_race_-_stage_1.jpg" alt="cicling">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0e/Inzell_2017_Kat_A1_ZBYSZEK_Kunert_-9513.jpg/320px-Inzell_2017_Kat_A1_ZBYSZEK_Kunert_-9513.jpg" alt="winter activities">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/Parapente_-_166.jpg/320px-Parapente_-_166.jpg"alt="air activities">
```


The style of the buttons has been set: 

```html
    <style>
        .btn-custom {
            background-color: purple; 
            color: white; 
            font-weight: bold; 
        }
    </style>
```

## Author

This project was created by **Yuliia Kharchenko**. 