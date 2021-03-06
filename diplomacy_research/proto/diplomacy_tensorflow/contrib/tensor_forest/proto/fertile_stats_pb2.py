# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: diplomacy_tensorflow/contrib/tensor_forest/proto/fertile_stats.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from diplomacy_tensorflow.contrib.decision_trees.proto import generic_tree_model_pb2 as diplomacy__tensorflow_dot_contrib_dot_decision__trees_dot_proto_dot_generic__tree__model__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='diplomacy_tensorflow/contrib/tensor_forest/proto/fertile_stats.proto',
  package='diplomacy.tensorflow.tensorforest',
  syntax='proto3',
  serialized_options=_b('\370\001\001'),
  serialized_pb=_b('\nDdiplomacy_tensorflow/contrib/tensor_forest/proto/fertile_stats.proto\x12!diplomacy.tensorflow.tensorforest\x1aJdiplomacy_tensorflow/contrib/decision_trees/proto/generic_tree_model.proto\"T\n\x0c\x46\x65rtileStats\x12\x44\n\x0cnode_to_slot\x18\x01 \x03(\x0b\x32..diplomacy.tensorflow.tensorforest.FertileSlot\"\x1b\n\tGiniStats\x12\x0e\n\x06square\x18\x02 \x01(\x02\"\x98\x05\n\x08LeafStat\x12\x12\n\nweight_sum\x18\x03 \x01(\x02\x12\x65\n\x0e\x63lassification\x18\x01 \x01(\x0b\x32K.diplomacy.tensorflow.tensorforest.LeafStat.GiniImpurityClassificationStatsH\x00\x12]\n\nregression\x18\x02 \x01(\x0b\x32G.diplomacy.tensorflow.tensorforest.LeafStat.LeastSquaresRegressionStatsH\x00\x1a\xf8\x01\n\x1fGiniImpurityClassificationStats\x12\x43\n\x0c\x64\x65nse_counts\x18\x01 \x01(\x0b\x32+.diplomacy.tensorflow.decision_trees.VectorH\x00\x12J\n\rsparse_counts\x18\x02 \x01(\x0b\x32\x31.diplomacy.tensorflow.decision_trees.SparseVectorH\x00\x12:\n\x04gini\x18\x03 \x01(\x0b\x32,.diplomacy.tensorflow.tensorforest.GiniStatsB\x08\n\x06\x63ounts\x1a\xa9\x01\n\x1bLeastSquaresRegressionStats\x12@\n\x0bmean_output\x18\x01 \x01(\x0b\x32+.diplomacy.tensorflow.decision_trees.Vector\x12H\n\x13mean_output_squares\x18\x02 \x01(\x0b\x32+.diplomacy.tensorflow.decision_trees.VectorB\x0b\n\tleaf_stat\"\x80\x02\n\x0b\x46\x65rtileSlot\x12?\n\nleaf_stats\x18\x04 \x01(\x0b\x32+.diplomacy.tensorflow.tensorforest.LeafStat\x12\x45\n\ncandidates\x18\x01 \x03(\x0b\x32\x31.diplomacy.tensorflow.tensorforest.SplitCandidate\x12I\n\x14post_init_leaf_stats\x18\x06 \x01(\x0b\x32+.diplomacy.tensorflow.tensorforest.LeafStat\x12\x0f\n\x07node_id\x18\x05 \x01(\x05\x12\r\n\x05\x64\x65pth\x18\x07 \x01(\x05\"\xe6\x01\n\x0eSplitCandidate\x12>\n\x05split\x18\x01 \x01(\x0b\x32/.diplomacy.tensorflow.decision_trees.BinaryNode\x12?\n\nleft_stats\x18\x04 \x01(\x0b\x32+.diplomacy.tensorflow.tensorforest.LeafStat\x12@\n\x0bright_stats\x18\x05 \x01(\x0b\x32+.diplomacy.tensorflow.tensorforest.LeafStat\x12\x11\n\tunique_id\x18\x06 \x01(\t\"P\n\x08TreePath\x12\x44\n\rnodes_visited\x18\x01 \x03(\x0b\x32-.diplomacy.tensorflow.decision_trees.TreeNodeB\x03\xf8\x01\x01\x62\x06proto3')
  ,
  dependencies=[diplomacy__tensorflow_dot_contrib_dot_decision__trees_dot_proto_dot_generic__tree__model__pb2.DESCRIPTOR,])




