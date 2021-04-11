# generators.py contains django models that are concerned with the business logic of the porespy.generators modules

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


# Model that uses the Blobs method porespy.generators, and returns the image in the generated_image property.
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

        # generate blob, save into bytes, and send back the base64 string and numpy array to the front end.
        im = ps.generators.blobs(shape=shape_array, porosity=float_porosity, blobiness=int_blobiness).tolist()
        im_data = np.array(im)
        buff = BytesIO()
        plt.imshow(np.atleast_3d(im)[:, :, 0], interpolation="none", origin="lower")
        plt.savefig(buff, format='png', transparent=True)
        new_im_string = base64.b64encode(buff.getvalue()).decode("utf-8")
        # im_object_return contains the numpy array and base64 representations of the generated image.
        im_object_return = {
            'np_array': im_data,
            'base_64': new_im_string
        }

        plt.close()
        return im_object_return


# Model that uses the BundleOfTubes method porespy.generators, and returns the image in the generated_image property.
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

        # generate bundle_of_tubes, save into bytes, and send back the base64 string and numpy array to the front end.
        im = ps.generators.bundle_of_tubes(shape=shape_array, spacing=float_spacing).tolist()
        # convert array of numbers into array of booleans so it can be filtered/passed around.
        im_data = np.array([[False if x == [0.0] else True for x in s] for s in im])
        buff = BytesIO()
        plt.imshow(np.atleast_3d(im)[:, :, 0], interpolation="none", origin="lower")
        plt.savefig(buff, format='png', transparent=True)
        new_im_string = base64.b64encode(buff.getvalue()).decode("utf-8")
        # im_object_return contains the numpy array and base64 representations of the generated image.
        im_object_return = {
            'np_array': im_data,
            'base_64': new_im_string
        }

        plt.close()
        return im_object_return


# Model that uses the BundleOfTubes method porespy.generators, and returns the image in the generated_image property.
class LatticeSpheres(models.Model):

    # TODO: when newest version of porespy is released, uncomment spacing and smooth properties
    # TODO: and in the function call in generated_image

    dimension_x = models.IntegerField(null=True, blank=True, default=500)
    dimension_y = models.IntegerField(null=True, blank=True, default=500)
    dimension_z = models.IntegerField(null=True, blank=True, default=0)
    radius = models.IntegerField(null=True, blank=True, default=0)
    # spacing = models.IntegerField(null=True, blank=True, default=0)
    offset = models.IntegerField(null=True, blank=True, default=0)
    # smooth = models.TextField(default="True")
    lattice = models.TextField(default="sc")

    @property
    def generated_image(self):
        plt.close()
        int_dimension_x = int(self.dimension_x)
        int_dimension_y = int(self.dimension_y)
        int_dimension_z = int(self.dimension_z)
        int_radius = int(self.radius)
        # int_spacing = int(self.spacing)
        int_offset = int(self.offset)
        # str_smooth = str(self.smooth)
        str_lattice = str(self.lattice)

        if int_dimension_z == 0:
            shape_array = [int_dimension_x, int_dimension_y]
        else:
            shape_array = [int_dimension_x, int_dimension_y, int_dimension_z]

        im = ps.generators.lattice_spheres(
            shape=shape_array,
            # spacing=int_spacing
            radius=int_radius,
            offset=int_offset,
            # smooth=str_smooth
            lattice=str_lattice
        )

        im_data = np.array(im)
        buff = BytesIO()
        plt.imshow(np.atleast_3d(im)[:, :, 0], interpolation="none", origin="lower")
        plt.savefig(buff, format='png', transparent=True)
        new_im_string = base64.b64encode(buff.getvalue()).decode("utf-8")
        # im_object_return contains the numpy array and base64 representations of the generated image.
        im_object_return = {
            'np_array': im_data,
            'base_64': new_im_string
        }

        plt.close()
        return im_object_return
