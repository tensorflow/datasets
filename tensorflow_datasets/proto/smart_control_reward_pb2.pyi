from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RewardInfo(_message.Message):
    __slots__ = ["agent_id", "air_handler_reward_infos", "boiler_reward_infos", "end_timestamp", "scenario_id", "start_timestamp", "zone_reward_infos"]
    class AirHandlerRewardInfo(_message.Message):
        __slots__ = ["air_conditioning_electrical_energy_rate", "blower_electrical_energy_rate"]
        AIR_CONDITIONING_ELECTRICAL_ENERGY_RATE_FIELD_NUMBER: _ClassVar[int]
        BLOWER_ELECTRICAL_ENERGY_RATE_FIELD_NUMBER: _ClassVar[int]
        air_conditioning_electrical_energy_rate: float
        blower_electrical_energy_rate: float
        def __init__(self, blower_electrical_energy_rate: _Optional[float] = ..., air_conditioning_electrical_energy_rate: _Optional[float] = ...) -> None: ...
    class AirHandlerRewardInfosEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: RewardInfo.AirHandlerRewardInfo
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[RewardInfo.AirHandlerRewardInfo, _Mapping]] = ...) -> None: ...
    class BoilerRewardInfo(_message.Message):
        __slots__ = ["natural_gas_heating_energy_rate", "pump_electrical_energy_rate"]
        NATURAL_GAS_HEATING_ENERGY_RATE_FIELD_NUMBER: _ClassVar[int]
        PUMP_ELECTRICAL_ENERGY_RATE_FIELD_NUMBER: _ClassVar[int]
        natural_gas_heating_energy_rate: float
        pump_electrical_energy_rate: float
        def __init__(self, natural_gas_heating_energy_rate: _Optional[float] = ..., pump_electrical_energy_rate: _Optional[float] = ...) -> None: ...
    class BoilerRewardInfosEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: RewardInfo.BoilerRewardInfo
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[RewardInfo.BoilerRewardInfo, _Mapping]] = ...) -> None: ...
    class ZoneRewardInfo(_message.Message):
        __slots__ = ["air_flow_rate", "air_flow_rate_setpoint", "average_occupancy", "cooling_setpoint_temperature", "heating_setpoint_temperature", "zone_air_temperature"]
        AIR_FLOW_RATE_FIELD_NUMBER: _ClassVar[int]
        AIR_FLOW_RATE_SETPOINT_FIELD_NUMBER: _ClassVar[int]
        AVERAGE_OCCUPANCY_FIELD_NUMBER: _ClassVar[int]
        COOLING_SETPOINT_TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
        HEATING_SETPOINT_TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
        ZONE_AIR_TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
        air_flow_rate: float
        air_flow_rate_setpoint: float
        average_occupancy: float
        cooling_setpoint_temperature: float
        heating_setpoint_temperature: float
        zone_air_temperature: float
        def __init__(self, heating_setpoint_temperature: _Optional[float] = ..., cooling_setpoint_temperature: _Optional[float] = ..., zone_air_temperature: _Optional[float] = ..., air_flow_rate_setpoint: _Optional[float] = ..., air_flow_rate: _Optional[float] = ..., average_occupancy: _Optional[float] = ...) -> None: ...
    class ZoneRewardInfosEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: RewardInfo.ZoneRewardInfo
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[RewardInfo.ZoneRewardInfo, _Mapping]] = ...) -> None: ...
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    AIR_HANDLER_REWARD_INFOS_FIELD_NUMBER: _ClassVar[int]
    BOILER_REWARD_INFOS_FIELD_NUMBER: _ClassVar[int]
    END_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    SCENARIO_ID_FIELD_NUMBER: _ClassVar[int]
    START_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ZONE_REWARD_INFOS_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    air_handler_reward_infos: _containers.MessageMap[str, RewardInfo.AirHandlerRewardInfo]
    boiler_reward_infos: _containers.MessageMap[str, RewardInfo.BoilerRewardInfo]
    end_timestamp: _timestamp_pb2.Timestamp
    scenario_id: str
    start_timestamp: _timestamp_pb2.Timestamp
    zone_reward_infos: _containers.MessageMap[str, RewardInfo.ZoneRewardInfo]
    def __init__(self, start_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., agent_id: _Optional[str] = ..., scenario_id: _Optional[str] = ..., zone_reward_infos: _Optional[_Mapping[str, RewardInfo.ZoneRewardInfo]] = ..., air_handler_reward_infos: _Optional[_Mapping[str, RewardInfo.AirHandlerRewardInfo]] = ..., boiler_reward_infos: _Optional[_Mapping[str, RewardInfo.BoilerRewardInfo]] = ...) -> None: ...

