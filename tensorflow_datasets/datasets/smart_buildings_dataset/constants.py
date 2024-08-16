# coding=utf-8
# Copyright 2024 The TensorFlow Datasets Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Single location for all constants related to the simulation and RL environment.

Copyright 2022 Google LLC

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

# --------- Thermal Constants ---------------

AIR_HEAT_CAPACITY = 1006.0  # J/kg/K, standard atmosphere
WATER_HEAT_CAPACITY = 4180.0  # J/kg/K
WATER_VAPOR_HEAT_CAPACITY = 1863.8  # J/kg/K

# --------- Energy Constants ---------------
BTU_PER_KWH: float = 3412.4
JOULES_PER_KWH: float = 3.6e6
JOULES_PER_BTU: float = 1055.06
W_PER_KW: float = 1000.0  # Number of Watts in a kW.
WATTS_PER_BTU_HR: float = 0.29307107  # Number of Watts in a BTU/hr
HZ_PERCENT: float = 100.0 / 60.0  # Converts blower/pump Hz to Percentage Power

# https://www.rapidtables.com/convert/power/hp-to-watt.html
WATTS_PER_HORSEPOWER = 746.0

# Natural gas energy conversion.
# Sources:
# http://www.kylesconverter.com/energy,-work,-and-heat/kilowatt--hours-to-cubic-feet-of-natural-gas#293.07
# https://www.traditionaloven.com/tutorials/energy/convert-cubic-foot-natural-gas-to-kilo-watt-hr-kwh.html
KWH_PER_KFT3_GAS = 293.07107  # kWh / 1000 cubic feet natural gas

# Natural gas CO2 emission.
# Source: https://www.eia.gov/environment/emissions/co2_vol_mass.php
GAS_CO2 = 53.12  # kg/1000 cubic feet

WATER_DENSITY = 1000.0  # kg/m3
GRAVITY = 9.8  # m/s2

# ------------ File Name Convention -----------------
NORMALIZATION_FILENAME = 'normalization_info'
OBSERVATION_RESPONSE_FILE_PREFIX = 'observation_response'
ACTION_RESPONSE_FILE_PREFIX = 'action_response'
IMAGES_DIR = 'images'
BUILDING_IMAGE_CSV_FILE = 'building_images.csv'
REWARD_INFO_PREFIX = 'reward_info'
REWARD_RESPONSE_PREFIX = 'reward_response'
DEVICE_INFO_PREFIX = 'device_info'
ZONE_INFO_PREFIX = 'zone_info'
