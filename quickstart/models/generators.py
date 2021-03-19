# generators.py is concerned with the business logic of the generators modules
# e.g. The GeneratorBlobs handles the business logic of generating a blob,
# and returns the image in a base64 string to the front end.

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
class Blobs(models.Model):
    porosity = models.FloatField(null=True, blank=True, default=0.6)
    blobiness = models.IntegerField(null=True, blank=True, default=2)
    dimension_x = models.IntegerField(null=True, blank=True, default=500)
    dimension_y = models.IntegerField(null=True, blank=True, default=500)
    dimension_z = models.IntegerField(null=True, blank=True, default=0)

    @property
    def generated_image(self):
        plt.close()
        int_dimension_x = int(self.dimension_x)
        int_dimension_y = int(self.dimension_y)
        int_dimension_z = int(self.dimension_z)
        float_porosity = float(self.porosity)
        int_blobiness = int(self.blobiness)

        if int_dimension_z == 0:
            shape_array = [int_dimension_x, int_dimension_y]
        else:
            shape_array = [int_dimension_x, int_dimension_y, int_dimension_z]

        # Generator blob form PoreSpy, convert to numpy array, and make it RGB.
        im = ps.generators.blobs(shape=shape_array, porosity=float_porosity, blobiness=int_blobiness).tolist()
        im_data = np.array(im)
        buff = BytesIO()
        plt.imshow(np.atleast_3d(im)[:, :, 0], interpolation="none", origin="lower")
        plt.savefig(buff, format='png')
        new_im_string = base64.b64encode(buff.getvalue()).decode("utf-8")
        im_object_return = {
            'np_array': im_data,
            'base_64': new_im_string
        }

        plt.close()
        return im_object_return


# Model that uses the BundleOfTubes method in the Generators from PoreSpy
class BundleOfTubes(models.Model):
    dimension_x = models.IntegerField(null=True, blank=True, default=500)
    dimension_y = models.IntegerField(null=True, blank=True, default=500)
    dimension_z = models.IntegerField(null=True, blank=True, default=0)
    spacing = models.FloatField(null=True, blank=True, default=30)

    @property
    def generated_image(self):
        plt.close()
        int_dimension_x = int(self.dimension_x)
        int_dimension_y = int(self.dimension_y)
        int_dimension_z = int(self.dimension_z)
        float_spacing = float(self.spacing)

        if int_dimension_z == 0:
            shape_array = [int_dimension_x, int_dimension_y]
        else:
            shape_array = [int_dimension_x, int_dimension_y, int_dimension_z]

        im = ps.generators.bundle_of_tubes(shape=shape_array, spacing=float_spacing).tolist()
        im_data = np.array([[False if x == [0.0] else True for x in s] for s in im])
        buff = BytesIO()
        plt.imshow(np.atleast_3d(im)[:, :, 0], interpolation="none", origin="lower")
        plt.savefig(buff, format='png')
        new_im_string = base64.b64encode(buff.getvalue()).decode("utf-8")
        im_object_return = {
            'np_array': im_data,
            'base_64': new_im_string
        }

        plt.close()
        return im_object_return
