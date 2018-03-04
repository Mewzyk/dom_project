# Mongo Experiments

## Tutorial
* Retrieve Sample Dataset
```
wget https://raw.githubusercontent.com/mongodb/docs-assets/primer-dataset/primer-dataset.json
```
* Import Data into mongodb
```
mongoimport --db test --collection restaurants --drop --file primer-dataset.json
```
