# stock market prediction


## Developing guide:

### 1. download the repository:
```console
$ git clone https://github.com/aalarifi2016/stock_market_prediction.git
```
### 2. Install the requirements:
```console
$ pip install -r requirements.txt
```
### 3. migrate:
every time you change the code, you should use this command:
```console
$ python3 manage.py makemigration
$ python3 manage.py migrate
```

### 4. run server:

```console
$ python3 manage.py runserver
```

### 5. create a new app:
to create a new app, you have to use the command below. remember that a new app means a new module or component in the project. 
```console
$ python3 manage.py startapp your_app
```



