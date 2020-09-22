"""isic2019 dataset."""
import tensorflow_datasets.public_api as tfds
import tensorflow as tf
import os

_URL = 'https://challenge2019.isic-archive.com/data.html'

_CITATION = """\
@article{DBLP:journals/corr/abs-1803-10417,
  author    = {Philipp Tschandl and
               Cliff Rosendahl and
               Harald Kittler},
  title     = {The {HAM10000} Dataset: {A} Large Collection of Multi-Source Dermatoscopic
               Images of Common Pigmented Skin Lesions},
  journal   = {CoRR},
  volume    = {abs/1803.10417},
  year      = {2018},
  url       = {http://arxiv.org/abs/1803.10417},
  archivePrefix = {arXiv},
  eprint    = {1803.10417},
  timestamp = {Mon, 13 Aug 2018 16:48:02 +0200},
  biburl    = {https://dblp.org/rec/journals/corr/abs-1803-10417.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
@article{DBLP:journals/corr/abs-1902-03368,
  author    = {Noel C. F. Codella and
               Veronica Rotemberg and
               Philipp Tschandl and
               M. Emre Celebi and
               Stephen W. Dusza and
               David Gutman and
               Brian Helba and
               Aadi Kalloo and
               Konstantinos Liopyris and
               Michael A. Marchetti and
               Harald Kittler and
               Allan Halpern},
  title     = {Skin Lesion Analysis Toward Melanoma Detection 2018: {A} Challenge
               Hosted by the International Skin Imaging Collaboration {(ISIC)}},
  journal   = {CoRR},
  volume    = {abs/1902.03368},
  year      = {2019},
  url       = {http://arxiv.org/abs/1902.03368},
  archivePrefix = {arXiv},
  eprint    = {1902.03368},
  timestamp = {Tue, 21 May 2019 18:03:39 +0200},
  biburl    = {https://dblp.org/rec/journals/corr/abs-1902-03368.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
@misc{combalia2019bcn20000,
    title={BCN20000: Dermoscopic Lesions in the Wild},
    author={Marc Combalia and Noel C. F. Codella and Veronica Rotemberg and Brian Helba and Veronica Vilaplana and Ofer Reiter and Cristina Carrera and Alicia Barreiro and Allan C. Halpern and Susana Puig and Josep Malvehy},
    year={2019},
    eprint={1908.02288},
    archivePrefix={arXiv},
    primaryClass={eess.IV}
}
"""


_DESCRIPTION = """\
For the ISIC 2019 grand challenge, the International Skin Imaging foundation released a data set containing 25,331 dermoscopic images that characterize 8 different types of skin cancers. Each image has a ground truth classification of Melanoma, Melanocytic nevus, Basal cell carcinoma, Actinic keratosis, Benign keratosis, Dermatofibroma, Vascular lesion, Squamous cell carcinoma, or None of the others. There is additional metadata for most, but not all images. This metadata includes information on patient age, patient sex, general anatomic site of dermoscopic image, and common lesion identifier (images of the same lesion). This dataset could be used to train image classification networks to identify the most common types of skin cancer from dermoscopic images
The dataset currently has two configs,
'full': 
    gives the eniter training dataset without, but the metadata is missing or incomplete in a few thousand entries. labels marked NA identify missing entries and is used across all fields 
'complete_metadata':
    provides only the entries were the metadata is available for approximate age 'represented as a string of 5 year incriments', lesion location, and patient sex.

repeated lesion id's are stored as a class variable under "lesion_id_family" to distinguish lesions from the same patient, and 'lesion_id' is used to represent the name of the given lesion. Entries missing a lesion id are assumed to be destinct entries, and not repeated. 
"""

_Image_URL = 'https://s3.amazonaws.com/isic-challenge-2019/ISIC_2019_Training_Input.zip'
_Data_Labels_URL = 'https://s3.amazonaws.com/isic-challenge-2019/ISIC_2019_Training_GroundTruth.csv'
_Meta_Data_URL= 'https://s3.amazonaws.com/isic-challenge-2019/ISIC_2019_Training_Metadata.csv'


