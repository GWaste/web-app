# HiWaste Web App

## Introduction

This web app written using Django framework, where... hmm... I'm just started learning it last week 😅. I think there's some broken English here, if you can fix it, just create a PR and we will review it together.

## venv (Virtual Environment) Initialization

I recommend to use `venv` for this project. To initialize the venv, you can use command below.

```
python -m venv [venv folder]
```

You can choose anywhere for this folder. After you create a venv folder, then you can activate by using command below.

```
[venv folder]/Scripts/activate
```

You can verify how it's works by installing all project requirements, and then show where all of them installed. You can use commands below, and after that, Django should be installed on your venv folder, not system-wide.

```
pip install -r requirements.txt
pip show Django
```

## Configs

Because we decided to not use the database for now, the app needs to load json files at initialization. Please put the `category.json`, `product.json`, and `ukm.json` file in the `config` folder before running the project.

## Running the project

To launch the web app, use the command below in the project folder

```
python manage.py runserver
```

## VSCode

I highly recommend using VSCode for this project. I have commited some config files like `.vscode/launch.json`, where you can just launch and debug the app by just pressing `F5`.

Of course, you need to install some extensions to make jobs easier. You can take a look a file named `.vscode/extensions.json`.