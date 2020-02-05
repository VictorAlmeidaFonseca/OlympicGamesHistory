## Olympic Games API

**This is a API for historical dataset on the modern Olympic Games**

### Installation

You can get this project following the steps below:

...

https://github.com/VictorAlmeidaFonseca/OlympicGamesHistory.git
cd estoque
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
pyhton manage.py migrate

...

### Next Steps

After does the steps above, you can run "pyhton manage.py runserver" and put in your browser this url: **http://127.0.0.1:8000/**.
The address takes you to the API endpoint. That showing the url's path. This router is use DefaultRoutet method from Django Rest Framwork as you can see in the picture below:

 ![](https://user-images.githubusercontent.com/36797751/73865793-95f26480-4822-11ea-978d-6c13019684e3.png)

### Populate DataBase

If you want to automatically load initial data for an app you would run **python manager.py populate_base** This command can be modified on the source **olympic_api/management/commands/populate_base.py**
The source file there is in **OlympicGamesHistory/script**.

