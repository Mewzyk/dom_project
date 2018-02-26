# Not Mountain Project

Project to build and maintain Full Stack Web Development Skills

### Prerequisites

What things you need to install the software and how to install them

```
python 3.5
flask 0.12
sqlalchemy x.x
pip
AWS Account
ubunutu x16.04 (production environment)
```

### Installing

```
git clone https://github.com/Mewzyk/dom_project.git
chmod +400 setup.sh (TO DO)
./setup.sh (TO DO)
```

## Deployment
To deploy, first launch an AWS EC2 Instance ubunutu server from your dashboard.

ADD INSTRUCTIONS ON HOW TO HOST AND SETUP AN EXTERNAL IP ADRESS (TO DO)

ssh into server via:
'''
ssh -i <path to .pem key> ubunutu@<ip Adress>
'''

After deploying your server, see Installing.

To launch server:
'''
python3 app.py
'''

## Built With

* [Flask](http://flask.pocoo.org/) - Webframework
* [SqlAlchemy](https://www.sqlalchemy.org/) - Database ORM
* [D3.js](https://d3js.org/) - Visualizaton Framework

## Contributing

Email me at: stephenthomasonline@gmail.com for contributor rights

## Authors

* **Stephen Thomas** - (https://github.com/mewzyk)

## TO DO

* setup server to host externally on AWS
* create template html for intial render
* learn about + connect sqlAlchemy
* create model for data
* build project directories
* create setup.sh script 
