# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nodeb_info.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import gnb_pb2 as gnb__pb2
from . import enb_pb2 as enb__pb2
from . import x2_setup_failure_response_pb2 as x2__setup__failure__response__pb2
from . import nb_identity_pb2 as nb__identity__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='nodeb_info.proto',
  package='entities',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x10nodeb_info.proto\x12\x08\x65ntities\x1a\tgnb.proto\x1a\tenb.proto\x1a\x1fx2_setup_failure_response.proto\x1a\x11nb_identity.proto\"\xf3\x03\n\tNodebInfo\x12\x10\n\x08ran_name\x18\x01 \x01(\t\x12\n\n\x02ip\x18\x02 \x01(\t\x12\x0c\n\x04port\x18\x03 \x01(\r\x12@\n\x17\x65\x32_application_protocol\x18\x04 \x01(\x0e\x32\x1f.entities.E2ApplicationProtocol\x12\x35\n\x11\x63onnection_status\x18\x05 \x01(\x0e\x32\x1a.entities.ConnectionStatus\x12*\n\x0cglobal_nb_id\x18\x06 \x01(\x0b\x32\x14.entities.GlobalNbId\x12&\n\tnode_type\x18\x07 \x01(\x0e\x32\x13.entities.Node.Type\x12\x1c\n\x03\x65nb\x18\x08 \x01(\x0b\x32\r.entities.EnbH\x00\x12\x1c\n\x03gnb\x18\t \x01(\x0b\x32\r.entities.GnbH\x00\x12,\n\x0c\x66\x61ilure_type\x18\n \x01(\x0e\x32\x16.entities.Failure.Type\x12-\n\rsetup_failure\x18\x0b \x01(\x0b\x32\x16.entities.SetupFailure\x12\'\n\x1f\x61ssociated_e2t_instance_address\x18\x0c \x01(\t\x12\x1a\n\x12setup_from_network\x18\r \x01(\x08\x42\x0f\n\rconfiguration\"-\n\x04Node\"%\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x07\n\x03\x45NB\x10\x01\x12\x07\n\x03GNB\x10\x02\"T\n\x07\x46\x61ilure\"I\n\x04Type\x12\x10\n\x0cUNKNOWN_TYPE\x10\x00\x12\x14\n\x10X2_SETUP_FAILURE\x10\x01\x12\x19\n\x15\x45NDC_X2_SETUP_FAILURE\x10\x02*m\n\x15\x45\x32\x41pplicationProtocol\x12#\n\x1fUNKNOWN_E2_APPLICATION_PROTOCOL\x10\x00\x12\x14\n\x10X2_SETUP_REQUEST\x10\x01\x12\x19\n\x15\x45NDC_X2_SETUP_REQUEST\x10\x02\x62\x06proto3')
  ,
  dependencies=[gnb__pb2.DESCRIPTOR,enb__pb2.DESCRIPTOR,x2__setup__failure__response__pb2.DESCRIPTOR,nb__identity__pb2.DESCRIPTOR,])

_E2APPLICATIONPROTOCOL = _descriptor.EnumDescriptor(
  name='E2ApplicationProtocol',
  full_name='entities.E2ApplicationProtocol',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_E2_APPLICATION_PROTOCOL', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='X2_SETUP_REQUEST', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENDC_X2_SETUP_REQUEST', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=739,
  serialized_end=848,
)
_sym_db.RegisterEnumDescriptor(_E2APPLICATIONPROTOCOL)

E2ApplicationProtocol = enum_type_wrapper.EnumTypeWrapper(_E2APPLICATIONPROTOCOL)
UNKNOWN_E2_APPLICATION_PROTOCOL = 0
X2_SETUP_REQUEST = 1
ENDC_X2_SETUP_REQUEST = 2


_NODE_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='entities.Node.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENB', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GNB', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=614,
  serialized_end=651,
)
_sym_db.RegisterEnumDescriptor(_NODE_TYPE)

_FAILURE_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='entities.Failure.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_TYPE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='X2_SETUP_FAILURE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENDC_X2_SETUP_FAILURE', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=664,
  serialized_end=737,
)
_sym_db.RegisterEnumDescriptor(_FAILURE_TYPE)


