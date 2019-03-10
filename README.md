<a id="top"></a>
# DIAGNOSIS CODES API
**Author**: Hisham Iddris

**Version**: 1.0
___

<a id="overview"></a>
## Overview

A Django Rest Framework API that allows you to utilize an internationally recognized set of diagnosis codes. This includes the ability to create a new diagnosis record, edit an existing diagnosis code record, list diagnosis codes in batches of 20, retrieve diagnosis code by ID and delete a diagnosis code. The API currently supports ICD-9 and ICD-10 diagnosis code types only. The API uses a PostgresSQL database for data persistence. For ease in deployment, a docker compose file is provided to spin up an instance in a docker container.
___

## Table of contents
* [Overview](#overview)
* [Setting Up](#setup)
* [API Endpoints](#api)
* [References](#references)
* [Todo](#todo)
___
<a id="setup"></a>
## Setting Up
In a terminal instance:

1. ```git clone https://github.com/vhish/mpharma.git``` (Clone the repo)
2. ```docker-compose run web python /mpharma/manage.py migrate --noinput``` (Run migragtions in the docker instance.)
3. ```docker-compose run web python /mpharma/manage.py load_data``` (Seed the PostgreSQL database with csv files in the docker instance.)
4. ```docker-compose up``` (Run the docker container)

___
<a id="api"></a>
## API Endpoints
All API endpoints can be acessed via the API swagger link upon running the docker container. i.e. http://localhost:8000/docs
___
<a id="todo"><a>
## TODO: 
  
Adding authorisation to the api.

___
<a id="references"></a>
## References
https://github.com/kamillamagna/ICD-10-CSV https://en.wikipedia.org/wiki/ICD-10 https://en.wikipedia.org/wiki/International_Statistical_Classification_of_Diseases_and_Related_Health_Problems
http://www.wvupc.org/compliance/PDF/training/Intro_to_ICD-9.pdf

[Back to top](#top)
