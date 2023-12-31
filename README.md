# de_scripts_template

## Description

This repository contains a template for a data engineering project. It is intended to be used as a starting point for new projects. It contains a basic project structure of the python scripts.

## Structure

The project structure is as follows:

```
.
├── de_scripts_template
│   ├── data
│   │   └──  example.csv
│   ├── logs
│   │   └──  example.log
│   ├── scripts
│   │   ├── __init__.py
│   │   ├── main.py
│   │   └──  utils
│   │      ├── __init__.py
│   │      ├── credentials_utilities.py
│   │      ├── crud_utilities.py
│   │      ├── extraction_utilities.py
│   │      ├── file_utilities.py
│   │      ├── load_utilities.py
│   │      ├── log_utilities.py
│   │      ├── schemas.py
│   │      └── transform_utilities.py
│   ├── tests
│   ├── README.md
│   └── requirements.txt
```

### About the structure

- The `data` folder is intended to contain the data that is used in the project.
- The `logs` folder is intended to contain the log files that are generated by the scripts.
- The `scripts` folder is intended to contain the python scripts.
- The `tests` folder is intended to contain the tests for the scripts.
- The `README.md` file is intended to contain the description of the project.
- The `requirements.txt` file is intended to contain the dependencies of the project.

Regarding the `scripts` folder.

- The `__init__.py` file is intended to make the folder a python module.
- The `main.py` file is intended to be the main script of the project.
- The `utils` folder is intended to contain the utility scripts.
- The `utils/__init__.py` file is intended to make the folder a python module.
- The `utils/credentials_utilities.py` file is intended to contain the functions that are used to get the credentials.
- The `utils/crud_utilities.py` file is intended to contain the functions that are used to perform CRUD operations in databases.
- The `utils/extraction_utilities.py` file is intended to contain the functions that are used to extract data.
- The `utils/file_utilities.py` file is intended to contain the functions that are used to handle files.
- The `utils/load_utilities.py` file is intended to contain the functions that are used to load data.
- The `utils/log_utilities.py` file is intended to contain the functions that are used to handle logs.
- The `utils/schemas.py` file is intended to contain the schemas of the data and some operations to force the type of the data.
- The `utils/transform_utilities.py` file is intended to contain the functions that are used to transform data.

## How to use it

0. Star this repository. :star:
1. Clone the repository.
2. Rename the folder `de_scripts_template` to the name of the project.
3. Fill the files in the `data` folder with the data that is needed for the project.
4. Fill the files in the `scripts/utils` folder with the functions that are needed for the project.
5. Fill the file `scripts/main.py` with the code that is needed for the project.
6. Fill the file `README.md` with the description of the project.
7. Fill the file `requirements.txt` with the dependencies of the project.
8. Run the script `scripts/main.py` to test the project.

## To be done in the future

- Add a `Makefile` to automate the execution of the scripts.
- Add a `Dockerfile` to containerize the project.
- Add tests for the scripts.
- Create a CI/CD pipeline for the project.

## Author

- [Balthazar Paixão](https://www.linkedin.com/in/balthapaixao/)

Check out my other projects on [GitHub](https://github.com/balthapaixao/)