_LABELS = ["Melanoma", "Melanocytic_nevus", "Basal_cell_carcinoma", "Actinic_keratosis", "Benign_keratosis", "Dermatofibroma", "Vascular_lesion", "Squamous_cell_carcinoma", "None_of_the_above"]
_AGE_APPOXIMATE = ['NA','0','5','10','15','20','25','35','40','45','50','55','60','65','70','75','80','85']
_LESION_LOCATION  =['NA','head/neck','anterior_torso','posterior_torso','lateral_torso','upper_extremity','lower_extremity','palms/soles','oral/genital']
_Sex = ['NA','female','male']

class Isic2019Config(tfds.core.BuilderConfig):
  """BuilderConfig for DeeplesionConfig."""
  def __init__(self, name=None,**kwargs):
    super(Isic2019Config, self).__init__(name=name,
                         version=tfds.core.Version('0.1.0'),**kwargs)

class Isic2019(tfds.core.GeneratorBasedBuilder):
    BUILDER_CONFIGS = [
        Isic2019Config(
            name='full',
            description=_DESCRIPTION,
        ),
        Isic2019Config(
            name='complete_metadata',
            description=_DESCRIPTION,
        ),
    ]
    """TODO(ISIC_2019): Short description of my dataset."""
    # TODO(ISIC_2019): Set up version.
    VERSION = tfds.core.Version('0.1.0')
    def _info(self):
        if self.builder_config.name == 'full':
            features=tfds.features.FeaturesDict({
                "image_name": tfds.features.Text(),
                "image": tfds.features.Image(encoding_format='jpeg'),
                "label": tfds.features.ClassLabel(names=_LABELS),
                "age": tfds.features.ClassLabel(num_classes=19),
                "lesion_location": tfds.features.ClassLabel(names = ['NA','head/neck','anterior_torso','posterior_torso',
                                                                     'lateral_torso','upper_extremity','lower_extremity','palms/soles','oral/genital']),
                "lesion_id": tfds.features.Text(),
                "lesion_id_family": tfds.features.ClassLabel(num_classes=11848),
                "sex": tfds.features.ClassLabel(names= ['NA','female','male']),
                })
        elif self.builder_config.name == 'complete_metadata':
            features=tfds.features.FeaturesDict({
                "image_name": tfds.features.Text(),
                "image": tfds.features.Image(encoding_format='jpeg'),
                "label": tfds.features.ClassLabel(names=_LABELS),
                "age": tfds.features.ClassLabel(num_classes=18),
                "lesion_location": tfds.features.ClassLabel(names = ['head/neck','anterior_torso','posterior_torso','lateral_torso',
                                                             'upper_extremity','lower_extremity','palms/soles','oral/genital']),
                "lesion_id": tfds.features.Text(),
                "lesion_id_family": tfds.features.ClassLabel(num_classes=11848), #every sample with an a lesion id has complete metadata
                "sex": tfds.features.ClassLabel(names= ['female','male']),
                })
        elif self.builder_config.name == 'labels_only':
            features=tfds.features.FeaturesDict({
                "image_name": tfds.features.Text(),
                "image": tfds.features.Image(encoding_format='jpeg'),
                "label": tfds.features.ClassLabel(names=_LABELS),
                })
        else:
            raise AssertionError('No builder_config found!')
            
        return tfds.core.DatasetInfo(
            builder=self,
            description=_DESCRIPTION,
            supervised_keys=("image", "label"),
            features=features,
            homepage=_URL,
            citation=_CITATION,
        ) 

    def _split_generators(self, dl_manager):
        """Returns SplitGenerators."""
        # TODO(ISIC_2019): Downloads the data and defines the splits
        # dl_manager is a tfds.download.DownloadManager that can be used to
        # download and extract URLs
        _image_path, _labels_path, _meta_path = dl_manager.download_and_extract([_Image_URL, _Data_Labels_URL, _Meta_Data_URL])
        _image_path = os.path.join(_image_path,'ISIC_2019_Training_Input')
        return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            # These kwargs will be passed to _generate_examples
            gen_kwargs={
                "image_path": _image_path,
                "data_parser": Annotations(_labels_path,_meta_path)
            },
        ),
        ]
    
    
    def _match_label(self,_label_str_list,_this_value):
        return tf.squeeze(tf.where(tf.strings.regex_full_match(_label_str_list,_this_value)))
    
    
    def _generate_examples(self, image_path,data_parser):
        image_name_tensor = tf.squeeze(data_parser._Data_Library['Image_name'])
        label_tensor = tf.squeeze(data_parser._Data_Library['Label'])
        age_tensor = tf.squeeze(data_parser._Data_Library['Age'])
        lesion_location_tensor = tf.squeeze(data_parser._Data_Library['Lesion_location'])
        lesion_id_tensor = tf.squeeze(data_parser._Data_Library['Lesion_id_list'])
        repeated_id_tensor = tf.squeeze(data_parser._Data_Library['Repeated_id'])
        sex_tensor = tf.squeeze(data_parser._Data_Library['Sex'])
        
  
        if self.builder_config.name == 'complete_metadata':
            data_parser.remove(Age = ['NA'], Lesion_location = ['NA'], Sex = ['NA'])
            data_of_interst = tf.where(data_parser._iter_idx)
        else:
            data_of_interst = tf.where(data_parser._iter_idx)
            
        for val in enumerate(data_of_interst):
            idx = int(data_of_interst[val[0]])
            if self.builder_config.name == 'labels_only':
                features = {"image_name": image_name_tensor[idx].numpy().decode('ascii'),
                            "image": os.path.join(image_path, (image_name_tensor[idx].numpy().decode('ascii')+ str('.jpg'))),
                            "label": int(self._match_label(data_parser.selected_data['Label'], label_tensor[idx]).numpy())}
            else:
                features = {"image_name": image_name_tensor[idx].numpy().decode('ascii'),
                            "image": os.path.join(image_path, (image_name_tensor[idx].numpy().decode('ascii')+ str('.jpg'))),
                            "label": int(self._match_label(data_parser.selected_data['Label'], label_tensor[idx]).numpy()),
                            'age': int(self._match_label(data_parser.selected_data['Age'], age_tensor[idx]).numpy()),
                            "lesion_id": lesion_id_tensor[idx].numpy().decode('ascii'),
                            "lesion_id_family": tf.cast(tf.squeeze(tf.where(tf.strings.regex_full_match(data_parser._Data_Library['Unique_lesion_id'],lesion_id_tensor[idx]))),dtype=tf.int32),
                            'lesion_location': int(self._match_label(data_parser.selected_data['Lesion_location'], lesion_location_tensor[idx]).numpy()),
                            'sex': int(self._match_label(data_parser.selected_data['Sex'], sex_tensor[idx]).numpy())
                           }
            yield image_name_tensor[idx].numpy().decode('ascii'), features
   
