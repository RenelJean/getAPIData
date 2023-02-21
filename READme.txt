Author: Renel Jean-Baptiste
Description:
    python-app.yml src= "https://github.com/actions/starter-workflows/blob/main/ci/python-app.yml"

    create a secrets.py file and create the variables subdomain= "form-username", format= "json" identifier="cubes-project-proposal-submission" api_key = "your form api key"

    your url should look like this in apiData.py
    url = "https://{subdomain}.wufoo.com/api/v3/forms.{format}"
Installs :

    for "import requests"
      type into terminal in the project folder scope  - "python.exe -m pip install requests
"

    for "import mysql.connector"
        type into terminal in the project folder scope or python local   - python -m pip install mysql-connector-python

   for "import PySide6.QtCore"
       type into terminal in the project folder scope or python local -  pip install pyside6

    pip install PyQt5
    pip install pyqt-tools

    # if PyQt5 Designer not installed
    pip install PyQt5Designer


NEED TO FIX DB MYSQL error and parse data from output.txt into correct key value labels currently the project adds data from
output.txt and stores in ito a list to be parsed. I'm going to parse the list so if any item at entries[i][1] that isn' data
get ignored and actually data gets linked to a dic having correct keys. As for the DB i'm going to do more research later today
in setting up db and tables