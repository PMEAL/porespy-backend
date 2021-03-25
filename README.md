## PoreSpy Backend

Backend written in Django/Python for PoreSpy.

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

When you pull the code from the repo, run `python manage.py runserver` to start the REST API. You can view the back-end at `http://localhost:3000/`.

## Contact:

Jeff Gostick (jgostick@uwaterloo.ca)
