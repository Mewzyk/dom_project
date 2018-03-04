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

## Infastructure
* There are two AWS EC2 Servers running that provide our application functionality.
* Application server: 18.222.10.95
* Mongo server: 18.219.228.163

## Data Ascess
* The function get_route_data for the application server returns a json object with the desired route data. 

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

## Setting up MongoDB/PyMongo

* Get PyMongo
```
pip3 install Flask-PyMongo
```
* Get MongoDB
```
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2930ADAE8CAF5059EE73BB4B58712A2291FA4AD5
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.6 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.6.list
sudo apt-get update
sudo apt-get install -y mongodb-org
```
* Start MongoDB
```
sudo service mongod start
```
* Enter mongo
```
mongo
```
* Run the update_db.py to populate the db
* Put index on mountainproject id field
```
db.routes.createIndex( { "id" : 1 }, { unique: true } )
```
