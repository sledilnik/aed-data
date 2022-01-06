#!/usr/bin/env python
import time
from datetime import date
# from numpy import int64, inf, nan
# from pandas.core.indexes.base import Index 
import requests
# import pandas as pd

def saveurl(url, filename, expectedContentType):
    print("Downloading ", url)
    r = requests.get(url, allow_redirects=True)
    r.raise_for_status()

    actualContentType = r.headers['Content-Type']

    if actualContentType == expectedContentType:
        open(filename, 'wb').write(r.content)
        print("Saved", filename)
    else:
        raise Exception("Unexpected content-type:", actualContentType)

def import_openstreetmap():
    # https://overpass-turbo.eu/s/1eNQ
    print('TODO: scrape overpass')


def import_opsi():
    # https://podatki.gov.si/data/search?s=defibrilatorjev

    # https://podatki.gov.si/dataset/lokacije-defibrilatorjev-aed
    saveurl("https://podatki.gov.si/dataset/5abdc896-d7b3-43a1-b580-ab2e6cff981c/resource/945e24c6-4808-4ee7-a86c-ff56a703fc6a/download/lokacijeaedvobinibreice.csv", "sources/podatki.gov.si/brezice.csv", "text/csv")

    # https://podatki.gov.si/dataset/evidenca-defibrilatorjev-v-obcini-braslovce
    saveurl("https://podatki.gov.si/dataset/789a9868-a24c-4fce-9275-28d2a7b4415f/resource/e90a1326-a98f-4169-9665-e6abab99cf25/download/evidencadefibrilatorjevobinibraslove.xlsx", "sources/podatki.gov.si/braslovce.xlsx", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

    # TODO: add others



if __name__ == "__main__":
    update_time = int(time.time())
    
    import_openstreetmap()
    import_opsi()
