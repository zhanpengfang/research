# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: diplomacy_tensorflow/core/protobuf/checkpointable_object_graph.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='diplomacy_tensorflow/core/protobuf/checkpointable_object_graph.proto',
  package='diplomacy.tensorflow',
  syntax='proto3',
  serialized_options=_b('\370\001\001'),
  serialized_pb=_b('\nDdiplomacy_tensorflow/core/protobuf/checkpointable_object_graph.proto\x12\x14\x64iplomacy.tensorflow\"\xc3\x05\n\x19\x43heckpointableObjectGraph\x12S\n\x05nodes\x18\x01 \x03(\x0b\x32\x44.diplomacy.tensorflow.CheckpointableObjectGraph.CheckpointableObject\x1a\xd0\x04\n\x14\x43heckpointableObject\x12\x66\n\x08\x63hildren\x18\x01 \x03(\x0b\x32T.diplomacy.tensorflow.CheckpointableObjectGraph.CheckpointableObject.ObjectReference\x12i\n\nattributes\x18\x02 \x03(\x0b\x32U.diplomacy.tensorflow.CheckpointableObjectGraph.CheckpointableObject.SerializedTensor\x12r\n\x0eslot_variables\x18\x03 \x03(\x0b\x32Z.diplomacy.tensorflow.CheckpointableObjectGraph.CheckpointableObject.SlotVariableReference\x1a\x36\n\x0fObjectReference\x12\x0f\n\x07node_id\x18\x01 \x01(\x05\x12\x12\n\nlocal_name\x18\x02 \x01(\t\x1aK\n\x10SerializedTensor\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tfull_name\x18\x02 \x01(\t\x12\x16\n\x0e\x63heckpoint_key\x18\x03 \x01(\t\x1al\n\x15SlotVariableReference\x12!\n\x19original_variable_node_id\x18\x01 \x01(\x05\x12\x11\n\tslot_name\x18\x02 \x01(\t\x12\x1d\n\x15slot_variable_node_id\x18\x03 \x01(\x05\x42\x03\xf8\x01\x01\x62\x06proto3')
)




_CHECKPOINTABLEOBJECTGRAPH_CHECKPOINTABLEOBJECT_OBJECTREFERENCE = _descriptor.Descriptor(
  name='ObjectReference',
  full_name='diplomacy.tensorflow.CheckpointableObjectGraph.CheckpointableObject.ObjectReference',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='node_id', full_name='diplomacy.tensorflow.CheckpointableObjectGraph.CheckpointableObject.ObjectReference.node_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='local_name', full_name='diplomacy.tensorflow.CheckpointableObjectGraph.CheckpointableObject.ObjectReference.local_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  ],
  serialized_start=561,
  serialized_end=615,
)

_CHECKPOINTABLEOBJECTGRAPH_CHECKPOINTABLEOBJECT_SERIALIZEDTENSOR = _descriptor.Descriptor(
  name='SerializedTensor',
  full_name='diplomacy.tensorflow.CheckpointableObjectGraph.CheckpointableObject.SerializedTensor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='diplomacy.tensorflow.CheckpointableObjectGraph.CheckpointableObject.SerializedTensor.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='full_name', full_name='diplomacy.tensorflow.CheckpointableObjectGraph.CheckpointableObject.SerializedTensor.full_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='checkpoint_key', full_name='diplomacy.tensorflow.CheckpointableObjectGraph.CheckpointableObject.SerializedTensor.checkpoint_key', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  ],
  serialized_start=617,
  serialized_end=692,
)

_CHECKPOINTABLEOBJECTGRAPH_CHECKPOINTABLEOBJECT_SLOTVARIABLEREFERENCE = _descriptor.Descriptor(
  name='SlotVariableReference',
  full_name='diplomacy.tensorflow.CheckpointableObjectGraph.CheckpointableObject.SlotVariableReference',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='original_variable_node_id', full_name='diplomacy.tensorflow.CheckpointableObjectGraph.CheckpointableObject.SlotVariableReference.original_variable_node_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='slot_name', full_name='diplomacy.tensorflow.CheckpointableObjectGraph.CheckpointableObject.SlotVariableReference.slot_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='slot_variable_node_id', full_name='diplomacy.tensorflow.CheckpointableObjectGraph.CheckpointableObject.SlotVariableReference.slot_variable_node_id', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  ],
  serialized_start=694,
  serialized_end=802,
)

_CHECKPOINTABLEOBJECTGRAPH_CHECKPOINTABLEOBJECT = _descriptor.Descriptor(
  name='CheckpointableObject',
  full_name='diplomacy.tensorflow.CheckpointableObjectGraph.CheckpointableObject',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='children', full_name='diplomacy.tensorflow.CheckpointableObjectGraph.CheckpointableObject.children', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='diplomacy.tensorflow.CheckpointableObjectGraph.CheckpointableObject.attributes', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='slot_variables', full_name='diplomacy.tensorflow.CheckpointableObjectGraph.CheckpointableObject.slot_variables', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CHECKPOINTABLEOBJECTGRAPH_CHECKPOINTABLEOBJECT_OBJECTREFERENCE, _CHECKPOINTABLEOBJECTGRAPH_CHECKPOINTABLEOBJECT_SERIALIZEDTENSOR, _CHECKPOINTABLEOBJECTGRAPH_CHECKPOINTABLEOBJECT_SLOTVARIABLEREFERENCE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=210,
  serialized_end=802,
)

