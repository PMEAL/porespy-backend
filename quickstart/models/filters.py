from django.db import models
import base64
import json
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


class LocalThickness(models.Model):
    local_thickness_image = models.TextField(default="")

    @property
    def local_thickness_image_filtered(self):
        im = np.array(json.loads(self.local_thickness_image))
        lt = ps.filters.local_thickness(im)
        lt_data = np.array(lt)
        buff = BytesIO()
        plt.imshow(lt)
        plt.savefig(buff, format='png')
        new_filtered_img_string = base64.b64encode(buff.getvalue()).decode("utf-8")
        im_object_return = {
            'np_array': lt_data,
            'base_64': new_filtered_img_string
        }

        return im_object_return

# class ApplyChords(models.Model):
    ### INSERT NECESSARY BUSINESS LOGIC HERE


