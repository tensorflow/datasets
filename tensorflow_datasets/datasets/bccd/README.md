BCCD Dataset is a small-scale dataset for blood cells detection.

Thanks the original data and annotations from cosmicad and akshaylamba. The
original dataset is re-organized into VOC format. BCCD Dataset is under MIT
licence.

Data preparation is important to use machine learning. In this project, the
Faster R-CNN algorithm from keras-frcnn for Object Detection is used. From this
dataset, nicolaschen1 developed two Python scripts to make preparation data (CSV
file and images) for recognition of abnormalities in blood cells on medical
images.

export.py: it creates the file "test.csv" with all data needed: filename,
class_name, x1,y1,x2,y2. plot.py: it plots the boxes for each image and save it
in a new directory.

Image Type : jpeg(JPEG) Width x Height : 640 x 480
