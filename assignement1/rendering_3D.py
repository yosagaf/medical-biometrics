

# import ImageIO and NumPy
import imageio
import numpy as np
import matplotlib.pyplot as plt
from utils.utils import *
from mayavi.mlab import *

dirname = 'data/'

# read as volume
vol = imageio.volread(dirname, 'DICOM')

# stack image into a volume

print(type(vol))
print("Dimensions of image array :", vol.shape)
#print("Available metadata :", vol.meta.keys())
#plt.imshow(vol[1], aspect=1)
#plt.show()

'''
def remove_keymap_conflicts(new_keys_set):
    for prop in plt.rcParams:
        if prop.startswith('keymap.'):
            keys = plt.rcParams[prop]
            remove_list = set(keys) & new_keys_set
            for key in remove_list:
                keys.remove(key)

def multi_slice_viewer(volume):
    remove_keymap_conflicts({'j', 'k'})
    fig, ax = plt.subplots()
    ax.volume = volume
    ax.index = volume.shape[0] // 2
    ax.imshow(volume[ax.index])
    fig.canvas.mpl_connect('key_press_event', process_key)

def process_key(event):
    fig = event.canvas.figure
    ax = fig.axes[0]
    if event.key == 'j':
        previous_slice(ax)
    elif event.key == 'k':
        next_slice(ax)
    fig.canvas.draw()

def previous_slice(ax):
    volume = ax.volume
    ax.index = (ax.index - 1) % volume.shape[0]  # wrap around using %
    ax.images[0].set_array(volume[ax.index])

def next_slice(ax):
    volume = ax.volume
    ax.index = (ax.index + 1) % volume.shape[0]
    ax.images[0].set_array(volume[ax.index])

multi_slice_viewer(vol)
'''