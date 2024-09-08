### TinyDB

## Overview

TinyDB is a lightweight, document-oriented database written in Python. It is designed for scenarios where a full-featured database system is overkill, and where simplicity and ease of use are paramount.

## Functionality

### Database Commands:

#### 1. Create a Database

Create or open a TinyDB database:

```python
db = TinyDB('db.json')
```

#### 2. Truncate the Database

Remove all documents without deleting the file:

```python
db.truncate()
```

### Data Manipulation Commands:

#### Insert Data

Insert documents (dictionaries) into the database:

```python
db.insert({'name': 'Alice', 'age': 28})
```

#### Insert Multiple Dictionaries

```python
db.insert_multiple([
    {'name': 'Bob', 'age': 35},
    {'name': 'Charlie', 'age': 40}
])
```

#### Query Data

Retrieve data using queries:

```python
User = Query()
```

##### Get All Documents

```python
all_docs = db.all()
print(all_docs)
```

##### Search for Specific Documents

```python
result = db.search(User.name == 'Alice')
print(result)
```

##### Get a Single Document

```python
single_doc = db.get(User.age > 30)
print(single_doc)
```

#### Update Data

Update existing documents:

```python
db.update({'age': 29}, User.name == 'Alice')
```

#### Remove Data

Remove documents that match a query:

```python
db.remove(User.name == 'Bob')
```

#### Count Documents

Count documents matching a query:

```python
count = db.count(User.age > 30)
print(count)
```

### Tables Commands:

#### 1. Using Tables

Organize data into tables:

```python
# Create or access a table
users_table = db.table('users')
```

##### Insert into the Table

```python
users_table.insert({'name': 'Eve', 'age': 22})
```

##### Display from Table

```python
users_table.all()
```

## Example Code:

```python
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
