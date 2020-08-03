# NanoDegree Data Engineering 

## Author 
Deivid Robim [Linkedin](https://www.linkedin.com/in/deivid-robim-200b3330/)

### Project 2: Data Modeling with Apache Cassandra

A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. 
The analytics team is particularly interested in understanding what songs users are listening to. 

Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

They'd like a data engineer to create a Postgres database with tables designed to optimize queries on song play analysis. The task is to create a star schema for Postgres and develop an ETL pipleine which will transfer the data from local files to the database.

### Project Structure
```
NanoDegree-Data-Engineering-Project-2-Data-Modeling-with-Apache-Cassandra
│   README.md # Project description
│   requirements.txt # Python packages required to execute scripts
└───data # The datasets
|   |               
|   yyyy-mm-dd-events.csv
└───src # Source code      
│   |  Project_1B_ Project_Template.ipynb # Project Notebook
```

### Requirements for running locally
- Python3 

### Datasets

- **Song dataset**: It's a subset of real data from the [Million Song Dataset](https://labrosa.ee.columbia.edu/millionsong/). 
Each file is in JSON format and contains metadata about a song and the artist of that song
```
{
    "num_songs":1,
    "artist_id":"ARD7TVE1187B99BFB1",
    "artist_latitude":null,
    "artist_longitude":null,
    "artist_location":"California - LA",
    "artist_name":"Casual",
    "song_id":"SOMZWCG12A8C13C480",
    "title":"I Didn't Mean To",
    "duration":218.93179,
    "year":0
 }
```

### Database Schema

Using the song and log datasets, you'll need to create a star schema optimized for queries on song play analysis. 

This includes the following tables.

### Fact Table
```
• songplays - records in log data associated with song plays i.e. records with page NextSong
  table schema: songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent
```
### Dimension Tables
```
• users - users in the app
  table schema: user_id, first_name, last_name, gender, level

• songs - songs in music database
  table schema: song_id, title, artist_id, year, duration

• artists - artists in music database
  table schema: artist_id, name, location, latitude, longitude

• time - timestamps of records in songplays broken down into specific units
  table schema: start_time, hour, day, week, month, year, weekday
```
### Instructions for running locally

Clone repository to local machine
```
git clone https://github.com/deivid-robim/NanoDegree-Data-Engineering-Project-2-Data-Modeling-with-Apache-Cassandra.git
```

Change directory to local repository
```
cd NanoDegree-Data-Engineering-Project-2-Data-Modeling-with-Apache-Cassandra
```

Check results

```
jupyter notebook  # launch jupyter notebook app

The notebook interface will appear in a new browser window or tab.
Navigate to src/Project_1B_ Project_Template.ipynb and run the code cells
```
