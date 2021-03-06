from django.db import models
import base64
from io import BytesIO
from PIL import Image
import numpy as np
import porespy as ps


class LocalThickness(models.Model):
    generator_image = models.TextField(default="")

    @property
    def generator_image_filtered(self):
        image_decoded = base64.encode(self.generator_image)
        image_bytes_io = BytesIO(image_decoded)
        image_as_im = np.array(Image.open(image_bytes_io))
        lt = ps.filters.local_thickness(image_as_im)

        # lt_data = np.array(lt)
        # pil_img = Image.fromarray(lt_data).convert("RGB")
        # buff = BytesIO()
        # pil_img.save(buff, format="PNG")
        # new_lt_string = base64.b64encode(buff.getvalue()).decode("utf-8")
        # return new_lt_string





        # int_dimension_x = int(self.dimension_x)
        # int_dimension_y = int(self.dimension_y)
        # int_dimension_z = int(self.dimension_z)
        # float_spacing = float(self.spacing)
        #
        # if int_dimension_z == 0:
        #     shape_array = [int_dimension_x, int_dimension_y]
        # else:
        #     shape_array = [int_dimension_x, int_dimension_y, int_dimension_z]
        #
        # im = ps.generators.bundle_of_tubes(shape=shape_array, spacing=float_spacing).tolist()
        # black, white = (0, 0, 0), (255, 255, 255)
        # yellow, purple = (255, 255, 0), (128, 0, 128)
        #
        # if int_dimension_z == 0:
        #     im_data = np.array([[False if x == [0.0] else True for x in s] for s in im])
        #     pil_img = Image.fromarray(im_data).convert("RGB")
        #     buff = BytesIO()
        #
        #     for x in range(pil_img.width):
        #         for y in range(pil_img.height):
        #             if pil_img.getpixel((x, y)) == black:
        #                 pil_img.putpixel((x, y), purple)
        #             else:
        #                 pil_img.putpixel((x, y), yellow)
        #
        #     pil_img.save(buff, format="PNG")
        #     new_im_string = base64.b64encode(buff.getvalue()).decode("utf-8")
        #     return new_im_string