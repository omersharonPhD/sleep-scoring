"""
Load a BrainVision file
=======================

This example demonstrate how to load a BrainVision file.

Required dataset at :
https://www.dropbox.com/s/t2bo9ufvc3f8mbj/sleep_brainvision.zip?dl=1

.. image:: ../../picture/picsleep/ex_LoadBrainVision.png
"""
import sys
sys.path.append('/Users/anjopagdanganan/visbrain-testing/port-visbrain-0.4.3')

import os
from visbrain_sleep_port.gui import Sleep
from visbrain_sleep_port.io import download_file, path_to_visbrain_data

###############################################################################
#                               LOAD YOUR FILE
###############################################################################
# Download dataset :
download_file("sleep_brainvision.zip", unzip=True, astype='example_data')
target_path = path_to_visbrain_data(folder='example_data')

dfile = os.path.join(target_path, 'sub-02.vhdr')
hfile = os.path.join(target_path, 'sub-02.hyp')
cfile = os.path.join(target_path, 'sub-02_config.txt')

# Open the GUI :
Sleep(data=dfile, hypno=hfile, config_file=cfile).show()
