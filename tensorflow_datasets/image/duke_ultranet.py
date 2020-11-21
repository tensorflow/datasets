"""TODO(duke_ultranet): Add a description here."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds
import logging

# TODO(duke_ultranet): BibTeX citation
_CITATION = """
"""

# TODO(duke_ultranet):
# Be sure to run pip install apache-beam==2.19.0
# and pip uninstall typing
_DESCRIPTION = {
    'channel': '''
        ```
        # Processing script
        
        DATASET_NAME=duke_ultranet/channel
        GCP_PROJECT=duke-ultrasound
        GCS_BUCKET=gs://duke-research-us
        
        echo "git+git://github.com/ouwen/datasets@tfds" > /tmp/beam_requirements.txt
        python3 -m tensorflow_datasets.scripts.download_and_prepare \
          --datasets=$DATASET_NAME \
          --data_dir=$GCS_BUCKET/tensorflow_datasets \
          --beam_pipeline_options=\
        "runner=DataflowRunner,project=$GCP_PROJECT,job_name=tfds-duke-ultranet,"\
        "staging_location=$GCS_BUCKET/binaries,temp_location=$GCS_BUCKET/temp,"\
        "requirements_file=/tmp/beam_requirements.txt,region=us-east1,"\
        "autoscaling_algorithm=NONE,num_workers=20,"\
        "machine_type=n1-highmem-16,experiments=shuffle_mode=service,disk_size_gb=500"
        ```
    
    ''',
    'iq_channel': '',
    'dynamic_rx_beamformed': '''
        ```
        # Processing script
        
        DATASET_NAME=duke_ultranet/dynamic_rx_beamformed
        GCP_PROJECT=duke-ultrasound
        GCS_BUCKET=gs://duke-research-us
        
        echo "git+git://github.com/ouwen/datasets@tfds" > /tmp/beam_requirements.txt
        python3 -m tensorflow_datasets.scripts.download_and_prepare \
          --datasets=$DATASET_NAME \
          --data_dir=$GCS_BUCKET/tensorflow_datasets \
          --beam_pipeline_options=\
        "runner=DataflowRunner,project=$GCP_PROJECT,job_name=tfds-duke-ultranet,"\
        "staging_location=$GCS_BUCKET/binaries,temp_location=$GCS_BUCKET/temp,"\
        "requirements_file=/tmp/beam_requirements.txt,region=us-east1,"\
        "autoscaling_algorithm=NONE,num_workers=20,"\
        "machine_type=n1-highmem-16,experiments=shuffle_mode=service,disk_size_gb=500"
        ```
    ''',
    'iq_dynamic_rx_beamformed': '',
    'b_mode': '''
        ```
        # Processing script
        
        DATASET_NAME=duke_ultranet/b_mode
        GCP_PROJECT=duke-ultrasound
        GCS_BUCKET=gs://duke-research-us
        
        echo "git+git://github.com/ouwen/datasets@tfds" > /tmp/beam_requirements.txt
        python3 -m tensorflow_datasets.scripts.download_and_prepare \
          --datasets=$DATASET_NAME \
          --data_dir=$GCS_BUCKET/tensorflow_datasets \
          --beam_pipeline_options=\
        "runner=DataflowRunner,project=$GCP_PROJECT,job_name=tfds-duke-ultranet-bmode,"\
        "staging_location=$q/binaries,temp_location=$GCS_BUCKET/temp,"\
        "requirements_file=/tmp/beam_requirements.txt,region=us-east1,"\
        "autoscaling_algorithm=NONE,num_workers=20,"\
        "machine_type=n1-standard-16,experiments=shuffle_mode=service,disk_size_gb=50"
        ```
    '''
}

_HOMEPAGE = """
"""

_BUCKET = 'gs://duke-research-us/hindexbooster'

_NAN_FILES = {75, 682, 3925, 2851, 3170, 1123, 2049, 45, 100, 37, 4, 5, 7, 4104, 2057, 4106, 4107, 2062, 4110, 4111, 4112, 4116, 4119, 25, 2074, 4122, 4124, 32, 2080, 4131, 2084, 4137, 2096, 4148, 54, 4152, 57, 4157, 4159, 2113, 67, 2115, 4166, 71, 72, 73, 2122, 2124, 4176, 2130, 2131, 85, 2135, 2136, 4183, 4185, 2140, 4193, 4197, 4199, 2152, 4210, 2169, 4217, 124, 2174, 4223, 4226, 4228, 2181, 4231, 4232, 137, 4234, 2187, 4236, 2190, 2193, 146, 2198, 2199, 4246, 2203, 158, 2207, 2209, 2213, 166, 2214, 170, 2220, 4269, 174, 2228, 2234, 187, 4284, 195, 2244, 201, 4299, 2252, 4300, 4301, 4307, 2264, 2267, 4319, 225, 228, 4329, 2282, 236, 4334, 2289, 243, 251, 4348, 253, 259, 265, 271, 272, 4367, 4369, 275, 4371, 2325, 4377, 288, 2338, 292, 4388, 309, 2357, 4405, 312, 315, 2364, 4415, 321, 2369, 2372, 2374, 2376, 4427, 4429, 337, 4441, 346, 4443, 4451, 4455, 2418, 4469, 2428, 4481, 2435, 388, 390, 4488, 4493, 4495, 4502, 408, 411, 420, 4516, 422, 4517, 424, 425, 4518, 4520, 428, 4521, 4523, 432, 4528, 2483, 436, 443, 444, 2491, 4543, 453, 2502, 2504, 2508, 4557, 462, 2511, 4560, 2515, 4568, 2522, 2525, 4573, 482, 488, 2536, 4585, 2539, 493, 494, 2545, 4596, 502, 514, 518, 2566, 2571, 4619, 4620, 4621, 2576, 532, 2587, 540, 542, 544, 548, 2597, 550, 552, 562, 2611, 4660, 2614, 2623, 4675, 2630, 585, 2634, 591, 2654, 609, 4706, 611, 2660, 4710, 4715, 620, 630, 639, 4735, 2695, 2699, 653, 2706, 2715, 4764, 2721, 691, 692, 701, 2750, 4801, 4802, 709, 713, 2761, 2762, 4810, 2765, 2767, 723, 4820, 725, 728, 4824, 2783, 738, 4835, 741, 746, 2796, 2800, 2801, 757, 2805, 759, 4854, 4859, 777, 2825, 2827, 2829, 2832, 785, 2841, 794, 2842, 4892, 2847, 4896, 801, 2849, 4904, 811, 812, 2862, 2863, 4913, 4917, 822, 824, 4920, 4922, 4927, 836, 2884, 4935, 840, 2892, 4942, 4946, 2901, 858, 863, 865, 866, 873, 4971, 876, 4974, 2929, 2932, 886, 4989, 894, 895, 4990, 904, 908, 2956, 911, 2963, 2971, 2972, 927, 2977, 2978, 936, 2991, 3005, 959, 3007, 3010, 965, 966, 968, 3016, 970, 3020, 3023, 3024, 977, 3032, 985, 3038, 991, 3044, 3046, 3057, 3063, 3065, 1019, 1022, 1024, 1026, 3080, 3082, 1038, 3086, 3089, 3094, 3100, 1053, 1054, 3101, 1057, 1058, 1063, 3116, 1070, 1071, 3118, 3119, 3120, 1076, 3128, 3144, 1100, 1102, 3153, 1106, 1108, 3157, 3158, 3159, 3165, 1120, 3169, 3174, 3176, 1130, 1131, 3183, 1150, 3200, 1153, 3205, 1161, 3211, 1166, 1172, 3229, 1182, 3242, 1199, 1210, 1215, 1219, 1220, 1222, 3271, 1241, 3291, 1244, 3293, 1252, 3301, 1261, 1262, 1263, 3309, 3316, 1270, 3345, 1300, 3353, 1310, 1315, 1316, 3364, 1319, 1322, 3373, 1326, 1330, 3380, 1334, 3385, 1339, 1340, 3388, 1355, 3403, 3405, 1361, 1367, 1369, 3417, 3422, 1375, 1378, 1385, 3442, 1400, 1405, 3457, 1414, 1417, 3465, 3471, 3490, 1443, 1445, 3500, 1463, 1464, 3515, 1472, 3523, 3524, 1481, 3534, 1490, 1496, 1501, 1502, 3551, 1517, 3568, 1540, 1542, 3592, 3610, 1569, 3617, 1576, 1577, 3630, 3631, 1585, 1596, 3644, 3648, 3652, 1611, 3661, 1614, 1619, 3667, 1622, 1631, 1635, 3690, 1643, 3691, 1645, 3695, 1648, 1652, 1657, 1659, 1670, 3721, 1676, 3724, 3725, 1682, 1689, 1690, 3737, 1694, 3747, 1702, 3750, 1708, 3766, 1719, 1720, 1729, 1730, 1731, 1732, 3783, 1736, 3785, 3786, 1744, 1746, 3797, 1751, 1753, 3801, 3803, 3805, 1758, 1759, 1769, 3823, 3833, 1786, 3841, 3849, 1814, 3870, 3873, 1826, 1827, 3878, 1834, 1845, 3897, 3899, 3906, 1859, 1865, 3916, 3918, 1884, 1886, 1888, 1893, 3955, 1909, 1911, 3959, 1914, 3964, 1917, 3974, 3980, 1936, 1939, 1944, 1948, 3999, 1957, 1958, 1963, 4012, 4015, 1968, 4016, 1974, 4029, 1982, 1983, 4030, 1987, 1995, 4046, 2003, 4051, 4053, 2008, 4058, 4059, 2014, 2019, 4071, 4075, 4079, 4085, 4093, 4095}

_BAD_FILES = {3584, 1025, 2048, 1538, 2564, 513, 4616, 3594, 3595, 1549, 4623, 2070, 3095, 2584, 3097, 23, 27, 1532, 1227, 3104, 4641, 1571, 3620, 4132, 39, 2601, 1066, 2090, 555, 1069, 2606, 47, 2607, 3117, 1074, 4657, 567, 2616, 569, 4670, 3135, 1090, 2628, 4677, 2631, 3663, 3668, 1621, 597, 3675, 4699, 1118, 3168, 98, 1634, 4194, 1125, 4200, 1641, 2668, 1647, 624, 3187, 2164, 1651, 1142, 4723, 4726, 3706, 3195, 4222, 127, 4737, 130, 1668, 3716, 645, 3717, 3210, 1164, 4238, 3216, 1171, 149, 3223, 3735, 3738, 4252, 2717, 4254, 4767, 159, 2210, 163, 1188, 1189, 4774, 3239, 4264, 4777, 171, 3243, 4268, 3757, 4274, 180, 182, 3767, 696, 694, 4790, 699, 3772, 2231, 191, 2752, 707, 2757, 198, 197, 714, 3787, 202, 205, 4814, 719, 1738, 1233, 4816, 3795, 1748, 213, 724, 3794, 217, 221, 4318, 1247, 3808, 1761, 4321, 4834, 4327, 3820, 3308, 751, 240, 3311, 4340, 3319, 4856, 1784, 1274, 4347, 1788, 3325, 4350, 1789, 1280, 1793, 2306, 3334, 1803, 267, 269, 2830, 3852, 1298, 3860, 4373, 3861, 3352, 4376, 3869, 4389, 806, 296, 297, 3884, 813, 3374, 4399, 2352, 820, 310, 3895, 823, 1337, 3386, 2363, 316, 2875, 831, 1346, 1347, 327, 3400, 842, 1354, 4426, 333, 3917, 2387, 4435, 853, 4438, 1879, 3928, 343, 4442, 2395, 4949, 855, 2398, 3530, 2916, 356, 3943, 4969, 4458, 4459, 3438, 2414, 367, 4465, 370, 1906, 4981, 1398, 1399, 2424, 2944, 897, 3459, 1923, 3975, 2952, 1931, 1935, 914, 3477, 2455, 3480, 3992, 2463, 1951, 4005, 427, 941, 944, 4530, 946, 1460, 439, 953, 3513, 1978, 1468, 3519, 4545, 4034, 1476, 3013, 1480, 2505, 2506, 971, 4556, 3532, 1486, 4559, 976, 2000, 4047, 3535, 981, 470, 3544, 4570, 3547, 4060, 3037, 3040, 481, 3043, 484, 4068, 2026, 491, 1516, 4590, 2544, 499, 2548, 1524, 1523, 2552, 508, 4094}

_FILES = list(set(range(5000)) - set(_NAN_FILES) - set(_BAD_FILES))

_TX_POS = np.array([-1.3188923611111137e-02, -1.2874774305555581e-02, -1.2560625000000027e-02, -1.2246475694444469e-02, -1.1932994791666688e-02, -1.1619513888888907e-02, -1.1305364583333352e-02, -1.0991215277777798e-02, -1.0677065972222240e-02, -1.0362916666666689e-02, -1.0048767361111127e-02, -9.7346180555555762e-03, -9.4204687500000217e-03, -9.1063194444444672e-03, -8.7928385416666897e-03, -8.4793576388889121e-03, -8.1652083333333559e-03, -7.8510590277778014e-03, -7.5369097222222452e-03, -7.2227604166666915e-03, -6.9086111111111318e-03, -6.5944618055555765e-03, -6.2803125000000211e-03, -5.9668315972222436e-03, -5.6533506944444660e-03, -5.3392013888889098e-03, -5.0250520833333553e-03, -4.7109027777777999e-03, -4.3967534722222455e-03, -4.0826041666666901e-03, -3.7684548611111308e-03, -3.4543055555555737e-03, -3.1401562500000210e-03, -2.8266753472222447e-03, -2.5125260416666881e-03, -2.1983767361111310e-03, -1.8842274305555758e-03, -1.5700781250000205e-03, -1.2559288194444655e-03, -9.4177951388891006e-04, -6.2763020833335394e-04, -3.1348090277779836e-04, -1.9931249937525191e-17,  3.1348090277775808e-04,  6.2763020833331339e-04,  9.4177951388886799e-04,  1.2559288194444239e-03,  1.5700781249999799e-03,  1.8842274305555346e-03,  2.1983767361110906e-03,  2.5125260416666473e-03,  2.8266753472222014e-03,  3.1401562499999793e-03,  3.4543055555555351e-03,  3.7684548611110909e-03,  4.0826041666666467e-03,  4.3967534722222030e-03,  4.7109027777777574e-03,  5.0250520833333119e-03,  5.3392013888888682e-03,  5.6533506944444235e-03,  5.9668315972222002e-03,  6.2803124999999778e-03,  6.5944618055555322e-03,  6.9086111111110876e-03,  7.2227604166666438e-03,  7.5369097222222009e-03,  7.8510590277777563e-03,  8.1652083333333108e-03,  8.4793576388888670e-03,  8.7928385416666446e-03,  9.1063194444444238e-03,  9.4204687499999801e-03,  9.7346180555555346e-03,  1.0048767361111091e-02,  1.0362916666666647e-02,  1.0677065972222203e-02,  1.0991215277777758e-02,  1.1305364583333312e-02,  1.1619513888888868e-02,  1.1932994791666646e-02,  1.2246475694444425e-02,  1.2560624999999983e-02,  1.2874774305555539e-02,  1.3188923611111096e-02])

_SUB_APERTURE_SIZE = 96
_CHANNELS = 180

class DukeUltranet(tfds.core.BeamBasedBuilder):
    """TODO(duke_ultranet): Short description of my dataset."""

    VERSION = tfds.core.Version('0.2.3', 'adds downsampled baseband IQ, adds test set')
    SUPPORTED_VERSIONS = [
          tfds.core.Version('0.2.2', 'dynamic_rx and bmode are cached')
      ]
    BUILDER_CONFIGS = [
        tfds.core.BuilderConfig(
            version=VERSION,
            name="channel",
            description="Raw channel data from simulated transducers."
        ),
        tfds.core.BuilderConfig(
            version=VERSION,
            name="iq_channel",
            description="IQ Raw channel data from simulated transducers."
        ),
        tfds.core.BuilderConfig(
            version=VERSION,
            name="dynamic_rx_beamformed",
            description="Dynamic recieve beamformed data windowed to target of interest."
        ),
        tfds.core.BuilderConfig(
            version=VERSION,
            name="iq_dynamic_rx_beamformed",
            description="IQ Dynamic recieve beamformed data windowed to target of interest."
        ),
        tfds.core.BuilderConfig(
            version=VERSION,
            name="b_mode",
            description="B mode image."
        )
    ]

    @staticmethod
    def get_rf_hdf5(filepath, i):
        h5py = tfds.core.lazy_imports.h5py
        
        with h5py.File(tf.io.gfile.GFile(filepath, 'rb'), mode='r') as f:
            nowall = f.get('rf_nowall')[()]
            wall = f.get('rf_wall')[()]
        return {
            'nowall': nowall,
            'wall': wall,
            'i': i
        }

    @staticmethod
    @tf.function
    def tf_demodulate(x, fs, f0, axis=-1):
        '''Uses baseband IQ and decreases axial samples by factor of 10'''
        fs = tf.cast(fs, tf.complex64)
        f0 = tf.cast(f0, tf.complex64)
        initial_downsampling = 2
        iq = DukeUltranet.tf_hilbert(x[..., ::initial_downsampling], axis=-1)
        t = tf.cast(tf.range(0, tf.shape(iq)[-1]), tf.complex64)*1/(fs/initial_downsampling)
        iq = iq*tf.math.exp(-1j*2*np.pi*f0*t[None, None, :])
        return iq[..., ::5]

    @staticmethod
    @tf.function
    def tf_hilbert(x, axis=-1):
        '''Performs 1d hilbert similar to scipy'''

        # Change axes to be most inner for fft 
        axis = tf.constant(axis)
        if axis < 0: axis = tf.rank(x) + axis
        axes = tf.range(tf.rank(x))
        axes = tf.math.mod(axes - tf.reduce_max(axes) + axis, tf.size(axes))
        x = tf.transpose(x, perm=axes)

        # Apply fft
        x = tf.cast(x, tf.complex64)
        Xf = tf.signal.fft(x)

        # Create 2U 
        N = tf.shape(Xf)[-1]
        h = tf.cast(tf.ones([N//2 + 1])*2, Xf.dtype)
        if tf.math.mod(N,2) == 0: h = tf.tensor_scatter_nd_update(h, [[0],[tf.size(h)-1]], [1,1])
        else: h = tf.tensor_scatter_nd_update(h, [[0]], [1])
        h = tf.concat([h, tf.zeros(N-tf.size(h), dtype=h.dtype)], axis=0)

        # Apply ifft and hilbert
        x = tf.signal.ifft(Xf*h)

        # Change axes back
        x = tf.transpose(x, perm=tf.argsort(axes))
        return x

    @staticmethod
    @tf.function
    def tf_log10(x):
        return tf.math.log(x) / tf.math.log(tf.constant(10, dtype=x.dtype))

    @staticmethod
    @tf.function
    def tf_db(x):
        return tf.constant(20, dtype=x.dtype) * DukeUltranet.tf_log10(x)

    @staticmethod
    @tf.function
    def batch_interp1d(x, x_min, x_max, y):
        '''
        y is an 3d array of function to interpolate where the last dimension is to be interpolated [..., N]
        x is a 3d array equal of locations to eval and is monotonically increasing
        '''
        x_max = x_max - 1
        valid_x = (x > x_min) & (x < x_max)

        x = tf.clip_by_value(x, x_min, x_max)
        x_floor = tf.cast(tf.math.floor(x), tf.int32)
        x_ceil = tf.cast(tf.math.ceil(x), tf.int32)

        y_floor = tf.gather(y, x_floor, axis=-1, batch_dims=2)
        y_ceil = tf.gather(y, x_ceil, axis=-1, batch_dims=2)

        out = y_floor + (y_ceil - y_floor)*(x - tf.cast(x_floor, y.dtype))
        out = out * tf.cast(valid_x, y.dtype)
        return out
    
    @staticmethod    
    def apply_delays(delays, data):
        '''
        data is a 3D array of shape (transmits, channels, axial_samples)
        delays is a 3D array of shape (transmits, channels, axial_samples)
        returns delayed data
        '''
        return DukeUltranet.batch_interp1d(delays, 0, tf.cast(delays.shape[-1], delays.dtype), data)

    @staticmethod
    @tf.function
    def beamform_dynamic_rx(data_shape, tx_pos, rx_pos, s0=0, c=1540, fs=None, s0_var=None, data_dtype=tf.float64):
        '''
        beamform_dynamic_rx will beamform focused data with a dynamic rx delay profile

        data is a 3D array of shape (transmits, channels, axial_samples)
        tx_pos is a 2D array shape (tx_beam_num, 3) where the last channel is (x,y,z) coordinates in cartesian space of the start beam.
        rx_pos is a 2D array shape (rx_beam_num, 3) where the last channel is (x,y,z) coordiates in cartesian space of the end beam.
        s0 is the sample number offset globally
        s0_var is sample number of the first sample across transmits
        c is the speed of sound (m/s)
        fs is the sampling frequency (Hz)
        tx_delays is an array of time delays (s) used to focus the beam.
        '''
        transmits = data_shape[0]
        channels = data_shape[1]
        axial_samples = data_shape[2]
        if fs is None: raise ValueError('fs cannot be None')
        if s0_var is None: s0_var = tf.zeros(transmits, dtype=data_dtype)
        c = tf.cast(c, data_dtype)
        fs = tf.cast(fs, data_dtype)
        s0 = tf.cast(s0, data_dtype)
        tx_pos = tf.cast(tx_pos, data_dtype)
        rx_pos = tf.cast(rx_pos, data_dtype)
        tx_pos = tx_pos[:,None,:]
        rx_pos = rx_pos[None, :, :]
        dx = c/fs
        x1=(s0+1)*dx
        dz = tf.cast(tf.range(axial_samples, delta=1, dtype=tf.int32), data_dtype)/2*dx
        tx_beam_path = dz[None, None, ...]

        # TODO only works for linear beams, use law of cosines for calculating sectorscans
        distance_from_beam = tf.norm(tx_pos - rx_pos, axis=2)[...,None]
        rx_echo_path = tf.sqrt(tx_beam_path**2 + distance_from_beam**2) + s0_var[..., None, None]*dx

        total_distance = rx_echo_path+tx_beam_path-x1
        s = total_distance/dx
        return s

    def _info(self):
        common = {
            'c': tfds.features.Tensor(shape=(), dtype=tf.float64),
            'fs': tfds.features.Tensor(shape=(), dtype=tf.float64),
            'tiny_imagenet': {
                'target_number': tfds.features.Tensor(shape=(), dtype=tf.int64),
                'body_wall_number': tfds.features.Tensor(shape=(), dtype=tf.int64),
                'target': tfds.features.Image(shape=(64,64,3), encoding_format='jpeg'),
                'clutter_wall': tfds.features.Image(shape=(64,64,3), encoding_format='jpeg')
            },
            'probe': {
                'tx_delays': tfds.features.Tensor(shape=(len(_TX_POS),_CHANNELS), dtype=tf.float64),
                'element_on_mask': tfds.features.Tensor(shape=(len(_TX_POS),_CHANNELS), dtype=tf.bool),
                'element_positions': tfds.features.Tensor(shape=(_CHANNELS,3), dtype=tf.float64),
                'rx_positions': tfds.features.Tensor(shape=(_CHANNELS,3), dtype=tf.float64),
                'tx_positions': tfds.features.Tensor(shape=(len(_TX_POS),3), dtype=tf.float64),
                'impulse': tfds.features.Tensor(shape=(57,), dtype=tf.float64),
                'pulse': tfds.features.Tensor(shape=(97,), dtype=tf.float64),
                'excitation': tfds.features.Tensor(shape=(41,), dtype=tf.float64),
                'a': tfds.features.Tensor(shape=(5,), dtype=tf.float64),
                'b': tfds.features.Tensor(shape=(5,), dtype=tf.float64),
                'pitch': tfds.features.Tensor(shape=(), dtype=tf.float64),
                't0': tfds.features.Tensor(shape=(), dtype=tf.float64),
                'f0_hz': tfds.features.Tensor(shape=(), dtype=tf.float64),
                'focus_depth': tfds.features.Tensor(shape=(), dtype=tf.float64)
            },
            'sim': {
                'B': tfds.features.Tensor(shape=(), dtype=tf.float64),
                'cmap': tfds.features.Tensor(shape=(1247, 1091), dtype=tf.float64),
                'atten': tfds.features.Tensor(shape=(), dtype=tf.float64),
                'cfl': tfds.features.Tensor(shape=(), dtype=tf.float64),
                'ncycles': tfds.features.Tensor(shape=(), dtype=tf.float64),
                'omega0': tfds.features.Tensor(shape=(), dtype=tf.float64),
                'p0': tfds.features.Tensor(shape=(), dtype=tf.float64),
                'ppw': tfds.features.Tensor(shape=(), dtype=tf.float64),
                'rho': tfds.features.Tensor(shape=(), dtype=tf.float64),
                'td': tfds.features.Tensor(shape=(), dtype=tf.float64),
                'v': tfds.features.Tensor(shape=(), dtype=tf.float64),
                'grid': {
                    'dT': tfds.features.Tensor(shape=(), dtype=tf.float64),
                    'dY': tfds.features.Tensor(shape=(), dtype=tf.float64),
                    'dZ': tfds.features.Tensor(shape=(), dtype=tf.float64),
                    'nT': tfds.features.Tensor(shape=(), dtype=tf.float64),
                    'nY': tfds.features.Tensor(shape=(), dtype=tf.float64),
                    'nZ': tfds.features.Tensor(shape=(), dtype=tf.float64),
                    'wY': tfds.features.Tensor(shape=(), dtype=tf.float64),
                    'wZ': tfds.features.Tensor(shape=(), dtype=tf.float64)
                },
            }
        }

        if self.builder_config.name is 'channel':
            return tfds.core.DatasetInfo(
                builder=self,
                description=_DESCRIPTION['channel'],
                features=tfds.features.FeaturesDict({
                    'data': {
                        'without_wall': tfds.features.Tensor(shape=(len(_TX_POS),_CHANNELS,7012), dtype=tf.float32),
                        'with_wall': tfds.features.Tensor(shape=(len(_TX_POS),_CHANNELS,7012), dtype=tf.float32)
                    },
                    'params': common
                }),
                supervised_keys=('data/with_wall', 'data/without_wall'),
                homepage=_HOMEPAGE,
                citation=_CITATION
            )
        
        if self.builder_config.name is 'iq_channel':
            return tfds.core.DatasetInfo(
                builder=self,
                description=_DESCRIPTION['iq_channel'],
                features=tfds.features.FeaturesDict({
                    'data': {
                        'without_wall_real': tfds.features.Tensor(shape=(len(_TX_POS),_CHANNELS,702), dtype=tf.float16),
                        'without_wall_imag': tfds.features.Tensor(shape=(len(_TX_POS),_CHANNELS,702), dtype=tf.float16),
                        'with_wall_real': tfds.features.Tensor(shape=(len(_TX_POS),_CHANNELS,702), dtype=tf.float16),
                        'with_wall_imag': tfds.features.Tensor(shape=(len(_TX_POS),_CHANNELS,702), dtype=tf.float16)
                    },
                    'params': common
                }),
                homepage=_HOMEPAGE,
                citation=_CITATION
            )
        
        if self.builder_config.name is 'dynamic_rx_beamformed':
            return tfds.core.DatasetInfo(
                builder=self,
                description=_DESCRIPTION['dynamic_rx_beamformed'],
                features=tfds.features.FeaturesDict({
                    'data': {
                        'without_wall': tfds.features.Tensor(shape=(len(_TX_POS),_CHANNELS,3117), dtype=tf.float32),
                        'with_wall': tfds.features.Tensor(shape=(len(_TX_POS),_CHANNELS,3117), dtype=tf.float32)
                    },
                    'params': common
                }),
                supervised_keys=('data/with_wall', 'data/without_wall'),
                homepage=_HOMEPAGE,
                citation=_CITATION
            )

        if self.builder_config.name is 'iq_dynamic_rx_beamformed':
            return tfds.core.DatasetInfo(
                builder=self,
                description=_DESCRIPTION['iq_dynamic_rx_beamformed'],
                features=tfds.features.FeaturesDict({
                    'data': {
                        'without_wall_real': tfds.features.Tensor(shape=(len(_TX_POS),_CHANNELS,312), dtype=tf.float16),
                        'without_wall_imag': tfds.features.Tensor(shape=(len(_TX_POS),_CHANNELS,312), dtype=tf.float16),
                        'with_wall_real': tfds.features.Tensor(shape=(len(_TX_POS),_CHANNELS,312), dtype=tf.float16),
                        'with_wall_imag': tfds.features.Tensor(shape=(len(_TX_POS),_CHANNELS,312), dtype=tf.float16)
                    },
                    'params': common
                }),
                homepage=_HOMEPAGE,
                citation=_CITATION
            )

        if self.builder_config.name is 'b_mode':
            return tfds.core.DatasetInfo(
                builder=self,
                description=_DESCRIPTION['b_mode'],
                features=tfds.features.FeaturesDict({
                    'data': {
                        'without_wall': tfds.features.Tensor(shape=(len(_TX_POS),3117), dtype=tf.float16),
                        'with_wall': tfds.features.Tensor(shape=(len(_TX_POS),3117), dtype=tf.float16),
                    },
                    'params': common
                }),
                supervised_keys=('data/with_wall', 'data/without_wall'),
                homepage=_HOMEPAGE,
                citation=_CITATION
            )

    def _split_generators(self, _):
        """Returns SplitGenerators."""
        return [
            tfds.core.SplitGenerator(
                    name=tfds.Split.TRAIN,
                    gen_kwargs={
                        'files': _FILES[1200:]
                    }
            ),
            tfds.core.SplitGenerator(
                    name=tfds.Split.TEST,
                    gen_kwargs={
                        'files': _FILES[:1200]
                    }
            )
        ]

    def _build_pcollection(self, pipeline, files):
        beam = tfds.core.lazy_imports.apache_beam
        h5py = tfds.core.lazy_imports.h5py
        signal = tfds.core.lazy_imports.scipy.signal
        
        filepaths_rf = []
        for file_num in files:
            for i in range(1,len(_TX_POS)+1):
                filepaths_rf.append((file_num, '{}/results/val_{}/rf_{}.mat'.format(_BUCKET, file_num, str(i).zfill(2)), i))

        def _download_rf(job):
            file_num, filepath, i = tuple(job)
            data = None
            try:
                data = DukeUltranet.get_rf_hdf5(filepath, i)
            except Exception as e:
                logging.error(e)
                logging.error(filepath)
                beam.metrics.Metrics.counter('results', "download-error").inc()
                return
            beam.metrics.Metrics.counter('results', "rf-downloaded").inc()
            yield file_num, data

        def _check_size(job):
            file_num, rf = job
            rf = list(rf)
            return len(rf) == 85

        def _process(job):
            file_num, rf = tuple(job)

            metadata_filepath = '{}/results/val_{}/structs_42.mat'.format(_BUCKET, file_num)
            target_jpeg_filepath = '{}/images/val_{}.JPEG'.format(_BUCKET, file_num+5000)
            body_jpeg_filepath = '{}/images/val_{}.JPEG'.format(_BUCKET, file_num)

            m = h5py.File(tf.io.gfile.GFile(metadata_filepath, 'rb'), mode='r')
            elements = m.get('/xdc/out')[()].shape[-1]
            on_elements = [np.arange(i,_SUB_APERTURE_SIZE+i, dtype=np.int64) for i in range(len(_TX_POS))]
            tx_delays = np.zeros((len(_TX_POS), elements))
            for i, on_ele in enumerate(on_elements): tx_delays[i, on_ele] = np.squeeze(m.get('xdc/delays'))[()]

            on_bool = np.zeros((len(_TX_POS), elements))
            for i, on_ele in enumerate(on_elements): on_bool[i, on_ele] = np.ones(_SUB_APERTURE_SIZE)
            on_bool = on_bool.astype(bool)

            common = {
                'c': np.squeeze(m.get('acq_params/c')[()]),
                'fs': np.squeeze(m.get('acq_params/fs')[()]),
                'tiny_imagenet': {
                    'target_number': file_num+5000,
                    'body_wall_number': file_num,
                    'target': target_jpeg_filepath,
                    'clutter_wall': body_jpeg_filepath
                },
                'probe': {
                    'tx_delays': tx_delays,
                    'element_on_mask': on_bool,
                    'element_positions': np.transpose(m.get('xdc/out')[()]),
                    'rx_positions': np.transpose(m.get('xdc/out')[()]),
                    'tx_positions': np.transpose(np.stack([_TX_POS, np.zeros_like(_TX_POS), np.zeros_like(_TX_POS)])),
                    'impulse': np.squeeze(m.get('xdc/impulse')[()]),
                    'pulse': np.squeeze(m.get('xdc/pulse')[()]),
                    'excitation': np.squeeze(m.get('xdc/excitation')[()]),
                    'a': np.squeeze(m.get('bf_params/a')[()]),
                    'b': np.squeeze(m.get('bf_params/b')[()]),
                    'pitch': np.squeeze(m.get('xdc/pitch')[()]),
                    't0': np.squeeze(m.get('xdc/t0')[()]),
                    'f0_hz': np.squeeze(m.get('acq_params/f0')[()]),
                    'focus_depth': np.squeeze(m.get('xdc/focus')[()][2])
                },
                'sim': {
                    'B': np.squeeze(m.get('input_vars/B')[()]),
                    'cmap': np.squeeze(m.get('field_maps/cmap')[()]),
                    'atten': np.squeeze(m.get('input_vars/atten')[()]),
                    'cfl': np.squeeze(m.get('input_vars/cfl')[()]),
                    'ncycles': np.squeeze(m.get('input_vars/ncycles')[()]),
                    'omega0': np.squeeze(m.get('input_vars/omega0')[()]),
                    'p0': np.squeeze(m.get('input_vars/p0')[()]),
                    'ppw': np.squeeze(m.get('input_vars/ppw')[()]),
                    'rho': np.squeeze(m.get('input_vars/rho')[()]),
                    'td': np.squeeze(m.get('input_vars/td')[()]),
                    'v': np.squeeze(m.get('input_vars/v')[()]),
                    'grid': {
                        'dT': np.squeeze(m.get('grid_vars/dT')[()]),
                        'dY': np.squeeze(m.get('grid_vars/dY')[()]),
                        'dZ': np.squeeze(m.get('grid_vars/dZ')[()]),
                        'nT': np.squeeze(m.get('grid_vars/nT')[()]),
                        'nY': np.squeeze(m.get('grid_vars/nY')[()]),
                        'nZ': np.squeeze(m.get('grid_vars/nZ')[()]),
                        'wY': np.squeeze(m.get('input_vars/wY')[()]),
                        'wZ': np.squeeze(m.get('input_vars/wZ')[()]),
                    }
                }
            }

            a = common['probe']['a'].astype(np.float32)
            b = common['probe']['b'].astype(np.float32)
            fs = common['fs'].astype(np.float32)
            f0 = common['probe']['f0_hz'].astype(np.float32)

            rf = list(rf)
            ordering = np.array([r['i'] for r in rf])
            ordering = list(np.argsort(ordering))
            nowall = []
            wall = []
            for idx in ordering:
                nowall.append(rf[idx]['nowall'])
                wall.append(rf[idx]['wall'])
            nowall = np.stack(nowall)
            wall = np.stack(wall)
            rf = None
            nowall = signal.lfilter(b, a, nowall, axis=-1)
            wall = signal.lfilter(b, a, wall, axis=-1)

            if self.builder_config.name is 'channel':
                varying = {
                    'without_wall': nowall,
                    'with_wall': wall
                }

            if self.builder_config.name is 'iq_channel':
                nowall = self.tf_demodulate(nowall, fs, f0, axis=-1)
                wall = self.tf_demodulate(wall, fs, f0, axis=-1)

                varying = {
                    'without_wall_real': tf.cast(tf.math.real(nowall), tf.float16),
                    'without_wall_imag': tf.cast(tf.math.imag(nowall), tf.float16),
                    'with_wall_real': tf.cast(tf.math.real(wall), tf.float16),
                    'with_wall_imag': tf.cast(tf.math.imag(wall), tf.float16)
                }

            if self.builder_config.name is 'dynamic_rx_beamformed' or self.builder_config.name is 'b_mode' or self.builder_config.name is 'iq_dynamic_rx_beamformed':
                s = self.beamform_dynamic_rx(nowall.shape, 
                                             common['probe']['tx_positions'], 
                                             common['probe']['rx_positions'], 
                                             s0=common['probe']['t0']*common['fs'], 
                                             fs=common['fs'], data_dtype=tf.float64)
                s = tf.cast(s, tf.float32)
                nowall = self.apply_delays(s, nowall)[..., 3117:6234]
                wall = self.apply_delays(s, wall)[..., 3117:6234]

                if self.builder_config.name is 'iq_dynamic_rx_beamformed':
                    nowall = self.tf_demodulate(nowall, fs, f0, axis=-1)
                    wall = self.tf_demodulate(wall, fs, f0, axis=-1)

                varying = {
                    'without_wall_real': tf.cast(tf.math.real(nowall), tf.float16),
                    'without_wall_imag': tf.cast(tf.math.imag(nowall), tf.float16),
                    'with_wall_real': tf.cast(tf.math.real(wall), tf.float16),
                    'with_wall_imag': tf.cast(tf.math.imag(wall), tf.float16)
                }

            if self.builder_config.name is 'b_mode':
                on_mask = tf.cast(common['probe']['element_on_mask'][..., None], tf.float32)
                env = tf.abs(self.tf_hilbert(tf.reduce_sum(nowall*on_mask, axis=1), axis=-1))
                env = env/tf.reduce_max(env)
                nowall = self.tf_db(env)

                env = tf.abs(self.tf_hilbert(tf.reduce_sum(wall*on_mask, axis=1), axis=-1))
                env = env/tf.reduce_max(env)
                wall = self.tf_db(env)

                varying = {
                    'without_wall': tf.cast(nowall, tf.float16),
                    'with_wall': tf.cast(wall, tf.float16)
                }
            m.close()

            beam.metrics.Metrics.counter('results', "rf-processed").inc()
            yield file_num, {
                'data': varying,
                'params': common
            }

        return (
            pipeline
            | beam.Create(filepaths_rf)
            | beam.FlatMap(_download_rf)
            | beam.GroupByKey()
            | beam.Filter(_check_size)
            | beam.FlatMap(_process)
        )
