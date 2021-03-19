from django.db import models
import base64
from io import BytesIO
import json
import numpy as np
import porespy as ps
import matplotlib
# Agg Buffer Description:
# https://matplotlib.org/3.1.3/gallery/misc/agg_buffer.html
# Agg Buffer is used to access the figure canvas as an RGBA buffer, convert it to an array,
# and pass it to Pillow for rendering
matplotlib.use('Agg')
from matplotlib import pyplot as plt


# Model that uses the Pore Size Distribution method in the Metrics from PoreSpy
class PoreSizeDistribution(models.Model):
    psd_im = models.TextField(default="")
    bins = models.IntegerField(null=True, blank=True, default=10)
    log = models.BooleanField(default=True)
    voxel_size = models.IntegerField(null=True, blank=True, default=1)

    @property
    def psd_im_metric(self):
        plt.close()
        im = np.array(json.loads(self.psd_im))
        int_bins = int(self.bins)
        log_bool = str(self.log) == 'True'
        int_voxel_size = int(self.voxel_size)
        data = ps.metrics.pore_size_distribution(im=im, bins=int_bins, log=log_bool, voxel_size=int_voxel_size)

        # return data

        if log_bool:
            radii = data.logR
        else:
            radii = data.R

        buff = BytesIO()
        plt.plot(radii, data.cdf, 'bo-')

        # Labels should be entered by the user.
        plt.xlabel('invasion size [voxels]')
        plt.ylabel('volume fraction invaded [voxels]')
        plt.savefig(buff, format='png')
        plt.close()



        new_im_string = base64.b64encode(buff.getvalue()).decode("utf-8")
        # return new_im_string
        im_object_return = {
            'np_array': im,
            'base_64': new_im_string,
            'data': data
        }

        return im_object_return

        # ps.metrics.pore_size_distribution return a named tuple
        # with the following data
        # data.pdf
        # data.cdf
        # data.satn
        # data.bin_centers
        # data.bin_edges
        # data.bin_widths




        return "testingPSD?.."