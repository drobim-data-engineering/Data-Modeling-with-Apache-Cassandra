# Data Engineering NanoDegree

## Author
Deivid Robim [Linkedin](https://www.linkedin.com/in/deivid-robim-200b3330/)

### Project 2: Data Modeling with Apache Cassandra

A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analysis team is particularly interested in understanding what songs users are listening to.

Currently, there is no easy way to query the data to generate the results, since the data reside in a directory of CSV files on user activity on the app.

They'd like a data engineer to create an Apache Cassandra database which can create queries on song play data to answer the questions, and wish to bring you on the project. Your role is to create a database for this analysis. You'll be able to test your database by running queries given to you by the analytics team from Sparkify to create the results.

### Project Structure
```
Data-Modeling-with-Apache-Cassandra
│   README.md # Project description
│   requirements.txt # Python packages required to execute scripts
|
└───data # The dataset
|   |
|   yyyy-mm-dd-events.csv
|   ...
└───src # Source code
│   |  ETL_Pipeline_Template.ipynb # Interactive notebook instead of python scripts
|   |  collect_events.py # Defines functions to consolidate event files
│   │  cassandra_connection.py # Defines functions to create the Cassandra
|   |  cql_queries.py   # Defines all cql queries used to create tables and insert data
|   |  etl.py           # ETL script
|   |  validation.py    # Script to validate the data
```

### Requirements for running locally
- Python3

### Dataset:
The dataset is split in 30 CSV files partitioned by day named as <font color=red>yyyy-mm-dd-events.csv</font>, located within the event_data directory.
The files contain the following schema:
```
  - artist
  - auth
  - firstName
  - gender
  - itemInSession
  - lastName
  - length
  - level
  - location
  - method
  - page
  - registration
  - sessionId
  - song
  - status
  - ts
  - userId
```
The `etl.py` script consolidates and denormalizes the daily event file into a single file named **event_datafile_new.csv**.
The image below is a screenshot of what the denormalized data should appear like in the event_datafile_new.csv after the `etl.py` run:<br>

<img src="images/image_event_datafile_new.jpg">

### Instructions for running locally

Clone repository to local machine
```
git clone https://github.com/drobim-data-engineering/Data-Modeling-with-Apache-Cassandra.git
```

Change directory to local repository
```
cd Data-Modeling-with-Apache-Cassandra
```

Create python virtual environment
```
python3 -m venv venv             # create virtualenv
source venv/bin/activate         # activate virtualenv
pip install -r requirements.txt  # install requirements (this can take couple of minutes)
```

Run scripts
```
cd src/
python -m etl.py # end-to-end pipeline from consolidating event files to loading the data on Cassandra
python -m validation.py # validates the data load on Cassandra
```

Run everything inside jupyter notebook
```
jupyter notebook  # launch jupyter notebook app

The notebook interface will appear in a new browser window or tab.
Navigate to src/ETL_Pipeline_Template.ipynb and run the code cells step by step
```
