#!/usr/bin/env python

import time
import requests
import os

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


overpass_api_url = "https://lz4.overpass-api.de/api/interpreter"
overpass_query_aed_json = """
[out:json]
[timeout:300];
area(id:3600218657)->.slovenia;
(
    nwr[emergency=defibrillator](area.slovenia);
);
out center body qt;
"""

#https://overpass-turbo.eu/s/1eNQ
overpass_query_aed_csv = """
[out:csv(
     ::"id", ::type, ::lat, ::lon, name,
     phone, "emergency:phone", image, website, description, operator, 
     opening_hours, indoor, access, wheelchair,
     "defibrillator:location", "defibrillator:location:en", "defibrillator:location:sl", "defibrillator:location:it", "defibrillator:location:hu", "defibrillator:location:de";
     true; ","
   )]
[timeout:300];
area(id:3600218657)->.slovenia;
(
    nwr[emergency=defibrillator](area.slovenia);
);
out center body qt;
"""

def saveFromOverpassAPI(
    query: str,
    filename: str, 
    expectedContentType: str,
    api_url: str = overpass_api_url,
):
    print(f"Requesting data from Overpass API. [url={api_url}]")
    response = requests.post(url=api_url, data={"data": query})
    response.raise_for_status()
    print("Downloaded data from Overpass API.")

    actualContentType = response.headers['Content-Type']
    if actualContentType == expectedContentType:
        if filename != None:
            open(filename, 'wb').write(response.content)
            print("Saved", filename)
    else:
        raise Exception("Unexpected content-type:", actualContentType)


def import_openstreetmap():
    if not os.path.exists("sources/openstreetmap.org"):
        os.makedirs("sources/openstreetmap.org")

    # saveFromOverpassAPI(overpass_query_aed_json, "sources/openstreetmap.org/openstreetmap.json", "application/json")
    saveFromOverpassAPI(overpass_query_aed_csv, "sources/openstreetmap.org/slovenia.csv", "text/csv")


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