class csv_parser():
    
    def __init__(self,_Label_csv_path,_Meta_csv_path):
        self._labels_path = _Label_csv_path
        self._meta_path = _Meta_csv_path
        self._extract_Meta_Data()
        
    @tf.function
    def _parse_csv(self,_csv_file_path):
        @tf.function
        def _split_map(_line):
            return tf.strings.strip(tf.compat.v1.strings.split(_line, sep=',').values[:])
        _split_csv = tf.map_fn(
            _split_map,tf.compat.v1.strings.split(input=tf.strings.strip(tf.io.gfile.GFile(_csv_file_path).read()),sep='\n').values[:],parallel_iterations= 10)
        return _split_csv
    
    def _extract_Meta_Data(self):
        _Label_Data = self._parse_csv(self._labels_path)
        _Meta_Data = self._parse_csv(self._meta_path)
        #Helper Functions
        def _replace_tensor_values(_data_to_edit,_new_value,_replace_idx):
            #function performs _data_to_edit[_replace_idx] = _new_value
            #acting as a work around for eager tensors
            if (tf.size(_replace_idx)==1):
                _replace_value = _new_value
            else:
                _replace_value = tf.repeat(_new_value,tf.size(_replace_idx))
            #find the location of index's to keep constant
            _keep_idx = tf.where(tf.equal(tf.constant([0]),tf.cast(tf.scatter_nd(_replace_idx,tf.ones(tf.size(_replace_idx)),
                                                                                 tf.expand_dims(tf.size(_data_to_edit),axis=0)),dtype=tf.int32)))
            _keep_value = tf.gather_nd(_data_to_edit,_keep_idx)
            return tf.dynamic_stitch([tf.cast(tf.squeeze(_replace_idx),dtype=tf.int32),
                                          tf.cast(tf.squeeze(_keep_idx),dtype=tf.int32)],[_replace_value,_keep_value])
        
        
        @tf.function
        def _find_empty_strings(_this_tensor_string):
                return tf.cast(tf.where(tf.equal(tf.constant([0]),tf.strings.length(_this_tensor_string,unit="UTF8_CHAR"))),dtype=tf.int32)
            
        @tf.function
        def _find_non_empty_strings(_this_tensor_string):
            return tf.cast(tf.where(tf.greater(tf.strings.length(_this_tensor_string,unit="UTF8_CHAR"),tf.constant([0]))),dtype=tf.int32)
            #Extract Functions
            
        @tf.function
        def _get_labels(_data_split_csv):
            _t_labels = tf.convert_to_tensor(_LABELS)
            @tf.function
            def assign_label(_label_row):
                this_label = _t_labels[_label_row]
                return this_label
            _image_name = _data_split_csv[1:,0]
            _label = tf.map_fn(assign_label,tf.where(tf.strings.regex_full_match(_data_split_csv[1:,1:], '1.0'))[:,1],dtype=tf.string,parallel_iterations= 10)
            return _image_name, _label

        def _get_age(_age_csv):
            _raw_age = _age_csv[1:,1]
            _age_aprox = _replace_tensor_values(_raw_age,'NA',_find_empty_strings(_raw_age))
            #_age,_age_idx,_age_counts = tf.unique_with_counts(_raw_age)
            return _age_aprox
        
        def _get_location(_location_csv):
            _location = _location_csv[1:,2]
            _location = _replace_tensor_values(_location,'NA',_find_empty_strings(_location))
            _location = tf.strings.regex_replace(_location,' ','_')
            return(_location)
        
        def _get_Lesion_ID(_meta_ID_csv):
            def _get_ID(_raw_id_data):
                _is_empty_idx = _find_empty_strings(_raw_id_data)
                return _replace_tensor_values(_raw_id_data,'NA',_is_empty_idx)
            _full_id_list = _get_ID(_meta_ID_csv[1:,3])
            _unique_ids,_id_locations,_repeat_counts = tf.unique_with_counts(_full_id_list)
            #Find Index of all values images with no provided lession ID
            _NA_id_idx = tf.constant(tf.where(tf.strings.regex_full_match(_unique_ids,'NA')))
            #Edit repeat counts so that all unlabled ID's are assumed to be unique
            _repeat_counts = _replace_tensor_values(tf.cast(_repeat_counts,dtype=tf.int32),
                                                        tf.cast(1,dtype=tf.int32),tf.cast(_NA_id_idx,dtype=tf.int32))
            #Find lesion ID index number for all lesions with repeated images, i.e. non unique images
            _repeat_ids = tf.where(tf.math.greater(_repeat_counts,tf.constant([1])))
            #Find the index of all non repeated lesion IDs
            _repeat_idx = tf.where(tf.math.equal(tf.cast(_id_locations,dtype=tf.int32),tf.cast(_repeat_ids,dtype=tf.int32)))
            #set all index's of repeated id's to zeros, then use tf.where to make boolian. _repeated = False gives non repeated ID's
            _sf_repeated = _replace_tensor_values(
                tf.cast(tf.zeros(tf.size(_full_id_list)), dtype=tf.int32),
                tf.cast(1,dtype=tf.int32)
                ,tf.expand_dims(tf.cast(tf.squeeze(_repeat_idx[:,1]), dtype=tf.int32), axis=1))
            return _full_id_list, _sf_repeated, _unique_ids, _id_locations
        
        def _get_sex(_sex_csv):
            return _replace_tensor_values(_sex_csv[1:,4],'NA',_find_empty_strings(_sex_csv[1:,4]))
        
        these_image_names, these_labels = _get_labels(_Label_Data)
        these_lesion_ids, these_repeated_ids, unique_ids, unique_id_locations = _get_Lesion_ID(_Meta_Data)
        
        self._Data_Library = {
            'Image_name': these_image_names,
            'Label': these_labels,
            'Age': _get_age(_Meta_Data),
            'Lesion_location':  _get_location(_Meta_Data),
            'Lesion_id_list':these_lesion_ids,
            'Repeated_id':tf.strings.as_string(these_repeated_ids),
            'Unique_lesion_id': unique_ids,
            'Unique_lesion_id_locations': unique_id_locations,
            'Sex': _get_sex(_Meta_Data),
        }
        
        
