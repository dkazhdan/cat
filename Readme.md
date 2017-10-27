# Pythian - DevOps Technical Project



## Getting Started

These instructions will get you a copy of the project up and running on your local machine .

## Stack Components

The stack consists of a python flask web application and mongodb as the backend

### Prerequisites

You need docker and docker-compose version >1.12 installed on your system

### Installing

All it takes to run the example is to check out the repo and run  start_cat.sh API_KEY where API_KEY is the key you recieve from http://thecatapi.com/docs.html

This is how you start the docker stack 9assuming your api_key is AIIYR)

```
bash start_cat.sh AIIYR
```


## Running the tests

On your local machine run 

```
curl localhost:8888/cat and curl localhost:8888/history
```
