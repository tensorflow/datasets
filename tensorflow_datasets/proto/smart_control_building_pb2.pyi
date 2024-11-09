from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ActionRequest(_message.Message):
    __slots__ = ["single_action_requests", "timestamp"]
    SINGLE_ACTION_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    single_action_requests: _containers.RepeatedCompositeFieldContainer[SingleActionRequest]
    timestamp: _timestamp_pb2.Timestamp
    def __init__(self, timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., single_action_requests: _Optional[_Iterable[_Union[SingleActionRequest, _Mapping]]] = ...) -> None: ...

class ActionResponse(_message.Message):
    __slots__ = ["request", "single_action_responses", "timestamp"]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    SINGLE_ACTION_RESPONSES_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    request: ActionRequest
    single_action_responses: _containers.RepeatedCompositeFieldContainer[SingleActionResponse]
    timestamp: _timestamp_pb2.Timestamp
    def __init__(self, timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., request: _Optional[_Union[ActionRequest, _Mapping]] = ..., single_action_responses: _Optional[_Iterable[_Union[SingleActionResponse, _Mapping]]] = ...) -> None: ...

class DeviceInfo(_message.Message):
    __slots__ = ["action_fields", "code", "device_id", "device_type", "namespace", "observable_fields", "zone_id"]
    class DeviceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class ValueType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class ActionFieldsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: DeviceInfo.ValueType
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[DeviceInfo.ValueType, str]] = ...) -> None: ...
    class ObservableFieldsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: DeviceInfo.ValueType
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[DeviceInfo.ValueType, str]] = ...) -> None: ...
    AC: DeviceInfo.DeviceType
    ACTION_FIELDS_FIELD_NUMBER: _ClassVar[int]
    AHU: DeviceInfo.DeviceType
    BLR: DeviceInfo.DeviceType
    CDWS: DeviceInfo.DeviceType
    CH: DeviceInfo.DeviceType
    CHWS: DeviceInfo.DeviceType
    CODE_FIELD_NUMBER: _ClassVar[int]
    CT: DeviceInfo.DeviceType
    DC: DeviceInfo.DeviceType
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    DFR: DeviceInfo.DeviceType
    DH: DeviceInfo.DeviceType
    DMP: DeviceInfo.DeviceType
    FAN: DeviceInfo.DeviceType
    FCU: DeviceInfo.DeviceType
    GAS: DeviceInfo.DeviceType
    HWS: DeviceInfo.DeviceType
    HX: DeviceInfo.DeviceType
    MAU: DeviceInfo.DeviceType
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    OBSERVABLE_FIELDS_FIELD_NUMBER: _ClassVar[int]
    OTHER: DeviceInfo.DeviceType
    PMP: DeviceInfo.DeviceType
    PWR: DeviceInfo.DeviceType
    SDC: DeviceInfo.DeviceType
    UH: DeviceInfo.DeviceType
    UNDEFINED: DeviceInfo.DeviceType
    VALUE_BINARY: DeviceInfo.ValueType
    VALUE_CATEGORICAL: DeviceInfo.ValueType
    VALUE_CONTINUOUS: DeviceInfo.ValueType
    VALUE_INTEGER: DeviceInfo.ValueType
    VALUE_TYPE_UNDEFINED: DeviceInfo.ValueType
    VAV: DeviceInfo.DeviceType
    ZONE_ID_FIELD_NUMBER: _ClassVar[int]
    action_fields: _containers.ScalarMap[str, DeviceInfo.ValueType]
    code: str
    device_id: str
    device_type: DeviceInfo.DeviceType
    namespace: str
    observable_fields: _containers.ScalarMap[str, DeviceInfo.ValueType]
    zone_id: str
    def __init__(self, device_id: _Optional[str] = ..., namespace: _Optional[str] = ..., code: _Optional[str] = ..., zone_id: _Optional[str] = ..., device_type: _Optional[_Union[DeviceInfo.DeviceType, str]] = ..., observable_fields: _Optional[_Mapping[str, DeviceInfo.ValueType]] = ..., action_fields: _Optional[_Mapping[str, DeviceInfo.ValueType]] = ...) -> None: ...

class ObservationRequest(_message.Message):
    __slots__ = ["single_observation_requests", "timestamp"]
    SINGLE_OBSERVATION_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    single_observation_requests: _containers.RepeatedCompositeFieldContainer[SingleObservationRequest]
    timestamp: _timestamp_pb2.Timestamp
    def __init__(self, timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., single_observation_requests: _Optional[_Iterable[_Union[SingleObservationRequest, _Mapping]]] = ...) -> None: ...

class ObservationResponse(_message.Message):
    __slots__ = ["request", "single_observation_responses", "timestamp"]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    SINGLE_OBSERVATION_RESPONSES_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    request: ObservationRequest
    single_observation_responses: _containers.RepeatedCompositeFieldContainer[SingleObservationResponse]
    timestamp: _timestamp_pb2.Timestamp
    def __init__(self, timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., request: _Optional[_Union[ObservationRequest, _Mapping]] = ..., single_observation_responses: _Optional[_Iterable[_Union[SingleObservationResponse, _Mapping]]] = ...) -> None: ...

