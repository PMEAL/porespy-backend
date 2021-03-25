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
    x_axis_label = models.TextField(default="invasion size [voxels]")
    y_axis_label = models.TextField(default="volume fraction invaded [voxels]")

    @property
    def psd_im_metric(self):
        plt.close()
        im = np.array(json.loads(self.psd_im))
        int_bins = int(self.bins)
        log_bool = str(self.log) == 'True'
        int_voxel_size = int(self.voxel_size)
        data = ps.metrics.pore_size_distribution(im=im, bins=int_bins, log=log_bool, voxel_size=int_voxel_size)

        if log_bool:
            radii = data.logR
        else:
            radii = data.R

        buff = BytesIO()
        plt.plot(radii, data.cdf, 'bo-')
        plt.xlabel(self.x_axis_label)
        plt.ylabel(self.y_axis_label)
        plt.savefig(buff, format='png', transparent=True)
        plt.close()
        new_im_string = base64.b64encode(buff.getvalue()).decode("utf-8")

        file_headers = ['radii', 'cdf', 'pdf', 'satn']
        csv_string = ",".join(file_headers) + "\n"

        for i in range(len(radii)):
            csv_string += str(radii[i]) + "," + str(data.cdf[i]) + "," + str(data.pdf[i]) + "," + str(data.satn[i]) + "\n"

        # im_object_return contains the numpy array of the input image,
        # the base64 representation of the generated metric,
        # and the string of contents for the .csv file
        im_object_return = {
            'np_array': im,
            'base_64': new_im_string,
            'csv_string': csv_string
        }

        return im_object_return
