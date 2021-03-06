# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: showtime.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='showtime.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0eshowtime.proto\"\x0f\n\rEmptyShowtime\")\n\tTimesData\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12\x0e\n\x06movies\x18\x02 \x03(\t\"\x14\n\x04\x44\x61te\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t2a\n\x08Showtime\x12.\n\x0cGetListTimes\x12\x0e.EmptyShowtime\x1a\n.TimesData\"\x00\x30\x01\x12%\n\x0eGetTimesByDate\x12\x05.Date\x1a\n.TimesData\"\x00\x62\x06proto3'
)




_EMPTYSHOWTIME = _descriptor.Descriptor(
  name='EmptyShowtime',
  full_name='EmptyShowtime',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=33,
)


_TIMESDATA = _descriptor.Descriptor(
  name='TimesData',
  full_name='TimesData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='date', full_name='TimesData.date', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='movies', full_name='TimesData.movies', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=35,
  serialized_end=76,
)


_DATE = _descriptor.Descriptor(
  name='Date',
  full_name='Date',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='date', full_name='Date.date', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=78,
  serialized_end=98,
)

DESCRIPTOR.message_types_by_name['EmptyShowtime'] = _EMPTYSHOWTIME
DESCRIPTOR.message_types_by_name['TimesData'] = _TIMESDATA
DESCRIPTOR.message_types_by_name['Date'] = _DATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EmptyShowtime = _reflection.GeneratedProtocolMessageType('EmptyShowtime', (_message.Message,), {
  'DESCRIPTOR' : _EMPTYSHOWTIME,
  '__module__' : 'showtime_pb2'
  # @@protoc_insertion_point(class_scope:EmptyShowtime)
  })
_sym_db.RegisterMessage(EmptyShowtime)

TimesData = _reflection.GeneratedProtocolMessageType('TimesData', (_message.Message,), {
  'DESCRIPTOR' : _TIMESDATA,
  '__module__' : 'showtime_pb2'
  # @@protoc_insertion_point(class_scope:TimesData)
  })
_sym_db.RegisterMessage(TimesData)

Date = _reflection.GeneratedProtocolMessageType('Date', (_message.Message,), {
  'DESCRIPTOR' : _DATE,
  '__module__' : 'showtime_pb2'
  # @@protoc_insertion_point(class_scope:Date)
  })
_sym_db.RegisterMessage(Date)



_SHOWTIME = _descriptor.ServiceDescriptor(
  name='Showtime',
  full_name='Showtime',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=100,
  serialized_end=197,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetListTimes',
    full_name='Showtime.GetListTimes',
    index=0,
    containing_service=None,
    input_type=_EMPTYSHOWTIME,
    output_type=_TIMESDATA,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetTimesByDate',
    full_name='Showtime.GetTimesByDate',
    index=1,
    containing_service=None,
    input_type=_DATE,
    output_type=_TIMESDATA,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SHOWTIME)

DESCRIPTOR.services_by_name['Showtime'] = _SHOWTIME

# @@protoc_insertion_point(module_scope)
