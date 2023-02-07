Author: Renel Jean-Baptiste
Description:
    python-app.yml src= "https://github.com/actions/starter-workflows/blob/main/ci/python-app.yml"

    create a secrets.py file and create the variables subdomain= "form-username", format= "json" identifier="cubes-project-proposal-submission" api_key = "your form api key"

    your url should look like this in apiData.py
    url = "https://{subdomain}.wufoo.com/api/v3/forms.{format}"
Installs :

    for "import requests"
      type into termnial in the project folder scope  - "python.exe -m pip install requests
"

    for "import mysql.connector"
        type into termnial in the project folder scope or python local   - python -m pip install mysql-connector-python

