## PoreSpy Backend

This repo contains the back end of PoreSpy, the web app of a python library of image analysis tools used to extract
information from 3D images of porous materials. The back end is written in Django/Python, and is a REST API. 
This backend was written in Python 3.7.4.

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

|Python Package                 |Command to install                 |Version (as of April 2nd, 2021)    |
|-------------------------------|-----------------------------------|-----------------------------------|
|Porespy                        |`pip install porespy`              |1.3.1                              |
|Django                         |`pip install django`               |3.1.3                              |
|Django REST Framework          |`pip install djangorestframework`  |3.12.2                             |
|Django CORS Headers            |`pip install django-cors-headers`  |3.7.0                              |
|Numpy                          |`pip install numpy`                |1.18.1                             |
|Pandas                         |`pip install pandas`               |1.2.3                              |
|Matplotlib                     |`pip install matplotlib`           |3.3.3                              |

Run `python manage.py runserver` to start the REST API. You can view the back-end at `http://localhost:8000/`.
If there are error messages in the terminal, make sure to resolve these first as the REST API will not run until
these errors have been resolved.


## Contact:

Jeff Gostick (jgostick@uwaterloo.ca)
