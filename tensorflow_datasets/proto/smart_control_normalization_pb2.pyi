from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ContinuousVariableInfo(_message.Message):
    __slots__ = ["id", "sample_end", "sample_maximum", "sample_mean", "sample_median", "sample_minimum", "sample_size", "sample_start", "sample_variance"]
    ID_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_END_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_MAXIMUM_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_MEAN_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_MEDIAN_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_MINIMUM_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_SIZE_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_START_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_VARIANCE_FIELD_NUMBER: _ClassVar[int]
    id: str
    sample_end: _timestamp_pb2.Timestamp
    sample_maximum: float
    sample_mean: float
    sample_median: float
    sample_minimum: float
    sample_size: int
    sample_start: _timestamp_pb2.Timestamp
    sample_variance: float
    def __init__(self, id: _Optional[str] = ..., sample_start: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., sample_end: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., sample_size: _Optional[int] = ..., sample_variance: _Optional[float] = ..., sample_mean: _Optional[float] = ..., sample_median: _Optional[float] = ..., sample_maximum: _Optional[float] = ..., sample_minimum: _Optional[float] = ...) -> None: ...
