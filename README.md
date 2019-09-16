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

## Downfalls with GMaps API

I tried to make a concept proof of `python-gmaps` package  for validate and retrive (from zip code) location coords from the GMaps API  on this project but when i try to connect google answer me with this error of account pricing

```python
Python 3.7.4 (default, Jul 16 2019, 07:12:58) 
[GCC 9.1.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from gmaps import Geocoding
>>> api = Geocoding(api_key='AIzaS******************************DvTw')
>>> api.reverse(51.232, 21.123)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/smoke/workspace/weather_mi/.env/lib/python3.7/site-packages/gmaps/geocoding.py", line 65, in reverse
    return self._make_request(self.GEOCODE_URL, parameters, "results")
  File "/home/smoke/workspace/weather_mi/.env/lib/python3.7/site-packages/gmaps/client.py", line 89, in _make_request
    )(response)
gmaps.errors.RequestDenied: {'error_message': 'You must enable Billing on the Google Cloud Project at https://console.cloud.google.com/project/_/billing/enable Learn more at https://developers.google.com/maps/gmp-get-started', 'results': [], 'status': 'REQUEST_DENIED', 'url': 'https://maps.googleapis.com/maps/api/geocode/json?latlng=51.232000%2C21.123000&sensor=false&key=AIzaS******************************DvTw'}
>>>
```

here mi wakatime metrics: https://wakatime.com/@ricardosiri68/projects/nppmuendql?start=2019-09-09&end=2019-09-15


You can email me any questions ^^
