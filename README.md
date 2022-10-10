<img src = "https://user-images.githubusercontent.com/48649849/194794889-3d3dc808-25f7-4c91-bfd5-10f9294e2d41.png" width="1080" height="200"/> 
  
  

  
  
![This is an image](https://img.shields.io/badge/purpose-Software_Engineering-blue)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7145407.svg)](https://doi.org/10.5281/zenodo.7145407)![Uploading SlackPoint logo (1).png…]()

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Github](https://img.shields.io/badge/language-python-red.svg)](https://docs.python.org/3/)
[![build](https://github.com/mithildani/se22-hw1-grp14/actions/workflows/test.yml/badge.svg)](https://github.com/nehakale8/slackpoint/actions)
[![GitHub top language](https://img.shields.io/github/languages/top/nehakale8/slackpoint)](https://docs.python.org/3/)
[![GitHub last commit](https://img.shields.io/github/last-commit/nehakale8/slackpoint)](https://github.com/nehakale8/slackpoint/commits/main)
[![codecov](https://codecov.io/gh/nehakale8/slackpoint/branch/main/graph/badge.svg?token=1H92SAVB5S)](https://codecov.io/gh/nehakale8/slackpoint)


Gamify your slack tasks! 💻


A lot of teams use Slack to get things done. However when you have ton of things to do with no short term rewards in sight, it gets difficult to check off those tasks. That's where SlackPoint comes to the rescue! SlackPoint aims to make work more fun and get people motivated to finish their tasks by gamifying Slack!


https://user-images.githubusercontent.com/68791644/194795317-2115c60b-adb9-42ba-88d3-868f57001278.mp4


## Built with
  <img src = "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original.svg" width="40" height="40"/> Flask
  <br/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="40" height="40" /> Python
  <br/>
 <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg" width="40" height="40" /> PostgreSQL

### How the Hell do you use this?

List of miracles that slackpoint can perform✨:

* Create a new task
* Mark task as done
* View pending tasks
* View completed tasks
* Ask for help

lets go over these one by one...

#### **1. Create new task:**

You can create a new task by simple using the ``/create-task`` command. We ask for just a few more parameters in addition to that:

Command: ``/create``

![Create Task GIF](https://i.imgur.com/lUtX23a.gif)

This particular command will create a new task with the description as ``Hey! This is my new task`` having ``100`` points and a deadline of ``15th October 2022``

#### **2. Mark task as done:**

Here you can mark a task as completed. You just need to give the task ID as a parameter

Command: ``/task-done [task ID]``

Example:
``/task-done 10214``

![Task Done GIF](https://i.imgur.com/gOB6dVs.gif)

This will mark the task having task ID ``10214`` as completed. Further, updates records to show that this task is completed by user who posted this command

#### **3. View pending tasks:**

This command will return the list of incomplete tasks. Relax! no parameters required here

Command: ``/viewpending [no parameters]``

![View pending GIF](https://i.imgur.com/TAnNoSO.gif)

Above command will display a list of pending tasks

#### **4. View completed tasks:**

Like the above command this will return a list of completed tasks. No parameters here as well!

Command: ``/viewcompleted [no parameter]``

![View completed GIF](https://i.imgur.com/3SFQU2N.gif)

Above command will display a list of completed tasks

#### **5. Leaderboard:**

Want to get competitive? Take a peek at the leaderboard and try to beat the winner!

Command: ``/leaderboard [no parameters]``

![Leaderboard GIF](https://i.imgur.com/LNfVFHX.gif)

It displays the list of the top performers on the channel along with their points.

#### **6. Help:**

Newbie at using slackpoint? You could use some help...

Command: ``/help [no parameters]``

![Help GIF](https://i.imgur.com/RNykp6p.gif)

This will provide you will all the available commands and how to use them. Same sh*t this section is doing.

## Project documentation
The `docs` folder incorporates all necessary documents and documentation in our project.

## Tools used
Code formatter: black and flake8

Tech stack: Flask, PostgreSQL
 
## 📖 Getting started:

  - ### Prerequisite:
      - Download [Python3.x](https://www.python.org/downloads/).
      - Download [Flask](https://flask.palletsprojects.com/en/2.2.x/installation/).
      - Download [PostgreSQL](https://www.postgresql.org/download/)
      - Download [Pgadmin](https://www.pgadmin.org/download/)

   ## Run Locally

Create a virtual environment:

```bash
  python3.x -m venv test_env
```

Activate the virtual environment:
Linux/MacOS:
```bash
  source test_env/bin/activate
```
Windows:
```bash
  ./test_env/Scripts/activate
```

Clone the project

```bash
  git clone https://github.com/nehakale8/slackpoint.git
```

Go to the project directory

```bash
  cd Slackpoint
```

Install dependencies

```bash 
  pip install -r requirements.txt
```
Log on to api.slack.com and create your own slack bot.

On ngrok shell run 'ngrok http 5000' to get the public IP address in your local machine. 

Finally add all the /commands in the bot configuration and paste the url from ngrok shell to requesting url section in the bot configuration.

Start the server

```bash
  flask run
```

     - Site will be hosted at:
       `http://127.0.0.1:5000/` 
       
Before creating the database, 

(1) Change the local path of PostgreSQL in .env file (DATABASE_URL= 'postgresql://postgres:(password)@localhost/(database name from PgAdmin') 

(2) Provide the Slack sigining secret and Slack bot token from the bot you created. 

To create tables in the database,
```bash
First run the command 'flask shell'
Next command to create the database - 'db.create_all()'
```
 
### Project Dependencies

* flask
* slackclient
* python-dotenv
* slackeventsapi
* flask-sqlalchemy
* psycopg2
* pytest
* pytest-mock
* black
* pylint
* coverage
* pytest-cov

### Future of this project

* Assign users to tasks while creating each task
* Add a command to reassign users
* Add a command to edit an existing task
* Progress of a task is currently binary. It can be improved to allow a percentage progress improvement
* Deploy the service on the cloud
* Improve code coverage
* UI/UX: Improve leaderboard command response to show gifs/graphs to further make the leaderboard more attractive and gamify it


## Developed by RoachPack

Heyy! We are a group of Graduate students at NC State University, or to be more specific, we are dreamers who want to be pioneers of the Computer Science world.
Consider this homework to be one of our many steps at achieving our dreams! :wink:

### Why RoachPack?
Good question!
We are international students, visiting the United States for the first time. We all live near the Centinnial campus of NC State University.
Our eyes ready to take in the grandeur and technological advancements of the United States, we were rather welcomed by a group of Anthropods which we all are afraid of.
Yup, you guessed it right. Cockroaches!
To overcome this fear and to take on challenges, we have named our group **RoachPack**! :muscle:

### Chat Channel

<code><a href="https://app.slack.com/client/T03VB79B2GG/C03U705CJ15" target="_blank"><img height="30" width="100" src="https://user-images.githubusercontent.com/111834635/194175304-834d5663-b6bb-4e38-981d-98bc1bf028b8.png"></a></code>


### Meet our team
- [@MithilDani](https://www.github.com/mithildani)
A studious nearsighted bespectacled charming individual who is an expert at building Django applications, designing optimal solutions and has an extensive work experience of 2 years in the IT industry.
- [@NehaKale](https://www.github.com/nehakale8)
A hardworking bespectacled Machine Learning expert who has multiple AI and ML projects and research paper contributions. She is an expert at providing out-of-the-box solutions and always has an unique perspective.
She also provides our group with the much needed diversity :sweat_smile:
- [@RishikeshYelne](https://www.github.com/rishikesh-yelne)
An old, very old, almost ancient bespectacled individual (so many bespectacled members :nerd_face:) with a work experience of 5 years in the IT industry. He is proficient and well-versed with the .NET Framework, which he claims to be highly relevant and at par with the newer technologies. Let's just respect his ancient age and agree with him for now. *-laughs in Python-*
- [@VanshMehta](https://github.com/vanshmehta-7)
A self-proclaimed charming good-looking handsome individual who is a Java enthusiast. A constant source of good jokes and efficient code, he has charmed his way into our group, just like Shah Rukh Khan does it in Bollywood movies.
- [@RitwikVaidya](https://www.github.com/ritwik4690)
A no-nonsense serious and dedicated prankster / comedian of the group, with an unique knack at solving programming questions and a strong supporter of C++ programming language.

### Reach out to us!

For any doubts or queries, reach out to our Developer Team @ slackpoint.developers@gmail.com