_FERTILESTATS = _descriptor.Descriptor(
  name='FertileStats',
  full_name='diplomacy.tensorflow.tensorforest.FertileStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='node_to_slot', full_name='diplomacy.tensorflow.tensorforest.FertileStats.node_to_slot', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=183,
  serialized_end=267,
)


_GINISTATS = _descriptor.Descriptor(
  name='GiniStats',
  full_name='diplomacy.tensorflow.tensorforest.GiniStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='square', full_name='diplomacy.tensorflow.tensorforest.GiniStats.square', index=0,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=269,
  serialized_end=296,
)


_LEAFSTAT_GINIIMPURITYCLASSIFICATIONSTATS = _descriptor.Descriptor(
  name='GiniImpurityClassificationStats',
  full_name='diplomacy.tensorflow.tensorforest.LeafStat.GiniImpurityClassificationStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dense_counts', full_name='diplomacy.tensorflow.tensorforest.LeafStat.GiniImpurityClassificationStats.dense_counts', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sparse_counts', full_name='diplomacy.tensorflow.tensorforest.LeafStat.GiniImpurityClassificationStats.sparse_counts', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gini', full_name='diplomacy.tensorflow.tensorforest.LeafStat.GiniImpurityClassificationStats.gini', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
      name='counts', full_name='diplomacy.tensorflow.tensorforest.LeafStat.GiniImpurityClassificationStats.counts',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=530,
  serialized_end=778,
)

_LEAFSTAT_LEASTSQUARESREGRESSIONSTATS = _descriptor.Descriptor(
  name='LeastSquaresRegressionStats',
  full_name='diplomacy.tensorflow.tensorforest.LeafStat.LeastSquaresRegressionStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mean_output', full_name='diplomacy.tensorflow.tensorforest.LeafStat.LeastSquaresRegressionStats.mean_output', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mean_output_squares', full_name='diplomacy.tensorflow.tensorforest.LeafStat.LeastSquaresRegressionStats.mean_output_squares', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=781,
  serialized_end=950,
)

_LEAFSTAT = _descriptor.Descriptor(
  name='LeafStat',
  full_name='diplomacy.tensorflow.tensorforest.LeafStat',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='weight_sum', full_name='diplomacy.tensorflow.tensorforest.LeafStat.weight_sum', index=0,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='classification', full_name='diplomacy.tensorflow.tensorforest.LeafStat.classification', index=1,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='regression', full_name='diplomacy.tensorflow.tensorforest.LeafStat.regression', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LEAFSTAT_GINIIMPURITYCLASSIFICATIONSTATS, _LEAFSTAT_LEASTSQUARESREGRESSIONSTATS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='leaf_stat', full_name='diplomacy.tensorflow.tensorforest.LeafStat.leaf_stat',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=299,
  serialized_end=963,
)


_FERTILESLOT = _descriptor.Descriptor(
  name='FertileSlot',
  full_name='diplomacy.tensorflow.tensorforest.FertileSlot',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='leaf_stats', full_name='diplomacy.tensorflow.tensorforest.FertileSlot.leaf_stats', index=0,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='candidates', full_name='diplomacy.tensorflow.tensorforest.FertileSlot.candidates', index=1,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='post_init_leaf_stats', full_name='diplomacy.tensorflow.tensorforest.FertileSlot.post_init_leaf_stats', index=2,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='node_id', full_name='diplomacy.tensorflow.tensorforest.FertileSlot.node_id', index=3,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='depth', full_name='diplomacy.tensorflow.tensorforest.FertileSlot.depth', index=4,
      number=7, type=5, cpp_type=1, label=1,
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
  serialized_start=966,
  serialized_end=1222,
)


_SPLITCANDIDATE = _descriptor.Descriptor(
  name='SplitCandidate',
  full_name='diplomacy.tensorflow.tensorforest.SplitCandidate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='split', full_name='diplomacy.tensorflow.tensorforest.SplitCandidate.split', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='left_stats', full_name='diplomacy.tensorflow.tensorforest.SplitCandidate.left_stats', index=1,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='right_stats', full_name='diplomacy.tensorflow.tensorforest.SplitCandidate.right_stats', index=2,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unique_id', full_name='diplomacy.tensorflow.tensorforest.SplitCandidate.unique_id', index=3,
      number=6, type=9, cpp_type=9, label=1,
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
  serialized_start=1225,
  serialized_end=1455,
)


_TREEPATH = _descriptor.Descriptor(
  name='TreePath',
  full_name='diplomacy.tensorflow.tensorforest.TreePath',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nodes_visited', full_name='diplomacy.tensorflow.tensorforest.TreePath.nodes_visited', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1457,
  serialized_end=1537,
)

