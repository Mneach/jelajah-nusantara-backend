# Infinity 2.0 Jelajah Nusantara Backend

Dependency Requirement:

-   Python 3 (Currently using: 3.11)
-   pip 22 (Currently using: 22)
-   XAMPP (Currenyly using : 3.3.0)

---

## Steps/Commands

> Note: Python virtual env docs can be found
> [here](https://docs.python.org/3/tutorial/venv.html).

1. Open a terminal and use the following command to create a virtual
   environment.

```
python -m venv venv
```

Now activate the virtual environment with the following command.

```
# windows machine (command prompt)
venv\Scripts\activate.bat

# mac/linux
source venv/bin/activate
```

You will know your virtual environment is active when your terminal displays the
following:

```
(venv) path\to\project\jelajah-nusantara-backend>
```

2. The project will rely on a whole bunch of 3rd party packages (requirements)
   to function. Install the project requirements. Add the following code to you
   terminal.

```
pip install -r requirements.txt
```

3. Create a env file to store information that is specific to our working
   environment. Use the following command in your terminal.

```
# windows machine
copy .env.example .env

#mac/linux cp
.env.example .env
```

4. Run the following command to make and apply the migrations to the database
    > Note: I'm using mysql database, you should input your datbase name,
    > database credentials, database host, and database port into your .env file

```
python manage.py makemigrations
python manage.py migrate
```

5. To run the server, run the following command
    > Note: The server will run through default port which is 8000, you can add
    > the last argument to specify the port

```
python manage.py runserver
```

---
