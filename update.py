#!/usr/bin/env python

import time
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import os

REQUEST_TIMEOUT = 120  # seconds

def create_session_with_retries(
    retries=3,
    backoff_factor=2,
    status_forcelist=(429, 500, 502, 503, 504),
    allowed_methods=("GET", "HEAD", "OPTIONS"),
):
    """Create a requests session with retry/backoff for transient failures."""
    session = requests.Session()
    retry_strategy = Retry(
        total=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
        allowed_methods=allowed_methods,
        raise_on_status=False,
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    return session

def saveurl(url, filename, expectedContentType):
    print("Downloading ", url)
    session = create_session_with_retries()
    r = session.get(url, allow_redirects=True, timeout=REQUEST_TIMEOUT)
    r.raise_for_status()

    actualContentType = r.headers['Content-Type']

    if actualContentType == expectedContentType:
        open(filename, 'wb').write(r.content)
        print("Saved", filename)
    else:
        raise Exception("Unexpected content-type:", actualContentType)


overpass_api_url = "https://overpass-api.de/api/interpreter"
overpass_headers = {
    "User-Agent": "aed-data-updater/1.0 (+https://github.com/sledilnik/aed-data)",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
}

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
    session = create_session_with_retries(retries=3, backoff_factor=10)
    request_headers = {
        **overpass_headers,
        "Accept": expectedContentType,
    }
    response = session.post(
        url=api_url,
        data={"data": query},
        headers=request_headers,
        timeout=REQUEST_TIMEOUT,
    )
    response.raise_for_status()
    print("Downloaded data from Overpass API.")

    actualContentType = response.headers['Content-Type'].split(';')[0].strip()
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
