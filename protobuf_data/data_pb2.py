# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: data.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='data.proto',
  package='protobuf_data',
  syntax='proto3',
  serialized_pb=_b('\n\ndata.proto\x12\rprotobuf_data\"\x14\n\x04\x44\x61ta\x12\x0c\n\x04text\x18\x01 \x01(\t2D\n\nFormatData\x12\x36\n\x08\x44oFormat\x12\x13.protobuf_data.Data\x1a\x13.protobuf_data.Data\"\x00\x62\x06proto3')
)




_DATA = _descriptor.Descriptor(
  name='Data',
  full_name='protobuf_data.Data',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='protobuf_data.Data.text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=29,
  serialized_end=49,
)

DESCRIPTOR.message_types_by_name['Data'] = _DATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Data = _reflection.GeneratedProtocolMessageType('Data', (_message.Message,), dict(
  DESCRIPTOR = _DATA,
  __module__ = 'data_pb2'
  # @@protoc_insertion_point(class_scope:protobuf_data.Data)
  ))
_sym_db.RegisterMessage(Data)



_FORMATDATA = _descriptor.ServiceDescriptor(
  name='FormatData',
  full_name='protobuf_data.FormatData',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=51,
  serialized_end=119,
  methods=[
  _descriptor.MethodDescriptor(
    name='DoFormat',
    full_name='protobuf_data.FormatData.DoFormat',
    index=0,
    containing_service=None,
    input_type=_DATA,
    output_type=_DATA,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_FORMATDATA)

DESCRIPTOR.services_by_name['FormatData'] = _FORMATDATA

# @@protoc_insertion_point(module_scope)
