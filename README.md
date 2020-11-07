# Origin Markets Backend Test

### Overview

This project contains the application used for ingesting data 
representing bonds and making the information queryable through an API.

Additional information for items being created comes from a call to the 
[GLEIF API](https://www.gleif.org/en/lei-data/gleif-lei-look-up-api/access-the-api) 
which is used to find the corresponding `Legal Name` of the entity which issued the bond.


## Setup

1. Ensure the prerequisites are installed
    ```
    - Python3.8 (as testes)
    - pip (tool for installing Python packages)
        - curl https://bootstrap.pypa.io/get-pip.py | python3.8
    ```

2. Create virtual env for python3 inside project directory:
    ```
    python3 -m venv venv 
    ```

3. Activate newly created environment
    ```
    . venv/bin/activate (Linux/OSX)
    venv\Scripts\activate.bat (Windows)
    ```

4. Install the required python packages
    ```
    pip install -r requirements.txt
    ```

5. Change into the project directory
    ```
    cd origin
    ```

6. Setup the database
    ```
   ./manage.py migrate
    ```

7. Create an initial user
    ```
   ./manage.py createsuperuser
    ```
   
 ## Run Project

Once the packages have been installed the project can be run by issuing the following command:
 ```
 ./manage.py runserver
 ```

### API Usage

#### Obtaining an authentication token

User authentication is performed using JSOM JWT web tokens.

1. Obtain the access token
    ```
    POST http://localhost:8000/api/token/
        Request body parameters
        {
            "username": username,
            "password": password
        }
    ```
2. Include the access token in the request
    ```
    Copy the result from the 'access' field
    Add Authentication header in the format 'Token {access_token}'
    ```

#### Endpoints

There are two endpoints in this project
* GET /bonds?legal_name={LEGAL_NAME}
    * LEGAL_NAME - filters by specified legal name
* POST /bonds/
    * Request body parameters:
         ```
        {
            "isin": "FR0000131104",
            "size": 100000000,
            "currency": "EUR",
            "maturity": "2025-02-28",
            "lei": "R0MUWSFPU8MPRO8K5P83"
        }
        ```

 ## Unit Tests

Tests can be invoked using the command:
 ```
 ./manage.py test
 ```

NOTES:
* In addition to running the tests code coverage reports are being generated:
    * These can be found in the **cover** directory
    * Comment the line ```'--with-coverage',``` in the setting.py file to turn off coverage generation