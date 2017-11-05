# Closest Bars

This simple console utility finds the biggest, the smallest, and the closest bars from a given text file in JSON format.

# Quickstart

The script requires Python 3.5 or later version installed

Example of script launch on Linux, Python 3.5:

```bash

$ python bars.py <path to file> # possibly requires call of python3 executive instead of just python

```

## Input Example: File

```bash

{
  "features": [{
    "geometry": {
      "coordinates": [37.621587946152012, 55.765366956608361],
      "type": "Point"
    },
    "properties": {
      "DatasetId": 1796,
      "VersionNumber": 2,
      "ReleaseNumber": 2,
      "RowId": "20a0b7c9-dad3-4af8-a2a2-08170f74379b",
      "Attributes": {
        "global_id": 20660594,
        "Name": "Юнион Джек",
        "IsNetObject": "нет",
        "OperatingCompany": null,
        "AdmArea": "Центральный административный округ",
        "District": "Мещанский район",
        "Address": "Нижний Кисельный переулок, дом 3, строение 1",
        "PublicPhone": [{
          "PublicPhone": "(495) 621-19-63"
        }],
        "SeatsCount": 30,
        "SocialPrivileges": "нет"
      }
    },
    "type": "Feature"
  }],
  "type": "FeatureCollection"
}

```
 
 
## Intput Example: Keyboard

    Latitude, Longitude: 55.836160, 37.322046

## Output Example

    The biggest bar is Спорт бар «Красная машина» at Автозаводская улица, дом 23, строение 1 with 450 places
    The smallest bar is БАР. СОКИ at Дубравная улица, дом 34/29 with 0 places
    The closest bar is БАР. СОКИ at Дубравная улица, дом 34/29 with 0 places


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
