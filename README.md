# AED (Automatic External Defibrilator) Data Collection - Sledilnik.org

[![Update](https://github.com/sledilnik/aed-data/actions/workflows/update.yml/badge.svg)](https://github.com/sledilnik/aed-data/actions/workflows/update.yml)

## Sources

| Status             | Source                                                              | License                                         | Credit                      | Local data                                                               | Links                                                                                                                                                              |
|--------------------|---------------------------------------------------------------------|-------------------------------------------------|-----------------------------|--------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| :white_check_mark: | [OpenStreetMap](https://openstreetmap.org)                          | [ODbL](https://www.openstreetmap.org/copyright) | ©OpenStreetMap contributors | [openstreetmap.org/slovenia.csv](sources/openstreetmap.org/slovenia.csv) | [`emergency=defibrillator`](https://wiki.openstreetmap.org/wiki/Tag:emergency%3Ddefibrillator), [Overpass API](https://overpass-turbo.eu/s/1eNQ)                   |
| :x:                | [Dispečerska služba zdravstva](https://www.dsz.si/index.php/sl/aed) | ?                                               |                             |                                                                          |                                                                                                                                                                    |
| :x:                | [AED baza Slovenije](https://aed-baza.si/)                          | ?                                               |                             |                                                                          |                                                                                                                                                                    |
| :x:                | [Portal OPSI (Odprti Podatki Slovenije)](https://podatki.gov.si)    | various                                         | Various municipalities      | [podatki.gov.si](sources/podatki.gov.si/)                                | [API](https://podatki.gov.si/api/view/store/apis/info?name=OPSI_osnovni&version=2.2.3&provider=admin), [search](https://podatki.gov.si/data/search?s=defibrilator) |

## How to run scripts

___
In this folder run:

1. `python3.8 -m venv venv` or `virtualenv -p python3.8 venv`
2. `source venv/bin/activate`
3. `pip install -r requirements.txt`
4. `python update.py`

## Updating data

GitHub:octocat: workflows are scheduled to be ran periodically and can also be triggered manually on the [Actions](https://github.com/sledilnik/aed-data/actions) page.