class RewardResponse(_message.Message):
    __slots__ = ["agent_reward_value", "carbon_cost", "carbon_emission_weight", "carbon_emitted", "electricity_energy_cost", "end_timestamp", "energy_cost_weight", "natural_gas_energy_cost", "normalized_carbon_emission", "normalized_energy_cost", "normalized_productivity_regret", "person_productivity", "productivity_regret", "productivity_reward", "productivity_weight", "reward_scale", "reward_shift", "start_timestamp", "total_occupancy"]
    AGENT_REWARD_VALUE_FIELD_NUMBER: _ClassVar[int]
    CARBON_COST_FIELD_NUMBER: _ClassVar[int]
    CARBON_EMISSION_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    CARBON_EMITTED_FIELD_NUMBER: _ClassVar[int]
    ELECTRICITY_ENERGY_COST_FIELD_NUMBER: _ClassVar[int]
    END_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ENERGY_COST_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    NATURAL_GAS_ENERGY_COST_FIELD_NUMBER: _ClassVar[int]
    NORMALIZED_CARBON_EMISSION_FIELD_NUMBER: _ClassVar[int]
    NORMALIZED_ENERGY_COST_FIELD_NUMBER: _ClassVar[int]
    NORMALIZED_PRODUCTIVITY_REGRET_FIELD_NUMBER: _ClassVar[int]
    PERSON_PRODUCTIVITY_FIELD_NUMBER: _ClassVar[int]
    PRODUCTIVITY_REGRET_FIELD_NUMBER: _ClassVar[int]
    PRODUCTIVITY_REWARD_FIELD_NUMBER: _ClassVar[int]
    PRODUCTIVITY_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    REWARD_SCALE_FIELD_NUMBER: _ClassVar[int]
    REWARD_SHIFT_FIELD_NUMBER: _ClassVar[int]
    START_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TOTAL_OCCUPANCY_FIELD_NUMBER: _ClassVar[int]
    agent_reward_value: float
    carbon_cost: float
    carbon_emission_weight: float
    carbon_emitted: float
    electricity_energy_cost: float
    end_timestamp: _timestamp_pb2.Timestamp
    energy_cost_weight: float
    natural_gas_energy_cost: float
    normalized_carbon_emission: float
    normalized_energy_cost: float
    normalized_productivity_regret: float
    person_productivity: float
    productivity_regret: float
    productivity_reward: float
    productivity_weight: float
    reward_scale: float
    reward_shift: float
    start_timestamp: _timestamp_pb2.Timestamp
    total_occupancy: float
    def __init__(self, agent_reward_value: _Optional[float] = ..., productivity_reward: _Optional[float] = ..., electricity_energy_cost: _Optional[float] = ..., natural_gas_energy_cost: _Optional[float] = ..., carbon_emitted: _Optional[float] = ..., carbon_cost: _Optional[float] = ..., productivity_weight: _Optional[float] = ..., energy_cost_weight: _Optional[float] = ..., carbon_emission_weight: _Optional[float] = ..., person_productivity: _Optional[float] = ..., total_occupancy: _Optional[float] = ..., reward_scale: _Optional[float] = ..., reward_shift: _Optional[float] = ..., productivity_regret: _Optional[float] = ..., normalized_productivity_regret: _Optional[float] = ..., normalized_energy_cost: _Optional[float] = ..., normalized_carbon_emission: _Optional[float] = ..., start_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
