"""siim_acr_pneumothorax dataset."""

import tensorflow_datasets.public_api as tfds
import tensorflow as tf
import pandas as pd
import numpy as np
import os

# TODO(siim_acr_pneumothorax): BibTeX citation
_CITATION = """
@ONLINE {societyforimaginginformaticsinmedicine(siim)2019,
    author = "Society for Imaging Informatics in Medicine (SIIM)",
    title  = "SIIM-ACR Pneumothorax Segmentation",
    month  = "aug",
    year   = "2019",
    url    = "https://www.kaggle.com/c/siim-acr-pneumothorax-segmentation/overview/description"
}"""

# TODO(siim_acr_pneumothorax):
_DESCRIPTION = """
This dataset comes from the SIIM-ACR Pneumothorax Segmentation, 
held by SIIM in 2019. It contains over 15,000 chest X-ray scans
(~12,100 for training, ~3,100 for testing) and corresponding masks 
for pneumothorax diagnosis segmentation. All scans are stored in 
DICOM format, which consists of patient demographic information
(de-identified) and scan metadata. All scans are identified with
unique file names and the labels are stored in separate csv files.
The annotation information consists of 3 columns: scan ID, scan
unique name and the encoded pixels. Scans without pneumothorax
have “-1” value under “encoded pixels” column while positive
scans have masks of pneumothorax air regions stored in
RLE(run-length encoding) format. 
"""


class SiimAcrPneumothorax(tfds.core.GeneratorBasedBuilder):
    """TODO(siim_acr_pneumothorax): Short description of my dataset."""

    # TODO(siim_acr_pneumothorax): Set up version.
    VERSION = tfds.core.Version('0.1.0')

    def _info(self):
        return tfds.core.DatasetInfo(
            builder=self,
            description=_DESCRIPTION,
            features=tfds.features.FeaturesDict({
                "image": tfds.features.Tensor(shape=(1024, 1024, 1), dtype=tf.uint8),
                "mask": tfds.features.Tensor(shape=(1024, 1024, 1), dtype=tf.bool)
            }),
#             supervised_keys=('image', 'mask'),
            homepage='https://www.kaggle.com/c/siim-acr-pneumothorax'
                     '-segmentation',
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager):
        """Returns SplitGenerators."""
        # TODO(siim_acr_pneumothorax): Downloads the data and defines the 
        #  splits 
        # dl_manager is a tfds.download.DownloadManager that can be 
        #  used to download and extract URLs 
        
        kaggle_data = 'seesee/siim-train-test'
        data_dir = dl_manager.download_kaggle_data(kaggle_data)
        print(data_dir)
        return [
            tfds.core.SplitGenerator(
                name=tfds.Split.TRAIN,
                # This SIIM dataset only has labeled training images, 
                # so leave this part as it is These kwargs will be passed to
                # _generate_examples 
                gen_kwargs={
                    'data_dir': data_dir
                },
            ),
        ]

    def _generate_examples(self, data_dir):
        """Yields examples."""
        # TODO(siim_acr_pneumothorax): Yields (key, example) tuples from the
        #  dataset 
        #  ... generator for the image and mask Try 
        #  tfds.download.iter_archive 
        dataset_dir = data_dir
        train_glob = dataset_dir + '/siim/dicom-images-train/*/*/*.dcm'
        train_fns = sorted(tfds.core.lazy_imports.glob.glob(train_glob))
        df_full = pd.read_csv(dataset_dir + '/siim/train-rle.csv',
                              index_col='ImageId') 
        
        im_height = 1024
        im_width = 1024
        
        # Get images and masks
        for n, _id in enumerate(train_fns):
            dataset = tfds.core.lazy_imports.pydicom.read_file(_id)
            image = np.expand_dims(dataset.pixel_array, axis=2)
            try:
                if '-1' in df_full.loc[_id.split('/')[-1][:-4],' EncodedPixels']:
                    mask = np.zeros((im_height, im_width, 1))
                else:
                    if type(df_full.loc[_id.split('/')[-1][:-4],' EncodedPixels']) == str:
                        mask = np.expand_dims(self.rle2mask(df_full.loc[_id.split('/')[-1][:-4],
                                                                              ' EncodedPixels'], 
                                                                  im_height, im_width), axis=2)
                    else:
                        mask = np.zeros((im_height, im_width, 1), dtype=np.bool)
                        for x in df_full.loc[_id.split('/')[-1][:-4],' EncodedPixels']:
                            mask =  mask + np.expand_dims(self.rle2mask(x, im_height, im_width), axis=2)
            except KeyError:
                mask = np.zeros((im_height, im_width, 1), dtype=np.bool)
                # Assume missing masks are empty masks.
            yield _id, {
                'image': tf.convert_to_tensor(image),
                'mask': tf.convert_to_tensor(mask)
            }

    @staticmethod
    def rle2mask(rle, width, height):
        mask = np.zeros(width * height)
        array = np.asarray([int(x) for x in rle.split()])
        starts = array[0::2]
        lengths = array[1::2]

        current_position = 0
        for index, start in enumerate(starts):
            current_position += start
            mask[current_position:current_position + lengths[index]] = 255
            current_position += lengths[index]

        return mask.reshape(width, height)
    
    @staticmethod
    def mask2rle(img, width, height):
        lastColor = 0
        currentPixel = 0
        runStart = -1
        runLength = 0

        for x in range(width):
            for y in range(height):
                currentColor = img[x][y]
                if currentColor != lastColor:
                    if currentColor == 255:
                        runStart = currentPixel
                        runLength = 1
                    else:
                        rle.append(str(runStart))
                        rle.append(str(runLength))
                        runStart = -1
                        runLength = 0
                        currentPixel = 0
                elif runStart > -1:
                    runLength += 1
                lastColor = currentColor
                currentPixel += 1

        return " ".join(rle)
