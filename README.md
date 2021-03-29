## PoreSpy Backend

This repo contains the back end of PoreSpy, the web app of a python library of image analysis tools used to extract
information from 3D images of porous materials. The back end is written in Django/Python, and is a REST API.

## TODO:

- Research how to section off models/serializers in django/python so they are not all concentrated in one file (Separation of Concerns).
- Continue writing out PoreSpy's modules:
    - generators (Currently Blobs and BundleOfTubes are completed, but will continue with the remaining modules)
    - filters (Currently LocalThickness is completed, but will continue with the remaining modules)
    - metrics (Currently PoreSizeDistribution is completed, but will continue with the remaining modules)
    - simulations
    - networks
    - visualization
    - io
    - tools

## Instructions

When you pull the code from the repo, make sure to have the following libraries installed:

|Python Package                 |Command                            |
|-------------------------------|-----------------------------------|
|Django                         |`pip install Django`               |
|Django REST Framework          |`pip install djangorestframework`  |
|Django CORS Headers            |`pip install django-cors-headers`  |

Run `python manage.py runserver` to start the REST API. You can view the back-end at `http://localhost:8000/`.
If there are error messages in the terminal, make sure to resolve these first as the REST API will not run until
these errors have been resolved.


## Contact:

Jeff Gostick (jgostick@uwaterloo.ca)
