# PocketSys (version Beta-01-19/4/17)
> Written to test functionality between **cross** python files and **mysql** connection.

![image](http://i.imgur.com/fnJBYVY.png?align=center "image")

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Pre-requisites
What things you need to install for this to work
```
- Python 2 or 3
- PIL, PyMySQL
- XAMPP (Optional) for database connection
```

### Installing
Steps to show you how to get the env deployed and working

1. To install **PIL** (Make sure you have python installed)
```
Opens command prompt
```
```
Type 'pip install Pillow'
```
To install into a specified python version (if both exists), E.G
```
$ python3 -m pip install Pillow
```
2. To install **PyMySQL**
```
Opens command prompt
```
```
Type $ pip install PyMySQL
```

## Running the tests
How to get the python files fully working

### Ensuring your database credentials matches
```
Go to login.py
```
```
See func enterButton() at Line 34 and make sure all databases match the one you are connecting to
```
```
Do the same for func createButton() at Line 105
```

### Fixing image not found error
```
Go to main.py
```
```
Either replace or remove the images at Line 21 and Line 27 respectively
```

## Deployment
Do the necessary changes mentioned above, and the program should work fine as intended

## Built With
* [Python](https://www.python.org/) - Language
* [PyCharm](https://www.jetbrains.com/pycharm/) - The IDE

## Authors
* **Myself** - *Developer*

## Notes
No longer further developing this. I've released the source code online for anyone who wish to see, learn and maybe further improve it.

Obviously this is not well coded, but it may serve as a pedagogy for beginners to learn!
