from matplotlib import figure as fig
from matplotlib import pyplot as plt
import tensorflow_datasets as tfds
from tensorflow_datasets import testing

figures_dir = ('examples/')

def generate_visualization(ds_name):
    try:
        ds, ds_info = tfds.load(name=ds_name, split='train', with_info=True)
        fig = tfds.show_examples(ds_info, ds)
        path_dir = tfds.core.get_tfds_path(figures_dir)
        fig.savefig(path_dir+ds_name+'.png')

        print('Saved '+ ds_name + '.png' + 'to' + path_dir)
    except:
        print('The selected dataset is not supported')

