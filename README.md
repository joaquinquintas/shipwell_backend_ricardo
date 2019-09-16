# weather m i

## Introduction 
La intencion detras de este proyecto es porder formar un hexagono lo mas prolijo posible. Con el fin de poder expandir futuros requermientos sin entorpecer lo desarrollado hasta ahora (Ver https://fideloper.com/hexagonal-architecture)

El producto final debe ser capaz de:

- Extender las opciones de  servicios de datos climaticos de manera simple. Ahora cuenta con 3 servicios pero podria tener mas.
- Poder configurar el servicio principal y la comunicacion con servicios externos.
- Y una capa de domino y de aplicacion que se encuentre los mas desacoplada de la infrastructura como sea posible. A fin ultimo de poder facilitar el intercambio de un framework web por otro.
  ej: Django -> Flask

En sintesis el objetivo detras de un hexagono es la portabilidad del codigo encargado de resolver el modelo de domino del software.

## Installation

### Requirements

needs python >= 3.7

### Step 1 Clone

clone this repo and gets inside of its root dir

```bash
git clone git@github.com:ricardosiri68/weather_mi.git && cd weather_mi
```

### Step 2 Virtualenv

create a virtual env and install dependencies

```bash
weather_mi/$ python -m venv .env && source .env/bin/activate && pip install --upgrade pip -r requirements.txt
```

### Step 3 (config)

configure the project making a copy of config.cfg.example

```bash
cp config.cfg.example config.cfg
```

add the configuration base_url for the *weather services* and *average_conviersion_unit*

```
[DEFAULT]
# posible values for average_conversion_unit
# F for fahrenheit
# C for celsius
# example: average_conversion_unit=F
average_conversion_unit=C

[accuweather-connection]
base_url=http://127.0.0.1:5000

[weatherdotcom-connection]
base_url=http://127.0.0.1:5000

[noaa-connection]
base_url=http://127.0.0.1:5000

```

## Usage

### Run tests.

The test suite is splited in two places: `django` test and and unit test with `nose`

```
nosetest -s tests && ./manage.py test
```

### Start the django web service

```bash
./manage.py runserver
```

### If you are developing

you can mock the weather services API's with this project https://github.com/otterlogic/mock-weather-api

is flask project and can be started with

```bash
FLASK_APP=app.py flask run
```

### Check the enpoint with curl


```bash
curl "http://localhost:8000/average_temperature/?latitude=33&longitude=44&services[]=accuweather&services[]=noaa&services[]=weatherdotcom"
```

The `service[]` filter can take the next values: `weatherdotcom` `accuweather` and  `noaa`

here mi wakatime metrics: https://wakatime.com/@ricardosiri68/projects/nppmuendql?start=2019-09-09&end=2019-09-15


You can email me any questions ^^
