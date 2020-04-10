Title: covid-api - a free and open source API service for COVID-19 data
Date: 2020-04-10 22:00
Author: Andrea Grandi
Category: Development
Tags: covid, api, rest, data, covid-19, service, free, open, source
Slug: covid-api-free-and-open-source-api-service-for-covid19-data
Status: published

## Introduction

In this period of COVID-19 emergency, many countries are publishing COVID related data that is being used by many existing projects and researchers.

The main problem with these data is that they are being released in CSV format on some GitHub repository. While we fully appreciate the opennes of this format, unfortunataly it can introduce an additional work to be done (downloading the data, cleaning it, importing the data into a database, keeping it updated etc...) before someone can consume and analyse the data.

## covid-api

covid-api project is a **free** and **open source** API service which automatically imports the data from various sources (at the moment we support the [John Hopkins CSSE](https://github.com/CSSEGISandData/COVID-19) data source) and makes it available as a REST API.

The service is still under development, but an initial version (with regularly updated data) is already available at [https://api.covid19data.cloud](https://api.covid19data.cloud).

## How to use the data

To consume the API you don't need an account nor you need to authenticate in any way. You just need to request the right endpoint using the supported parameters.

Here is an example for Python language:

    :::python
    In [1]: import requests

    In [2]: response = requests.get('https://api.covid19data.cloud/v1/jh/daily-reports?last_update_from=2020-04-01&last_update_to=2020-04-03&country=Italy')

    In [3]: response.json()
    Out[3]:
    [{'id': 35343,
    'country_region': 'Italy',
    'province_state': None,
    'fips': None,
    'admin2': None,
    'last_update': '2020-04-01T21:58:34',
    'confirmed': 110574,
    'deaths': 13155,
    'recovered': 16847},
    {'id': 37895,
    'country_region': 'Italy',
    'province_state': None,
    'fips': None,
    'admin2': None,
    'last_update': '2020-04-02T23:25:14',
    'confirmed': 115242,
    'deaths': 13915,
    'recovered': 18278}]

Further API documentation is available at https://api.covid19data.cloud/docs

## Next steps

While we keep polishing the code and [improving the existing data import](https://github.com/andreagrandi/covid-api/issues/43) procedure, we are planning to support additional data sources. The next one we are going to support is the [**Italian Protezione Civile**](https://github.com/andreagrandi/covid-api/issues/46).

If you are aware of an additional data source that you would like to see covered, please let us know (creating a new Issue on GitHub) or send us a pull request.

## Contribute to the project

If you are a Python developer and would like to contribute to the project, my advice is to first have a look at the main documentation available in the [README](https://github.com/andreagrandi/covid-api/blob/master/README.md).

Then I suggest to have a look at the existing [Issues](https://github.com/andreagrandi/covid-api/issues) and see where help is needed or in alternative you can open a new Issue or send a pull request with fixes and improvements.

I also recommend to become familiar with our [Code of Conduct](https://github.com/andreagrandi/covid-api/blob/master/CODE_OF_CONDUCT.md) before sending any contribution.

## Sponsors and Thanks

I want to thank [Heroku](https://www.heroku.com/) for accepting to sponsor the hosting of this service.

I also want to thank all the [volunteers](https://github.com/andreagrandi/covid-api/graphs/contributors) involved in the project for their help and contributions.

## Disclaimer

We are doing our best to keep the available data updated, clean (removing duplicates), and to provide a reliable service, 
but we are not in any way responsible for the accuracy of the data nor for the availability of the service itself. 
Please **use it at your own risk**.

**Abuse notice**: we are currently not requiring any registration or authentication to use this service because 
we would like to keep it as simple as possible. 
Please do not abuse the service or you will force us to require a registration (subject to approval) to continue using it.
