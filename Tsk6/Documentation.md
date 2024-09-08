####TinyDB
###Overview
TinyDB is a lightweight, document-oriented database written in Python. It is designed for scenarios where a full-featured database system is overkill, and where simplicity and ease of use are paramount.
###Functionality
##Database Commands:
# 1. Create a Database
Create or open a TinyDB database:
```
db = TinyDB('db.json')
```
#2. Truncate the Database
Remove all documents without deleting the file:
```
db.truncate()
```
##Data Manipulation Commands:
# Insert Data
Insert documents (dictionaries) into the database:
```
db.insert({'name': 'Alice', 'age': 28})
```
# Insert multiple dictionaries
```
db.insert_multiple([
    {'name': 'Bob', 'age': 35},
    {'name': 'Charlie', 'age': 40}
])
```
# 2. Query Data
Retrieve data using queries:
```
User = Query()
```
# Get all documents
```
all_docs = db.all()
print(all_docs)
```
# Search for specific documents
```
result = db.search(User.name == 'Alice')
print(result)
```
# Get a single document
```
single_doc = db.get(User.age > 30)
print(single_doc)
```
# Update Data
Update existing documents:
```
db.update({'age': 29}, User.name == 'Alice')
```
# Remove Data
Remove documents that match a query:
```
db.remove(User.name == 'Bob')
```
# Count Documents
Count documents matching a query:
```
count = db.count(User.age > 30)
print(count)
```
##Tables Commands:
#1. Using Tables
Organize data into tables:
```
# Create or access a table
users_table = db.table('users')
```
# Insert into the table
```
users_table.insert({'name': 'Eve', 'age': 22})
```
#Display from Table
```
table.all()
```

##Example Code:
```
from tinydb import TinyDB, Query

# Create or open the database
db = TinyDB('db.json')

# Insert data
db.insert({'name': 'Alice', 'age': 28})
db.insert_multiple([
    {'name': 'Bob', 'age': 35},
    {'name': 'Charlie', 'age': 40}
])

# Query data
User = Query()
print(db.search(User.name == 'Alice'))

# Update data
db.update({'age': 29}, User.name == 'Alice')

# Remove data
db.remove(User.name == 'Bob')

# Count documents
print(db.count(User.age > 30))

# Truncate the database
db.truncate()

```
