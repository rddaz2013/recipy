"""
Sample script that runs skimage functions logged by recipy.
"""

# Copyright (c) 2016 University of Edinburgh.

from __future__ import (nested_scopes, generators, division,
                        absolute_import, with_statement,
                        print_function, unicode_literals)

import recipy

import os
import sys
import numpy as np
from skimage import external
from skimage import io
from skimage import transform

from integration_test.packages.base import Base


class SkimageSample(Base):
    """
    Sample script that runs skimage functions logged by recipy.

    This class assumes the existence of a data/skimage directory,
    co-located with this file, with the following content:

    * image.tiff: TIFF file
    * sift.key: SIFT file
    * image.surf: SURF file

    sift.key can be generated using
    [SIFT](http://people.cs.ubc.ca/~lowe/keypoints/) Version 4, July
    2005, on Windows 7, as follows (where book.pgm is provided with
    SIFT):

        siftWin32.exe < book.pgm > sift.key

    image.surf can be generated using
    [SURF](http://www.vision.ee.ethz.ch/~surf/) Version 1.0.9 (Linux,
    GCC 4, 32 bit) (12/20/2006) on Ubuntu 14.04.3 LTS as follows
    (using book.pgm from SIFT) as follows:

        ./surf.ln -i book.pgm -o image.surf

    All functions that save files delete the files after saving,
    to keep the directory clean.
    """

    def __init__(self):
        """
        Constructor. Set data_dir attribute with path to data files needed
        by this class.
        """
        Base.__init__(self)
        self.data_dir = os.path.join(self.current_dir, "data", "skimage")

    def io_imread(self):
        """
        Use sklearn.io.imread to read image.tiff.
        """
        file_name = os.path.join(self.data_dir, "image.tiff")
        io.imread(file_name)

    def io_imsave(self):
        """
        Use sklearn.io.imread to read image.tiff and
        sklearn.io.imsave to save out_image.tiff.
        """
        file_name = os.path.join(self.data_dir, "image.tiff")
        out_file_name = os.path.join(self.data_dir, "out_image.tiff")
        data = io.imread(file_name)
        data = transform.rotate(data, 90)
        io.imsave(out_file_name, data)
        os.remove(out_file_name)

    def io_load_sift(self):
        """
        Use sklearn.io.load_sift to read sift.key.
        """
        file_name = os.path.join(self.data_dir, "sift.key")
        io.load_sift(file_name)

    def io_load_surf(self):
        """
        Use sklearn.io.load_surf to read image.surf.
        """
        file_name = os.path.join(self.data_dir, "image.surf")
        io.load_surf(file_name)

    def external_tifffile_imread(self):
        """
        Use sklearn.external.tifffile.imread to read image.tiff.
        """
        file_name = os.path.join(self.data_dir, "image.tiff")
        external.tifffile.imread(file_name)

    def external_tifffile_imsave(self):
        """
        Use sklearn.external.tifffile.imread to read image.tiff
        and sklearn.external.tifffile.imsave to save out_image.tiff.
        """
        file_name = os.path.join(self.data_dir, "image.tiff")
        out_file_name = os.path.join(self.data_dir, "out_image.tiff")
        data = external.tifffile.imread(file_name)
        data = transform.rotate(data, 90)
        data = 255 * data
        data = data.astype(dtype=np.uint8)
        external.tifffile.imsave(out_file_name, data)
        os.remove(out_file_name)


if __name__ == "__main__":
    SkimageSample().invoke(sys.argv)
