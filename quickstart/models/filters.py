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


# Model that uses the LocalThickness method in the Filters from PoreSpy
class LocalThickness(models.Model):
    local_thickness_image = models.TextField(default="")
    sizes = models.IntegerField(null=True, blank=True, default=25)
    mode = models.TextField(default="")

    @property
    def local_thickness_image_filtered(self):
        plt.close()
        im = np.array(json.loads(self.local_thickness_image))
        sizes_int = int(self.sizes)
        mode_str = str(self.mode)
        lt = ps.filters.local_thickness(im, sizes=sizes_int, mode=mode_str)
        lt_data = np.array(lt)
        buff = BytesIO()

        # Always renders a 3D image regardless.
        plt.imshow(np.atleast_3d(lt)[:, :, 0], interpolation="none", origin="lower")
        plt.savefig(buff, format='png', transparent=True)
        new_filtered_img_string = base64.b64encode(buff.getvalue()).decode("utf-8")
        # im_object_return contains the numpy array and base64 representations of the generated image.
        im_object_return = {
            'np_array': lt_data,
            'base_64': new_filtered_img_string
        }

        plt.close()
        return im_object_return


# class ApplyChords(models.Model):
    # TODO: start writing business logic for ApplyChords filter (and remaining filter functions)


