# generators.py is concerned with the business logic of the generators modules
# e.g. The GeneratorBlobs handles the business logic of generating a blob,
# and returns the image in a base64 string to the front end.

from django.db import models
import base64
from io import BytesIO
from PIL import Image
import numpy as np
import porespy as ps


# Model that uses the Blobs method in the Generators from PoreSpy
class Blobs(models.Model):
    porosity = models.FloatField(null=True, blank=True, default=0.6)
    blobiness = models.IntegerField(null=True, blank=True, default=2)
    dimension_x = models.IntegerField(null=True, blank=True, default=500)
    dimension_y = models.IntegerField(null=True, blank=True, default=500)
    dimension_z = models.IntegerField(null=True, blank=True, default=0)






    ### TODO: generated_image should return the base64 string and the numpy array.







    @property
    def generated_image(self):
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
        # return im

        #TODO: abstract this transition of black/white to yellow/purple to apply DRY
        black, white = (0, 0, 0), (255, 255, 255)
        yellow, purple = (255, 255, 0), (128, 0, 128)

        if int_dimension_z == 0:
            im_data = np.array(im)
            pil_img = Image.fromarray(im_data).convert("RGB")
            buff = BytesIO()

            for x in range(pil_img.width):
                for y in range(pil_img.height):
                    if pil_img.getpixel((x, y)) == black:
                        pil_img.putpixel((x, y), purple)
                    else:
                        pil_img.putpixel((x, y), yellow)

            pil_img.save(buff, format="PNG")
            new_im_string = base64.b64encode(buff.getvalue()).decode("utf-8")
            im_object_return = {
                'np_array': im_data,
                'base_64': new_im_string
            }

            return im_object_return
            # return new_im_string
        else:
            #TODO: how to render 3D images if requested

            im_data = np.array(im)
            pil_img = Image.fromarray(im_data.astype(np.uint8)).convert("RGB")
            buff = BytesIO()

            # for x in range(pil_img.width):
            #     for y in range(pil_img.height):
            #         for z in range(pil_img.
            #         if pil_img.getpixel((x, y)) == black:
            #             pil_img.putpixel((x, y), purple)
            #         else:
            #             pil_img.putpixel((x, y), yellow)

            pil_img.save(buff, format="PNG")
            new_im_string = base64.b64encode(buff.getvalue()).decode("utf-8")
            im_object_return = {
                'np_array': im_data,
                'base_64': new_im_string
            }

            return im_object_return


class BundleOfTubes(models.Model):
    dimension_x = models.IntegerField(null=True, blank=True, default=500)
    dimension_y = models.IntegerField(null=True, blank=True, default=500)
    dimension_z = models.IntegerField(null=True, blank=True, default=0)
    spacing = models.FloatField(null=True, blank=True, default=30)

    @property
    def generated_image(self):
        int_dimension_x = int(self.dimension_x)
        int_dimension_y = int(self.dimension_y)
        int_dimension_z = int(self.dimension_z)
        float_spacing = float(self.spacing)

        if int_dimension_z == 0:
            shape_array = [int_dimension_x, int_dimension_y]
        else:
            shape_array = [int_dimension_x, int_dimension_y, int_dimension_z]

        im = ps.generators.bundle_of_tubes(shape=shape_array, spacing=float_spacing).tolist()
        black, white = (0, 0, 0), (255, 255, 255)
        yellow, purple = (255, 255, 0), (128, 0, 128)

        if int_dimension_z == 0:
            im_data = np.array([[False if x == [0.0] else True for x in s] for s in im])
            pil_img = Image.fromarray(im_data).convert("RGB")
            buff = BytesIO()

            for x in range(pil_img.width):
                for y in range(pil_img.height):
                    if pil_img.getpixel((x, y)) == black:
                        pil_img.putpixel((x, y), purple)
                    else:
                        pil_img.putpixel((x, y), yellow)

            pil_img.save(buff, format="PNG")
            new_im_string = base64.b64encode(buff.getvalue()).decode("utf-8")
            im_object_return = {
                'np_array': im_data,
                'base_64': new_im_string
            }
            return im_object_return
            # return new_im_string
