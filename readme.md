**Lazyman's Flask Kickstarter**

It does an awesome job at kicking your start, but you require some stuff before you begin:

* python3
* python3-pip
* libcurl4-openssl-dev
* python-virtualenv

Install all as such:
`sudo apt install python3 python3-pip libcurl4-openssl-dev -y && pip3 install virtualenv`

---

How to setup?

Clone, create virtual env, install dependencies, change config and GO!

Clone the repo:

  `git clone https://github.com/d3vzer0/kickstart-flask.git`

Access directory:

  `cd kickstart-flask`

Create virtual environment:

  `virtualenv venv`

Activate virtual environment:

  `. venv/bin/activate`

Install dependecies:

  `pip3 install -r requirements.txt`

Then edit the config to your likings: 

  `cp app/configs/variables.py.example app/configs/variables.py`
  
  `vim app/configs/variables.py`

When all is said and done: 

  `python3 run.py`