class SingleActionRequest(_message.Message):
    __slots__ = ["binary_value", "categorical_value", "continuous_value", "device_id", "integer_value", "setpoint_name", "string_value"]
    BINARY_VALUE_FIELD_NUMBER: _ClassVar[int]
    CATEGORICAL_VALUE_FIELD_NUMBER: _ClassVar[int]
    CONTINUOUS_VALUE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    INTEGER_VALUE_FIELD_NUMBER: _ClassVar[int]
    SETPOINT_NAME_FIELD_NUMBER: _ClassVar[int]
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    binary_value: bool
    categorical_value: str
    continuous_value: float
    device_id: str
    integer_value: int
    setpoint_name: str
    string_value: str
    def __init__(self, device_id: _Optional[str] = ..., setpoint_name: _Optional[str] = ..., continuous_value: _Optional[float] = ..., integer_value: _Optional[int] = ..., categorical_value: _Optional[str] = ..., binary_value: bool = ..., string_value: _Optional[str] = ...) -> None: ...

class SingleActionResponse(_message.Message):
    __slots__ = ["additional_info", "request", "response_type"]
    class ActionResponseType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ACCEPTED: SingleActionResponse.ActionResponseType
    ADDITIONAL_INFO_FIELD_NUMBER: _ClassVar[int]
    OTHER: SingleActionResponse.ActionResponseType
    PENDING: SingleActionResponse.ActionResponseType
    REJECTED_DEVICE_OFFLINE: SingleActionResponse.ActionResponseType
    REJECTED_INVALID_DEVICE: SingleActionResponse.ActionResponseType
    REJECTED_INVALID_SETTING: SingleActionResponse.ActionResponseType
    REJECTED_NOT_ENABLED_OR_AVAILABLE: SingleActionResponse.ActionResponseType
    REJECTED_OVERRIDE: SingleActionResponse.ActionResponseType
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_TYPE_FIELD_NUMBER: _ClassVar[int]
    TIMED_OUT: SingleActionResponse.ActionResponseType
    UNDEFINED: SingleActionResponse.ActionResponseType
    UNKNOWN: SingleActionResponse.ActionResponseType
    additional_info: str
    request: SingleActionRequest
    response_type: SingleActionResponse.ActionResponseType
    def __init__(self, request: _Optional[_Union[SingleActionRequest, _Mapping]] = ..., response_type: _Optional[_Union[SingleActionResponse.ActionResponseType, str]] = ..., additional_info: _Optional[str] = ...) -> None: ...

class SingleObservationRequest(_message.Message):
    __slots__ = ["device_id", "measurement_name"]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    MEASUREMENT_NAME_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    measurement_name: str
    def __init__(self, device_id: _Optional[str] = ..., measurement_name: _Optional[str] = ...) -> None: ...

class SingleObservationResponse(_message.Message):
    __slots__ = ["binary_value", "categorical_value", "continuous_value", "integer_value", "observation_valid", "single_observation_request", "string_value", "timestamp"]
    BINARY_VALUE_FIELD_NUMBER: _ClassVar[int]
    CATEGORICAL_VALUE_FIELD_NUMBER: _ClassVar[int]
    CONTINUOUS_VALUE_FIELD_NUMBER: _ClassVar[int]
    INTEGER_VALUE_FIELD_NUMBER: _ClassVar[int]
    OBSERVATION_VALID_FIELD_NUMBER: _ClassVar[int]
    SINGLE_OBSERVATION_REQUEST_FIELD_NUMBER: _ClassVar[int]
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    binary_value: bool
    categorical_value: str
    continuous_value: float
    integer_value: int
    observation_valid: bool
    single_observation_request: SingleObservationRequest
    string_value: str
    timestamp: _timestamp_pb2.Timestamp
    def __init__(self, timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., single_observation_request: _Optional[_Union[SingleObservationRequest, _Mapping]] = ..., observation_valid: bool = ..., continuous_value: _Optional[float] = ..., integer_value: _Optional[int] = ..., categorical_value: _Optional[str] = ..., binary_value: bool = ..., string_value: _Optional[str] = ...) -> None: ...

class ZoneInfo(_message.Message):
    __slots__ = ["area", "building_id", "devices", "floor", "zone_description", "zone_id", "zone_type"]
    class ZoneType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    AREA_FIELD_NUMBER: _ClassVar[int]
    BUILDING_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICES_FIELD_NUMBER: _ClassVar[int]
    FLOOR: ZoneInfo.ZoneType
    FLOOR_FIELD_NUMBER: _ClassVar[int]
    OTHER: ZoneInfo.ZoneType
    ROOM: ZoneInfo.ZoneType
    UNDEFINED: ZoneInfo.ZoneType
    ZONE_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ZONE_ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_TYPE_FIELD_NUMBER: _ClassVar[int]
    area: float
    building_id: str
    devices: _containers.RepeatedScalarFieldContainer[str]
    floor: int
    zone_description: str
    zone_id: str
    zone_type: ZoneInfo.ZoneType
    def __init__(self, zone_id: _Optional[str] = ..., building_id: _Optional[str] = ..., zone_description: _Optional[str] = ..., area: _Optional[float] = ..., devices: _Optional[_Iterable[str]] = ..., zone_type: _Optional[_Union[ZoneInfo.ZoneType, str]] = ..., floor: _Optional[int] = ...) -> None: ...
