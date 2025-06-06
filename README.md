# About

This proyect is a basic structure for a Python / Flask application

# Requirements

You need Docker Desktop installed on your computer.

# Install

Clone this repository:

```bash
git clone git@github.com:falces/flaskTemplate.git
```

## Configure Docker

1. Inside /docker folder, copy the file .env.template with the name .env
2. Open it and edit the information with your desired data

## Run the app

Go to the foler where the repository has been cloned in and run:

```bash
docker compose -f docker/compose.yaml up -d
```

The application comes with a basic endpoint to test. Open your web browser and navigate to:

```
http://localhost:8001/v1/users/user/1?name=JohnDoe
```

In the Users class you have examples about how to manage the query string and URL parameters.