_NODEBINFO = _descriptor.Descriptor(
  name='NodebInfo',
  full_name='entities.NodebInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ran_name', full_name='entities.NodebInfo.ran_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ip', full_name='entities.NodebInfo.ip', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port', full_name='entities.NodebInfo.port', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='e2_application_protocol', full_name='entities.NodebInfo.e2_application_protocol', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='connection_status', full_name='entities.NodebInfo.connection_status', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='global_nb_id', full_name='entities.NodebInfo.global_nb_id', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='node_type', full_name='entities.NodebInfo.node_type', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enb', full_name='entities.NodebInfo.enb', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gnb', full_name='entities.NodebInfo.gnb', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='failure_type', full_name='entities.NodebInfo.failure_type', index=9,
      number=10, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='setup_failure', full_name='entities.NodebInfo.setup_failure', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='associated_e2t_instance_address', full_name='entities.NodebInfo.associated_e2t_instance_address', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='setup_from_network', full_name='entities.NodebInfo.setup_from_network', index=12,
      number=13, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
    _descriptor.OneofDescriptor(
      name='configuration', full_name='entities.NodebInfo.configuration',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=105,
  serialized_end=604,
)


_NODE = _descriptor.Descriptor(
  name='Node',
  full_name='entities.Node',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _NODE_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=606,
  serialized_end=651,
)


_FAILURE = _descriptor.Descriptor(
  name='Failure',
  full_name='entities.Failure',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _FAILURE_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=653,
  serialized_end=737,
)

_NODEBINFO.fields_by_name['e2_application_protocol'].enum_type = _E2APPLICATIONPROTOCOL
_NODEBINFO.fields_by_name['connection_status'].enum_type = nb__identity__pb2._CONNECTIONSTATUS
_NODEBINFO.fields_by_name['global_nb_id'].message_type = nb__identity__pb2._GLOBALNBID
_NODEBINFO.fields_by_name['node_type'].enum_type = _NODE_TYPE
_NODEBINFO.fields_by_name['enb'].message_type = enb__pb2._ENB
_NODEBINFO.fields_by_name['gnb'].message_type = gnb__pb2._GNB
_NODEBINFO.fields_by_name['failure_type'].enum_type = _FAILURE_TYPE
_NODEBINFO.fields_by_name['setup_failure'].message_type = x2__setup__failure__response__pb2._SETUPFAILURE
_NODEBINFO.oneofs_by_name['configuration'].fields.append(
  _NODEBINFO.fields_by_name['enb'])
_NODEBINFO.fields_by_name['enb'].containing_oneof = _NODEBINFO.oneofs_by_name['configuration']
_NODEBINFO.oneofs_by_name['configuration'].fields.append(
  _NODEBINFO.fields_by_name['gnb'])
_NODEBINFO.fields_by_name['gnb'].containing_oneof = _NODEBINFO.oneofs_by_name['configuration']
_NODE_TYPE.containing_type = _NODE
_FAILURE_TYPE.containing_type = _FAILURE
DESCRIPTOR.message_types_by_name['NodebInfo'] = _NODEBINFO
DESCRIPTOR.message_types_by_name['Node'] = _NODE
DESCRIPTOR.message_types_by_name['Failure'] = _FAILURE
DESCRIPTOR.enum_types_by_name['E2ApplicationProtocol'] = _E2APPLICATIONPROTOCOL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NodebInfo = _reflection.GeneratedProtocolMessageType('NodebInfo', (_message.Message,), {
  'DESCRIPTOR' : _NODEBINFO,
  '__module__' : 'nodeb_info_pb2'
  # @@protoc_insertion_point(class_scope:entities.NodebInfo)
  })
_sym_db.RegisterMessage(NodebInfo)

Node = _reflection.GeneratedProtocolMessageType('Node', (_message.Message,), {
  'DESCRIPTOR' : _NODE,
  '__module__' : 'nodeb_info_pb2'
  # @@protoc_insertion_point(class_scope:entities.Node)
  })
_sym_db.RegisterMessage(Node)

Failure = _reflection.GeneratedProtocolMessageType('Failure', (_message.Message,), {
  'DESCRIPTOR' : _FAILURE,
  '__module__' : 'nodeb_info_pb2'
  # @@protoc_insertion_point(class_scope:entities.Failure)
  })
_sym_db.RegisterMessage(Failure)


# @@protoc_insertion_point(module_scope)
