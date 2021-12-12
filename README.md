# Python Service

## Intro
First flask server.

## Setup
- Install pre-requisites

`sudo apt install python3 python3-pip python3-venv`

- Enable Python virtual environment

```
python3 -m venv venv
. venv/bin/activate
```

- Install the Flask library

`pip install Flask`

## Usage
Run the server

`flask run`

- Multiply by ten service

http://127.0.0.1:5000/timesten/{any_number}

- Nice greeting for a bad day

http://127.0.0.1:5000/hello/{any_name} 