_CHECKPOINTABLEOBJECTGRAPH = _descriptor.Descriptor(
  name='CheckpointableObjectGraph',
  full_name='diplomacy.tensorflow.CheckpointableObjectGraph',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nodes', full_name='diplomacy.tensorflow.CheckpointableObjectGraph.nodes', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CHECKPOINTABLEOBJECTGRAPH_CHECKPOINTABLEOBJECT, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=95,
  serialized_end=802,
)

_CHECKPOINTABLEOBJECTGRAPH_CHECKPOINTABLEOBJECT_OBJECTREFERENCE.containing_type = _CHECKPOINTABLEOBJECTGRAPH_CHECKPOINTABLEOBJECT
_CHECKPOINTABLEOBJECTGRAPH_CHECKPOINTABLEOBJECT_SERIALIZEDTENSOR.containing_type = _CHECKPOINTABLEOBJECTGRAPH_CHECKPOINTABLEOBJECT
_CHECKPOINTABLEOBJECTGRAPH_CHECKPOINTABLEOBJECT_SLOTVARIABLEREFERENCE.containing_type = _CHECKPOINTABLEOBJECTGRAPH_CHECKPOINTABLEOBJECT
_CHECKPOINTABLEOBJECTGRAPH_CHECKPOINTABLEOBJECT.fields_by_name['children'].message_type = _CHECKPOINTABLEOBJECTGRAPH_CHECKPOINTABLEOBJECT_OBJECTREFERENCE
_CHECKPOINTABLEOBJECTGRAPH_CHECKPOINTABLEOBJECT.fields_by_name['attributes'].message_type = _CHECKPOINTABLEOBJECTGRAPH_CHECKPOINTABLEOBJECT_SERIALIZEDTENSOR
_CHECKPOINTABLEOBJECTGRAPH_CHECKPOINTABLEOBJECT.fields_by_name['slot_variables'].message_type = _CHECKPOINTABLEOBJECTGRAPH_CHECKPOINTABLEOBJECT_SLOTVARIABLEREFERENCE
_CHECKPOINTABLEOBJECTGRAPH_CHECKPOINTABLEOBJECT.containing_type = _CHECKPOINTABLEOBJECTGRAPH
_CHECKPOINTABLEOBJECTGRAPH.fields_by_name['nodes'].message_type = _CHECKPOINTABLEOBJECTGRAPH_CHECKPOINTABLEOBJECT
DESCRIPTOR.message_types_by_name['CheckpointableObjectGraph'] = _CHECKPOINTABLEOBJECTGRAPH
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CheckpointableObjectGraph = _reflection.GeneratedProtocolMessageType('CheckpointableObjectGraph', (_message.Message,), dict(

  CheckpointableObject = _reflection.GeneratedProtocolMessageType('CheckpointableObject', (_message.Message,), dict(

    ObjectReference = _reflection.GeneratedProtocolMessageType('ObjectReference', (_message.Message,), dict(
      DESCRIPTOR = _CHECKPOINTABLEOBJECTGRAPH_CHECKPOINTABLEOBJECT_OBJECTREFERENCE,
      __module__ = 'diplomacy_tensorflow.core.protobuf.checkpointable_object_graph_pb2'
      # @@protoc_insertion_point(class_scope:diplomacy.tensorflow.CheckpointableObjectGraph.CheckpointableObject.ObjectReference)
      ))
    ,

    SerializedTensor = _reflection.GeneratedProtocolMessageType('SerializedTensor', (_message.Message,), dict(
      DESCRIPTOR = _CHECKPOINTABLEOBJECTGRAPH_CHECKPOINTABLEOBJECT_SERIALIZEDTENSOR,
      __module__ = 'diplomacy_tensorflow.core.protobuf.checkpointable_object_graph_pb2'
      # @@protoc_insertion_point(class_scope:diplomacy.tensorflow.CheckpointableObjectGraph.CheckpointableObject.SerializedTensor)
      ))
    ,

    SlotVariableReference = _reflection.GeneratedProtocolMessageType('SlotVariableReference', (_message.Message,), dict(
      DESCRIPTOR = _CHECKPOINTABLEOBJECTGRAPH_CHECKPOINTABLEOBJECT_SLOTVARIABLEREFERENCE,
      __module__ = 'diplomacy_tensorflow.core.protobuf.checkpointable_object_graph_pb2'
      # @@protoc_insertion_point(class_scope:diplomacy.tensorflow.CheckpointableObjectGraph.CheckpointableObject.SlotVariableReference)
      ))
    ,
    DESCRIPTOR = _CHECKPOINTABLEOBJECTGRAPH_CHECKPOINTABLEOBJECT,
    __module__ = 'diplomacy_tensorflow.core.protobuf.checkpointable_object_graph_pb2'
    # @@protoc_insertion_point(class_scope:diplomacy.tensorflow.CheckpointableObjectGraph.CheckpointableObject)
    ))
  ,
  DESCRIPTOR = _CHECKPOINTABLEOBJECTGRAPH,
  __module__ = 'diplomacy_tensorflow.core.protobuf.checkpointable_object_graph_pb2'
  # @@protoc_insertion_point(class_scope:diplomacy.tensorflow.CheckpointableObjectGraph)
  ))
_sym_db.RegisterMessage(CheckpointableObjectGraph)
_sym_db.RegisterMessage(CheckpointableObjectGraph.CheckpointableObject)
_sym_db.RegisterMessage(CheckpointableObjectGraph.CheckpointableObject.ObjectReference)
_sym_db.RegisterMessage(CheckpointableObjectGraph.CheckpointableObject.SerializedTensor)
_sym_db.RegisterMessage(CheckpointableObjectGraph.CheckpointableObject.SlotVariableReference)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)