class Annotations(csv_parser):
    
    def __init__(self, _labels_path, _meta_data_path):
        super().__init__(_labels_path, _meta_data_path)
        #indexs = tf.range(tf.size(self._Image_Names))
        self.default()
        
    #Sets the default values to return. The default conatains all values in the dataset, but built in functions allow the user to subselect desired criteria
    #If the user wants to restore default values they just need to call data.default()
    #To specify conditions to include use the function data.select(),
    #To specify conditions to exclude use the function data.remove(),
    def default(self):
        self._iter_idx = tf.ones(tf.size(self._Data_Library['Image_name']),dtype=tf.int32)
        self._data_valid_values = {
            'Label': ("Melanoma", "Melanocytic_nevus", "Basal_cell_carcinoma", "Actinic_keratosis", "Benign_keratosis",
                      "Dermatofibroma", "Vascular_lesion","Squamous_cell_carcinoma", "None_of_the_above"),
            'Age': ('NA','0','5','10','15','20','25','30','35','40','45','50','55','60','65','70','75','80','85'),
            'Lesion_location': ('NA','head/neck','anterior_torso','posterior_torso','lateral_torso','upper_extremity','lower_extremity',
                    'palms/soles','oral/genital'),
            'Sex': ('NA','female','male'),
            #'Image_name': self._Data_Library['Image_name'],
            #'Unique_lesion_id': self._Data_Library['Unique_lesion_id'],
            'Repeated_id': ('0','1')}
        self._supported_sort_methods = {'sort_by': ('image','lesion_id')}
        self.sort = {'sort_by': ('image')}
        self.selected_data = self._data_valid_values.copy()
        
    def get_matching_sample_ids(self, idx_of_image):
        #find index of lesion id in unique names list
        name_of_id = self._Data_Library['Lesion_id_list'][idx_of_image]
        if (name_of_id != 'NA'):
            lesion_id_idx = tf.cast(tf.squeeze(tf.where(tf.strings.regex_full_match(self._Data_Library['Unique_lesion_id'],name_of_id))),dtype=tf.int32)

            #find location of matching ids
            matching_lesion_ids = tf.cast(tf.squeeze(tf.where(tf.equal(self._Data_Library['Unique_lesion_id_locations'],lesion_id_idx))),dtype=tf.int32).numpy()

            #find image names of matching ids
            _matching_images = tf.gather(self._Data_Library['Image_name'],matching_lesion_ids)
        else:
            _matching_images = self._Data_Library['Image_name'][idx_of_image]
        return _matching_images
    
    def select(self,**kwargs):
            if self._valid_dict(self._data_valid_values,kwargs)==True:
                kwargs = self._format_key_values(kwargs)
                for key in kwargs.keys():   
                    self.selected_data[key] = kwargs[key]
                #update the output index values
                self._output_idx()
                
                
    def remove(self,**kwargs):
        if self._valid_dict(self._data_valid_values,kwargs)==True:
            kwargs = self._format_key_values(kwargs)
            for key in kwargs.keys():
                for idx in range(tf.size(kwargs[key])):
                    #initial call to self._valid_dict will ensure key and value paris are valid
                    #this if statement tells the function to ignore values that were already removed.
                    if kwargs[key][idx] in self.selected_data[key]:
                        _edit_list = list(self.selected_data[key])
                        _edit_list.remove(kwargs[key][idx])
                        self.selected_data[key] = tuple(_edit_list)
            #update the output index values
            self._output_idx()
    #Ensure that all values in dictionary are supported in the dataset 
    
    def return_data(self):
        print(self._Data_Library['Image_name'])
        print(self._Data_Library['Label'])
        print(self._Data_Library['Age'])
        print(self._Data_Library['Lesion_location'])
        print(self._Data_Library['Lesion_id_list'])
        print(self._Data_Library['Repeated_id'])
        print(self._Data_Library['Sex'])
        return self._Data_Library['Image_name'], self._Data_Library['Label'], self._Data_Library['Age'], self._Data_Library['Lesion_location'], self._Data_Library['Lesion_id_list'], self._Data_Library['Repeated_id'], self._Data_Library['Sex']
    
    def _valid_dict(self,_compare_dict,_this_dict):
        for key in _this_dict.keys():
            #check for valid kwarg names
            if not key in _compare_dict:
                print(key, 'is not a supported value. Supported values include ', _compare_dict.keys())
                return 0
            #ensure kwargs values are in the proper format
            if tf.rank(_this_dict[key])==0:
                _this_dict[key] = tf.convert_to_tensor([_this_dict[key]])
            else:
                _this_dict[key] = tf.convert_to_tensor(_this_dict[key])
            if (_this_dict[key].dtype != tf.string):
                _this_dict[key] = tf.strings.as_string(_this_dict[key])
            #check for valid values in kwargs
            for idx in range(tf.size(_this_dict[key])):
                if not _this_dict[key][idx] in _compare_dict[key]:
                    print((_this_dict[key][idx], 'is an innvalid element name. Valid element names of ', key,' include', _compare_dict[key]))
                    return 0
        return True
    
    def _output_idx(self):
        #create an array of ones that is the length of the enire dataset
        self._iter_idx = tf.ones(tf.size(self._Data_Library['Image_name']),dtype=tf.int32)
        #This is call is a backup in case the user decideds to append selection by hand rather than using built in functions
        if self._valid_dict(self._data_valid_values,self.selected_data)==True:
            self.selected_data = self._format_key_values(self.selected_data)
            for key in self.selected_data:
                #gives zeros values to the indexes that do not meet the conditions of selected_data
                self._iter_idx = self._iter_idx*self._valid_idx(self._Data_Library[key],self.selected_data[key])
                
    #backup to ensure users entered values in the correct format. 
    def _format_key_values(self,_this_dict):
        for key in _this_dict.keys():
            if tf.rank(_this_dict[key])==0:
                _this_dict[key] = tf.convert_to_tensor([_this_dict[key]])
            else:
                _this_dict[key] = tf.convert_to_tensor(_this_dict[key])
            if (_this_dict[key].dtype != tf.string):
                _this_dict[key] = tf.strings.as_string(_this_dict[key])
        return _this_dict
    
    #find the location of values that match the selected criteria. Returns an int32 array containing zeros or ones. 
    def _valid_idx(self,_this_data, _use_values):
        def _map_valid(this_idx):
            out = tf.cast(tf.strings.regex_full_match(_this_data,_use_values[this_idx]),dtype=tf.int32)
            return out
        _valid = tf.map_fn(_map_valid,tf.range(tf.size(_use_values)))
        _valid = tf.math.reduce_max(_valid,axis=0)
        return _valid