# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: booking.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='booking.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rbooking.proto\"\x0e\n\x0c\x45mptyBooking\"o\n\x0b\x42ookingData\x12\x0e\n\x06userid\x18\x01 \x01(\t\x12%\n\x05\x64\x61tes\x18\x02 \x03(\x0b\x32\x16.BookingData.datesData\x1a)\n\tdatesData\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12\x0e\n\x06movies\x18\x02 \x03(\t\"\x1f\n\rUserIDBooking\x12\x0e\n\x06userid\x18\x01 \x01(\t\"9\n\nnewBooking\x12\x0e\n\x06userid\x18\x01 \x01(\t\x12\r\n\x05movie\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x61te\x18\x03 \x01(\t\"3\n\x11returnInfoBooking\x12\r\n\x05\x65rror\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t2\x9f\x01\n\x07\x42ooking\x12,\n\x0bgetBookings\x12\r.EmptyBooking\x1a\x0c.BookingData0\x01\x12\x31\n\x11getBookingForUser\x12\x0e.UserIDBooking\x1a\x0c.BookingData\x12\x33\n\x10\x61\x64\x64\x42ookingByUser\x12\x0b.newBooking\x1a\x12.returnInfoBookingb\x06proto3'
)




_EMPTYBOOKING = _descriptor.Descriptor(
  name='EmptyBooking',
  full_name='EmptyBooking',
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
  serialized_start=17,
  serialized_end=31,
)


_BOOKINGDATA_DATESDATA = _descriptor.Descriptor(
  name='datesData',
  full_name='BookingData.datesData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='date', full_name='BookingData.datesData.date', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='movies', full_name='BookingData.datesData.movies', index=1,
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
  serialized_start=103,
  serialized_end=144,
)

_BOOKINGDATA = _descriptor.Descriptor(
  name='BookingData',
  full_name='BookingData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='userid', full_name='BookingData.userid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dates', full_name='BookingData.dates', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_BOOKINGDATA_DATESDATA, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=144,
)


_USERIDBOOKING = _descriptor.Descriptor(
  name='UserIDBooking',
  full_name='UserIDBooking',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='userid', full_name='UserIDBooking.userid', index=0,
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
  serialized_start=146,
  serialized_end=177,
)


_NEWBOOKING = _descriptor.Descriptor(
  name='newBooking',
  full_name='newBooking',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='userid', full_name='newBooking.userid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='movie', full_name='newBooking.movie', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='date', full_name='newBooking.date', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=179,
  serialized_end=236,
)


_RETURNINFOBOOKING = _descriptor.Descriptor(
  name='returnInfoBooking',
  full_name='returnInfoBooking',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='error', full_name='returnInfoBooking.error', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='returnInfoBooking.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=238,
  serialized_end=289,
)

_BOOKINGDATA_DATESDATA.containing_type = _BOOKINGDATA
_BOOKINGDATA.fields_by_name['dates'].message_type = _BOOKINGDATA_DATESDATA
DESCRIPTOR.message_types_by_name['EmptyBooking'] = _EMPTYBOOKING
DESCRIPTOR.message_types_by_name['BookingData'] = _BOOKINGDATA
DESCRIPTOR.message_types_by_name['UserIDBooking'] = _USERIDBOOKING
DESCRIPTOR.message_types_by_name['newBooking'] = _NEWBOOKING
DESCRIPTOR.message_types_by_name['returnInfoBooking'] = _RETURNINFOBOOKING
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EmptyBooking = _reflection.GeneratedProtocolMessageType('EmptyBooking', (_message.Message,), {
  'DESCRIPTOR' : _EMPTYBOOKING,
  '__module__' : 'booking_pb2'
  # @@protoc_insertion_point(class_scope:EmptyBooking)
  })
_sym_db.RegisterMessage(EmptyBooking)

BookingData = _reflection.GeneratedProtocolMessageType('BookingData', (_message.Message,), {

  'datesData' : _reflection.GeneratedProtocolMessageType('datesData', (_message.Message,), {
    'DESCRIPTOR' : _BOOKINGDATA_DATESDATA,
    '__module__' : 'booking_pb2'
    # @@protoc_insertion_point(class_scope:BookingData.datesData)
    })
  ,
  'DESCRIPTOR' : _BOOKINGDATA,
  '__module__' : 'booking_pb2'
  # @@protoc_insertion_point(class_scope:BookingData)
  })
_sym_db.RegisterMessage(BookingData)
_sym_db.RegisterMessage(BookingData.datesData)

UserIDBooking = _reflection.GeneratedProtocolMessageType('UserIDBooking', (_message.Message,), {
  'DESCRIPTOR' : _USERIDBOOKING,
  '__module__' : 'booking_pb2'
  # @@protoc_insertion_point(class_scope:UserIDBooking)
  })
_sym_db.RegisterMessage(UserIDBooking)

newBooking = _reflection.GeneratedProtocolMessageType('newBooking', (_message.Message,), {
  'DESCRIPTOR' : _NEWBOOKING,
  '__module__' : 'booking_pb2'
  # @@protoc_insertion_point(class_scope:newBooking)
  })
_sym_db.RegisterMessage(newBooking)

returnInfoBooking = _reflection.GeneratedProtocolMessageType('returnInfoBooking', (_message.Message,), {
  'DESCRIPTOR' : _RETURNINFOBOOKING,
  '__module__' : 'booking_pb2'
  # @@protoc_insertion_point(class_scope:returnInfoBooking)
  })
_sym_db.RegisterMessage(returnInfoBooking)



_BOOKING = _descriptor.ServiceDescriptor(
  name='Booking',
  full_name='Booking',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=292,
  serialized_end=451,
  methods=[
  _descriptor.MethodDescriptor(
    name='getBookings',
    full_name='Booking.getBookings',
    index=0,
    containing_service=None,
    input_type=_EMPTYBOOKING,
    output_type=_BOOKINGDATA,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='getBookingForUser',
    full_name='Booking.getBookingForUser',
    index=1,
    containing_service=None,
    input_type=_USERIDBOOKING,
    output_type=_BOOKINGDATA,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='addBookingByUser',
    full_name='Booking.addBookingByUser',
    index=2,
    containing_service=None,
    input_type=_NEWBOOKING,
    output_type=_RETURNINFOBOOKING,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_BOOKING)

DESCRIPTOR.services_by_name['Booking'] = _BOOKING

# @@protoc_insertion_point(module_scope)
