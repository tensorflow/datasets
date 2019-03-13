from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets.human_pose import skeleton as s

s16 = s.Skeleton((
    (s.r_ankle, s.r_knee),
    (s.r_knee, s.r_hip),
    (s.r_hip, s.pelvis),
    (s.l_hip, s.pelvis),
    (s.l_knee, s.l_hip),
    (s.l_ankle, s.l_knee),
    (s.pelvis, None),
    (s.thorax, s.pelvis),
    (s.neck, s.thorax),
    (s.head_back, s.neck),
    (s.r_wrist, s.r_elbow),
    (s.r_elbow, s.r_shoulder),
    (s.r_shoulder, s.neck),
    (s.l_shoulder, s.neck),
    (s.l_elbow, s.l_shoulder),
    (s.l_wrist, s.l_elbow),
), name="mpii_s16")
