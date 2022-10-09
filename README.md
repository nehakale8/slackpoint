## SlackPoint!

![This is an image](https://img.shields.io/badge/purpose-Software_Engineering-blue)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7145407.svg)](https://doi.org/10.5281/zenodo.7145407)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Github](https://img.shields.io/badge/language-python-red.svg)](https://docs.python.org/3/)
[![build](https://github.com/mithildani/se22-hw1-grp14/actions/workflows/test.yml/badge.svg)](https://github.com/mithildani/se22-hw1-grp14/actions)
[![GitHub top language](https://img.shields.io/github/languages/top/mithildani/se22-hw1-grp14)](https://docs.python.org/3/)
[![GitHub last commit](https://img.shields.io/github/last-commit/mithildani/se22-hw1-grp14)](https://github.com/mithildani/se22-hw1-grp14/commits/main)
[![codecov](https://codecov.io/gh/nehakale8/slackpoint/branch/main/graph/badge.svg?token=1H92SAVB5S)](https://codecov.io/gh/nehakale8/slackpoint)


Gamify your slack tasks! 💻


A lot of teams use Slack to get things done. However when you have ton of things to do with no short term rewards in sight, it gets difficult to check off those tasks. That's where SlackPoint comes to the rescue! SlackPoint aims to make work more fun and get people motivated to finish their tasks by gamifying Slack!



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



Command: ``/create -d [description of task] -p [points of the task] -ddl [deadline of the task]``

Example:
``/create -d Hey! This is my new task -p 100 -ddl 15/10/2022``

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

### RoachPack

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
