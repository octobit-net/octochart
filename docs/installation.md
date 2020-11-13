# Installation Guide

By default, Dash apps run on localhost - you can only access them on your own machine.

## Localhost

This example requires Python and pip.

0. Pre Requirements
Install Python, and pip (Python) on your system.
Clone or Download Repository at: <https://github.com/octobit-net/octochart>

1. Install all dependencies.  
`pip install dash`  
`pip install plotly_express`  
`pip install pickle`  
`pip install pandas`  
`pip install xlrd`  
Start the App with:  
`python app.py`  
If it builds correctly, you will see something like this in your Terminal:  
`*Dash is running on http://127.0.0.1:8050/*`  
Now you can open your Browser an visit your localhost.  

2. (Optional) Update the data and figure in create_dataset.py  
`python /scripts/create_dataset.py`
or simply use update_fig.sh

3. (Optional) Offline Mode 
uncomment dataset paths in scripts/create_dataset.py  
    `raw_dataset_path_rubella = f.RAW_PATH + f.parser['path']['rubella']`  
    `raw_dataset_path_measles = f.RAW_PATH + f.parser['path']['measles']`  
instead comment dataset paths in scripts/create_dataset.py  
    `#raw_dataset_path_measles = '...'`  
    `#raw_dataset_path_rubella = '...'`  
If you still need up to date data from the who page you can download them at: <https://www.who.int/>
or simply use update_data.sh (To run update data script, you need to have wget installed)

## Server

To share this Dash app, you need to deploy it to a server, running Flask applications.
Heroku is an simple platform for that deployment method.

### Example for Heroku

This example requires also a Heroku account, git, and virtualenv.  
0. Install heroku, git and virtualenv on your system.  

1. Create a new folder for your project.  
`mkdir dash_app_example`  
`cd dash_app_example`  
2. Initialize the folder with git and a virtualenv.  
`git init        # initializes an empty git repo`  
`virtualenv venv # creates a virtualenv called "venv"`  
`source venv/bin/activate # uses the virtualenv`  
virtualenv creates a fresh Python instance. You will need to reinstall your app's dependencies with this virtualenv:  
`pip install dash`  
`pip install plotly_express`  
`pip install pickle`  
`pip install pandas`  
You will also need a new dependency, gunicorn, for deploying the app:  
`pip install gunicorn`  
3. Initialize Heroku, add files to Git, and deploy  
`heroku create my-dash-app # change my-dash-app to a unique name`  
`git add . # add all files to git`  
`git commit -m 'Initial app _'`  
`git push heroku master # deploy code to heroku`  
`heroku ps:scale web=1  # run the app with a 1 heroku "dyno"`  
You should be able to view your app at <https://my-dash-app.herokuapp.com>
4. When you modify app.py with your own code, you will need to add the changes to git and push those changes to heroku.  
`git status # view the changes`  
`git add .  # add all the changes`  
`git commit -m 'a description of the changes'`  
`git push heroku master`  
If you modify Python dependencies. You can fill this file in automatically with:  
`pip freeze > requirements.txt`  

### Stay up to date (Automating Scripts)

The server-side script *update_fig.sh* should be run at least one time a month. You can easily automate this on your own server.