_FERTILESTATS.fields_by_name['node_to_slot'].message_type = _FERTILESLOT
_LEAFSTAT_GINIIMPURITYCLASSIFICATIONSTATS.fields_by_name['dense_counts'].message_type = diplomacy__tensorflow_dot_contrib_dot_decision__trees_dot_proto_dot_generic__tree__model__pb2._VECTOR
_LEAFSTAT_GINIIMPURITYCLASSIFICATIONSTATS.fields_by_name['sparse_counts'].message_type = diplomacy__tensorflow_dot_contrib_dot_decision__trees_dot_proto_dot_generic__tree__model__pb2._SPARSEVECTOR
_LEAFSTAT_GINIIMPURITYCLASSIFICATIONSTATS.fields_by_name['gini'].message_type = _GINISTATS
_LEAFSTAT_GINIIMPURITYCLASSIFICATIONSTATS.containing_type = _LEAFSTAT
_LEAFSTAT_GINIIMPURITYCLASSIFICATIONSTATS.oneofs_by_name['counts'].fields.append(
  _LEAFSTAT_GINIIMPURITYCLASSIFICATIONSTATS.fields_by_name['dense_counts'])
_LEAFSTAT_GINIIMPURITYCLASSIFICATIONSTATS.fields_by_name['dense_counts'].containing_oneof = _LEAFSTAT_GINIIMPURITYCLASSIFICATIONSTATS.oneofs_by_name['counts']
_LEAFSTAT_GINIIMPURITYCLASSIFICATIONSTATS.oneofs_by_name['counts'].fields.append(
  _LEAFSTAT_GINIIMPURITYCLASSIFICATIONSTATS.fields_by_name['sparse_counts'])
_LEAFSTAT_GINIIMPURITYCLASSIFICATIONSTATS.fields_by_name['sparse_counts'].containing_oneof = _LEAFSTAT_GINIIMPURITYCLASSIFICATIONSTATS.oneofs_by_name['counts']
_LEAFSTAT_LEASTSQUARESREGRESSIONSTATS.fields_by_name['mean_output'].message_type = diplomacy__tensorflow_dot_contrib_dot_decision__trees_dot_proto_dot_generic__tree__model__pb2._VECTOR
_LEAFSTAT_LEASTSQUARESREGRESSIONSTATS.fields_by_name['mean_output_squares'].message_type = diplomacy__tensorflow_dot_contrib_dot_decision__trees_dot_proto_dot_generic__tree__model__pb2._VECTOR
_LEAFSTAT_LEASTSQUARESREGRESSIONSTATS.containing_type = _LEAFSTAT
_LEAFSTAT.fields_by_name['classification'].message_type = _LEAFSTAT_GINIIMPURITYCLASSIFICATIONSTATS
_LEAFSTAT.fields_by_name['regression'].message_type = _LEAFSTAT_LEASTSQUARESREGRESSIONSTATS
_LEAFSTAT.oneofs_by_name['leaf_stat'].fields.append(
  _LEAFSTAT.fields_by_name['classification'])
_LEAFSTAT.fields_by_name['classification'].containing_oneof = _LEAFSTAT.oneofs_by_name['leaf_stat']
_LEAFSTAT.oneofs_by_name['leaf_stat'].fields.append(
  _LEAFSTAT.fields_by_name['regression'])
_LEAFSTAT.fields_by_name['regression'].containing_oneof = _LEAFSTAT.oneofs_by_name['leaf_stat']
_FERTILESLOT.fields_by_name['leaf_stats'].message_type = _LEAFSTAT
_FERTILESLOT.fields_by_name['candidates'].message_type = _SPLITCANDIDATE
_FERTILESLOT.fields_by_name['post_init_leaf_stats'].message_type = _LEAFSTAT
_SPLITCANDIDATE.fields_by_name['split'].message_type = diplomacy__tensorflow_dot_contrib_dot_decision__trees_dot_proto_dot_generic__tree__model__pb2._BINARYNODE
_SPLITCANDIDATE.fields_by_name['left_stats'].message_type = _LEAFSTAT
_SPLITCANDIDATE.fields_by_name['right_stats'].message_type = _LEAFSTAT
_TREEPATH.fields_by_name['nodes_visited'].message_type = diplomacy__tensorflow_dot_contrib_dot_decision__trees_dot_proto_dot_generic__tree__model__pb2._TREENODE
DESCRIPTOR.message_types_by_name['FertileStats'] = _FERTILESTATS
DESCRIPTOR.message_types_by_name['GiniStats'] = _GINISTATS
DESCRIPTOR.message_types_by_name['LeafStat'] = _LEAFSTAT
DESCRIPTOR.message_types_by_name['FertileSlot'] = _FERTILESLOT
DESCRIPTOR.message_types_by_name['SplitCandidate'] = _SPLITCANDIDATE
DESCRIPTOR.message_types_by_name['TreePath'] = _TREEPATH
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FertileStats = _reflection.GeneratedProtocolMessageType('FertileStats', (_message.Message,), dict(
  DESCRIPTOR = _FERTILESTATS,
  __module__ = 'diplomacy_tensorflow.contrib.tensor_forest.proto.fertile_stats_pb2'
  # @@protoc_insertion_point(class_scope:diplomacy.tensorflow.tensorforest.FertileStats)
  ))
