from django.db import models
import base64
from io import BytesIO
import numpy as np
import porespy as ps
import matplotlib
# Agg Buffer Description:
# https://matplotlib.org/3.1.3/gallery/misc/agg_buffer.html
# Agg Buffer is used to access the figure canvas as an RGBA buffer, convert it to an array,
# and pass it to Pillow for rendering
matplotlib.use('Agg')
from matplotlib import pyplot as plt


# Model that uses the Blobs method in the Generators from PoreSpy
class PoreSizeDistribution(models.Model):
    psd_im = models.TextField(default="")

    @property
    def psd_im_metric(self):
        return "testingPSD?.."