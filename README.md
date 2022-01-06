# AED (Automatic External Defibrilator) Data Collection - Sledilnik.org

[![Update](https://github.com/sledilnik/aed-data/actions/workflows/update.yml/badge.svg)](https://github.com/sledilnik/aed-data/actions/workflows/update.yml)

## Sources

### OpenStreetMap

In OSM nodes are tagged with [`emergency=defibrilator`](https://wiki.openstreetmap.org/wiki/Tag:emergency%3Ddefibrillator)

Overpass query for Slovenia: https://overpass-turbo.eu/s/1eNQ

### Portal OPSI (Odprti Podatki Slovenije)

https://podatki.gov.si/data/search?s=defibrilatorjev

## How to run scripts

___
In this folder run:

1. `python3.8 -m venv venv` or `virtualenv -p python3.8 venv`
2. `source venv/bin/activate`
3. `pip install -r requirements.txt`
4. `python update.py`

## Updating data

GitHub:octocat: workflows are scheduled to be ran periodically and can also be triggered manually on the [Actions](https://github.com/sledilnik/aed-data/actions) page.