_sym_db.RegisterMessage(FertileStats)

GiniStats = _reflection.GeneratedProtocolMessageType('GiniStats', (_message.Message,), dict(
  DESCRIPTOR = _GINISTATS,
  __module__ = 'diplomacy_tensorflow.contrib.tensor_forest.proto.fertile_stats_pb2'
  # @@protoc_insertion_point(class_scope:diplomacy.tensorflow.tensorforest.GiniStats)
  ))
_sym_db.RegisterMessage(GiniStats)

LeafStat = _reflection.GeneratedProtocolMessageType('LeafStat', (_message.Message,), dict(

  GiniImpurityClassificationStats = _reflection.GeneratedProtocolMessageType('GiniImpurityClassificationStats', (_message.Message,), dict(
    DESCRIPTOR = _LEAFSTAT_GINIIMPURITYCLASSIFICATIONSTATS,
    __module__ = 'diplomacy_tensorflow.contrib.tensor_forest.proto.fertile_stats_pb2'
    # @@protoc_insertion_point(class_scope:diplomacy.tensorflow.tensorforest.LeafStat.GiniImpurityClassificationStats)
    ))
  ,

  LeastSquaresRegressionStats = _reflection.GeneratedProtocolMessageType('LeastSquaresRegressionStats', (_message.Message,), dict(
    DESCRIPTOR = _LEAFSTAT_LEASTSQUARESREGRESSIONSTATS,
    __module__ = 'diplomacy_tensorflow.contrib.tensor_forest.proto.fertile_stats_pb2'
    # @@protoc_insertion_point(class_scope:diplomacy.tensorflow.tensorforest.LeafStat.LeastSquaresRegressionStats)
    ))
  ,
  DESCRIPTOR = _LEAFSTAT,
  __module__ = 'diplomacy_tensorflow.contrib.tensor_forest.proto.fertile_stats_pb2'
  # @@protoc_insertion_point(class_scope:diplomacy.tensorflow.tensorforest.LeafStat)
  ))
_sym_db.RegisterMessage(LeafStat)
_sym_db.RegisterMessage(LeafStat.GiniImpurityClassificationStats)
_sym_db.RegisterMessage(LeafStat.LeastSquaresRegressionStats)

FertileSlot = _reflection.GeneratedProtocolMessageType('FertileSlot', (_message.Message,), dict(
  DESCRIPTOR = _FERTILESLOT,
  __module__ = 'diplomacy_tensorflow.contrib.tensor_forest.proto.fertile_stats_pb2'
  # @@protoc_insertion_point(class_scope:diplomacy.tensorflow.tensorforest.FertileSlot)
  ))
_sym_db.RegisterMessage(FertileSlot)

SplitCandidate = _reflection.GeneratedProtocolMessageType('SplitCandidate', (_message.Message,), dict(
  DESCRIPTOR = _SPLITCANDIDATE,
  __module__ = 'diplomacy_tensorflow.contrib.tensor_forest.proto.fertile_stats_pb2'
  # @@protoc_insertion_point(class_scope:diplomacy.tensorflow.tensorforest.SplitCandidate)
  ))
_sym_db.RegisterMessage(SplitCandidate)

TreePath = _reflection.GeneratedProtocolMessageType('TreePath', (_message.Message,), dict(
  DESCRIPTOR = _TREEPATH,
  __module__ = 'diplomacy_tensorflow.contrib.tensor_forest.proto.fertile_stats_pb2'
  # @@protoc_insertion_point(class_scope:diplomacy.tensorflow.tensorforest.TreePath)
  ))
_sym_db.RegisterMessage(TreePath)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
