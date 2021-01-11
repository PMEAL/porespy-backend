from django.db import models
from django.contrib import admin
import base64
import porespy as ps
from io import BytesIO
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# IMPORTANT: Run these 3 commands when creating a new model
# python manage.py migrate
#
# python manage.py makemigrations
#
# python manage.py migrate


class GeneratorBlobs(models.Model):
    porosity = models.FloatField(null=True, blank=True, default=0.6)
    blobiness = models.IntegerField(null=True, blank=True, default=2)
    dimension_x = models.IntegerField(null=True, blank=True, default=500)
    dimension_y = models.IntegerField(null=True, blank=True, default=500)

    @property
    def generated_image(self):
        int_dimension_x = int(self.dimension_x)
        int_dimension_y = int(self.dimension_y)
        float_porosity = float(self.porosity)
        int_blobiness = int(self.blobiness)
        shape_array = [int_dimension_x, int_dimension_y]

        # Generator blob form PoreSpy, convert to numpy array, and make it RGB.
        im = ps.generators.blobs(shape=shape_array, porosity=float_porosity, blobiness=int_blobiness).tolist()
        # plt.show(im)

        # try:
        #     lt = ps.filters.local_thickness(im)
        #     return lt
        # except Exception as e:
        #     return str(e)

        im_data = np.array(im)
        pil_img = Image.fromarray(im_data).convert("RGB")
        buff = BytesIO()

        # Change black pixels to purple, white pixels to yellow.
        # Porous pixels are now yellow, solid pixels are now purple.
        for x in range(pil_img.width):
            for y in range(pil_img.height):
                black, white = (0, 0, 0), (255, 255, 255)
                yellow, purple = (255, 255, 0), (128, 0, 128)
                if pil_img.getpixel((x, y)) == black:
                    pil_img.putpixel((x, y), purple)
                else:
                    pil_img.putpixel((x, y), yellow)

        pil_img.save(buff, format="PNG")
        new_im_string = base64.b64encode(buff.getvalue()).decode("utf-8")
        return new_im_string

