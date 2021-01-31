from django.db import models
from django.contrib import admin
import base64
import porespy as ps
from io import BytesIO
from PIL import Image
import numpy as np

import inspect
import porespy as ps
import json

import matplotlib.pyplot as plt

# IMPORTANT: Run these 3 commands when creating a new model
# python manage.py migrate
#
# python manage.py makemigrations
#
# python manage.py migrate


# TODO: how to get details of generator functions.
class PoreSpyFuncsNames(models.Model):
    @property
    def porespy_funcs(self):
        def return_arg_names_vals_and_types(f):
            s = inspect.signature(f)
            js = {}
            for item in s.parameters.keys():
                if item == 'shape':
                    js.update({'shape[0]': {'value': 100, 'type': 'int', 'required': True},
                               'shape[1]': {'value': 100, 'type': 'int', 'required': True},
                               'shape[2]': {'value': '', 'type': 'int', 'required': False}})
                else:
                    p = s.parameters[item]
                    info = {}
                    try:
                        info['value'] = json.dumps(p.default)
                        info['required'] = True
                    except TypeError:  # Means there is no default value
                        info['value'] = ''
                        info['required'] = False

                    dtype = p.annotation

                    if dtype is inspect._empty:
                        info['type'] = json.dumps(None)
                    elif hasattr(dtype, '__name__'):
                        info['type'] = dtype.__name__
                    else:
                        info['type'] = str(p.annotation)
                    js.update({item: info})
            return js

        func_details = {
            "filters": {},
            "generators": {},
            "io": {},
            "metrics": {},
            "networks": {},
            "tools": {}
        }

        def porespy_modules_populate(modules, module_strs):
            for i in range(len(modules)):
                for func in dir(modules[i]):
                    if not func.startswith('__'):
                        f = getattr(modules[i], func)
                        func_details[module_strs[i]][func] = return_arg_names_vals_and_types(f)

        # Currently, ps.networks is throwing an error and cannot be populated through the porespy_modules_populate function.
        # Will need to look into this further.
        modules = [ps.filters, ps.generators, ps.io, ps.metrics, ps.tools];
        modules_strs = ['filters', 'generators', 'io', 'metrics', 'tools']
        porespy_modules_populate(modules, modules_strs)
        return func_details

# Model that uses the Blobs method in the Generators from PoreSpy
class GeneratorBlobs(models.Model):
    porosity = models.FloatField(null=True, blank=True, default=0.6)
    blobiness = models.IntegerField(null=True, blank=True, default=2)
    dimension_x = models.IntegerField(null=True, blank=True, default=500)
    dimension_y = models.IntegerField(null=True, blank=True, default=500)
    dimension_z = models.IntegerField(null=True, blank=True, default=0)

    @property
    def generated_image(self):
        int_dimension_x = int(self.dimension_x)
        int_dimension_y = int(self.dimension_y)
        int_dimension_z = int(self.dimension_z)
        float_porosity = float(self.porosity)
        int_blobiness = int(self.blobiness)

        shape_array = []
        if int_dimension_z == 0:
            shape_array = [int_dimension_x, int_dimension_y]
        else:
            shape_array = [int_dimension_x, int_dimension_y, int_dimension_z]

        # Generator blob form PoreSpy, convert to numpy array, and make it RGB.
        im = ps.generators.blobs(shape=shape_array, porosity=float_porosity, blobiness=int_blobiness).tolist()

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
            return new_im_string
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
            return new_im_string

            # return "3dimensional"

        # plt.show(im)

        # try:
        #     lt = ps.filters.local_thickness(im)
        #     return lt
        # except Exception as e:
        #     return str(e)



        # im_data = np.array(im)
        # pil_img = Image.fromarray(im_data).convert("RGB")
        # buff = BytesIO()

        # Change black pixels to purple, white pixels to yellow.
        # Porous pixels are now yellow, solid pixels are now purple.
        # for x in range(pil_img.width):
        #     for y in range(pil_img.height):
        #         black, white = (0, 0, 0), (255, 255, 255)
        #         yellow, purple = (255, 255, 0), (128, 0, 128)
        #         if pil_img.getpixel((x, y)) == black:
        #             pil_img.putpixel((x, y), purple)
        #         else:
        #             pil_img.putpixel((x, y), yellow)
        #
        # pil_img.save(buff, format="PNG")
        # new_im_string = base64.b64encode(buff.getvalue()).decode("utf-8")
        # return new_im_string