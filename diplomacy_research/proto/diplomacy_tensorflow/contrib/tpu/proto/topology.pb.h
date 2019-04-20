// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: diplomacy_tensorflow/contrib/tpu/proto/topology.proto

#ifndef PROTOBUF_INCLUDED_diplomacy_5ftensorflow_2fcontrib_2ftpu_2fproto_2ftopology_2eproto
#define PROTOBUF_INCLUDED_diplomacy_5ftensorflow_2fcontrib_2ftpu_2fproto_2ftopology_2eproto

#include <string>

#include <google/protobuf/stubs/common.h>

#if GOOGLE_PROTOBUF_VERSION < 3006001
#error This file was generated by a newer version of protoc which is
#error incompatible with your Protocol Buffer headers.  Please update
#error your headers.
#endif
#if 3006001 < GOOGLE_PROTOBUF_MIN_PROTOC_VERSION
#error This file was generated by an older version of protoc which is
#error incompatible with your Protocol Buffer headers.  Please
#error regenerate this file with a newer version of protoc.
#endif

#include <google/protobuf/io/coded_stream.h>
#include <google/protobuf/arena.h>
#include <google/protobuf/arenastring.h>
#include <google/protobuf/generated_message_table_driven.h>
#include <google/protobuf/generated_message_util.h>
#include <google/protobuf/inlined_string_field.h>
#include <google/protobuf/metadata.h>
#include <google/protobuf/message.h>
#include <google/protobuf/repeated_field.h>  // IWYU pragma: export
#include <google/protobuf/extension_set.h>  // IWYU pragma: export
#include <google/protobuf/unknown_field_set.h>
// @@protoc_insertion_point(includes)
#define PROTOBUF_INTERNAL_EXPORT_protobuf_diplomacy_5ftensorflow_2fcontrib_2ftpu_2fproto_2ftopology_2eproto 

namespace protobuf_diplomacy_5ftensorflow_2fcontrib_2ftpu_2fproto_2ftopology_2eproto {
// Internal implementation detail -- do not use these members.
struct TableStruct {
  static const ::google::protobuf::internal::ParseTableField entries[];
  static const ::google::protobuf::internal::AuxillaryParseTableField aux[];
  static const ::google::protobuf::internal::ParseTable schema[1];
  static const ::google::protobuf::internal::FieldMetadata field_metadata[];
  static const ::google::protobuf::internal::SerializationTable serialization_table[];
  static const ::google::protobuf::uint32 offsets[];
};
void AddDescriptors();
}  // namespace protobuf_diplomacy_5ftensorflow_2fcontrib_2ftpu_2fproto_2ftopology_2eproto
namespace diplomacy {
namespace tensorflow {
namespace tpu {
class TopologyProto;
class TopologyProtoDefaultTypeInternal;
extern TopologyProtoDefaultTypeInternal _TopologyProto_default_instance_;
}  // namespace tpu
}  // namespace tensorflow
}  // namespace diplomacy
namespace google {
namespace protobuf {
template<> ::diplomacy::tensorflow::tpu::TopologyProto* Arena::CreateMaybeMessage<::diplomacy::tensorflow::tpu::TopologyProto>(Arena*);
}  // namespace protobuf
}  // namespace google
namespace diplomacy {
namespace tensorflow {
namespace tpu {

// ===================================================================

class TopologyProto : public ::google::protobuf::Message /* @@protoc_insertion_point(class_definition:diplomacy.tensorflow.tpu.TopologyProto) */ {
 public:
  TopologyProto();
  virtual ~TopologyProto();

  TopologyProto(const TopologyProto& from);

  inline TopologyProto& operator=(const TopologyProto& from) {
    CopyFrom(from);
    return *this;
  }
  #if LANG_CXX11
  TopologyProto(TopologyProto&& from) noexcept
    : TopologyProto() {
    *this = ::std::move(from);
  }

  inline TopologyProto& operator=(TopologyProto&& from) noexcept {
    if (GetArenaNoVirtual() == from.GetArenaNoVirtual()) {
      if (this != &from) InternalSwap(&from);
    } else {
      CopyFrom(from);
    }
    return *this;
  }
  #endif
  inline ::google::protobuf::Arena* GetArena() const final {
    return GetArenaNoVirtual();
  }
  inline void* GetMaybeArenaPointer() const final {
    return MaybeArenaPtr();
  }
  static const ::google::protobuf::Descriptor* descriptor();
  static const TopologyProto& default_instance();

  static void InitAsDefaultInstance();  // FOR INTERNAL USE ONLY
  static inline const TopologyProto* internal_default_instance() {
    return reinterpret_cast<const TopologyProto*>(
               &_TopologyProto_default_instance_);
  }
  static constexpr int kIndexInFileMessages =
    0;

  void UnsafeArenaSwap(TopologyProto* other);
  void Swap(TopologyProto* other);
  friend void swap(TopologyProto& a, TopologyProto& b) {
    a.Swap(&b);
  }

  // implements Message ----------------------------------------------

  inline TopologyProto* New() const final {
    return CreateMaybeMessage<TopologyProto>(NULL);
  }

  TopologyProto* New(::google::protobuf::Arena* arena) const final {
    return CreateMaybeMessage<TopologyProto>(arena);
  }
  void CopyFrom(const ::google::protobuf::Message& from) final;
  void MergeFrom(const ::google::protobuf::Message& from) final;
  void CopyFrom(const TopologyProto& from);
  void MergeFrom(const TopologyProto& from);
  void Clear() final;
  bool IsInitialized() const final;

  size_t ByteSizeLong() const final;
  bool MergePartialFromCodedStream(
      ::google::protobuf::io::CodedInputStream* input) final;
  void SerializeWithCachedSizes(
      ::google::protobuf::io::CodedOutputStream* output) const final;
  ::google::protobuf::uint8* InternalSerializeWithCachedSizesToArray(
      bool deterministic, ::google::protobuf::uint8* target) const final;
  int GetCachedSize() const final { return _cached_size_.Get(); }

  private:
  void SharedCtor();
  void SharedDtor();
  void SetCachedSize(int size) const final;
  void InternalSwap(TopologyProto* other);
  protected:
  explicit TopologyProto(::google::protobuf::Arena* arena);
  private:
  static void ArenaDtor(void* object);
  inline void RegisterArenaDtor(::google::protobuf::Arena* arena);
  private:
  inline ::google::protobuf::Arena* GetArenaNoVirtual() const {
    return _internal_metadata_.arena();
  }
  inline void* MaybeArenaPtr() const {
    return _internal_metadata_.raw_arena_ptr();
  }
  public:

  ::google::protobuf::Metadata GetMetadata() const final;

  // nested types ----------------------------------------------------

  // accessors -------------------------------------------------------

  // repeated int32 mesh_shape = 1;
  int mesh_shape_size() const;
  void clear_mesh_shape();
  static const int kMeshShapeFieldNumber = 1;
  ::google::protobuf::int32 mesh_shape(int index) const;
  void set_mesh_shape(int index, ::google::protobuf::int32 value);
  void add_mesh_shape(::google::protobuf::int32 value);
  const ::google::protobuf::RepeatedField< ::google::protobuf::int32 >&
      mesh_shape() const;
  ::google::protobuf::RepeatedField< ::google::protobuf::int32 >*
      mutable_mesh_shape();

  // repeated int32 device_coordinates = 4;
  int device_coordinates_size() const;
  void clear_device_coordinates();
  static const int kDeviceCoordinatesFieldNumber = 4;
  ::google::protobuf::int32 device_coordinates(int index) const;
  void set_device_coordinates(int index, ::google::protobuf::int32 value);
  void add_device_coordinates(::google::protobuf::int32 value);
  const ::google::protobuf::RepeatedField< ::google::protobuf::int32 >&
      device_coordinates() const;
  ::google::protobuf::RepeatedField< ::google::protobuf::int32 >*
      mutable_device_coordinates();

  // int32 num_tasks = 2;
  void clear_num_tasks();
  static const int kNumTasksFieldNumber = 2;
  ::google::protobuf::int32 num_tasks() const;
  void set_num_tasks(::google::protobuf::int32 value);

  // int32 num_tpu_devices_per_task = 3;
  void clear_num_tpu_devices_per_task();
  static const int kNumTpuDevicesPerTaskFieldNumber = 3;
  ::google::protobuf::int32 num_tpu_devices_per_task() const;
  void set_num_tpu_devices_per_task(::google::protobuf::int32 value);

  // @@protoc_insertion_point(class_scope:diplomacy.tensorflow.tpu.TopologyProto)
 private:

  ::google::protobuf::internal::InternalMetadataWithArena _internal_metadata_;
  template <typename T> friend class ::google::protobuf::Arena::InternalHelper;
  typedef void InternalArenaConstructable_;
  typedef void DestructorSkippable_;
  ::google::protobuf::RepeatedField< ::google::protobuf::int32 > mesh_shape_;
  mutable int _mesh_shape_cached_byte_size_;
  ::google::protobuf::RepeatedField< ::google::protobuf::int32 > device_coordinates_;
  mutable int _device_coordinates_cached_byte_size_;
  ::google::protobuf::int32 num_tasks_;
  ::google::protobuf::int32 num_tpu_devices_per_task_;
  mutable ::google::protobuf::internal::CachedSize _cached_size_;
  friend struct ::protobuf_diplomacy_5ftensorflow_2fcontrib_2ftpu_2fproto_2ftopology_2eproto::TableStruct;
};
// ===================================================================


// ===================================================================

#ifdef __GNUC__
  #pragma GCC diagnostic push
  #pragma GCC diagnostic ignored "-Wstrict-aliasing"
#endif  // __GNUC__
// TopologyProto

// repeated int32 mesh_shape = 1;
inline int TopologyProto::mesh_shape_size() const {
  return mesh_shape_.size();
}
inline void TopologyProto::clear_mesh_shape() {
  mesh_shape_.Clear();
}
inline ::google::protobuf::int32 TopologyProto::mesh_shape(int index) const {
  // @@protoc_insertion_point(field_get:diplomacy.tensorflow.tpu.TopologyProto.mesh_shape)
  return mesh_shape_.Get(index);
}
inline void TopologyProto::set_mesh_shape(int index, ::google::protobuf::int32 value) {
  mesh_shape_.Set(index, value);
  // @@protoc_insertion_point(field_set:diplomacy.tensorflow.tpu.TopologyProto.mesh_shape)
}
inline void TopologyProto::add_mesh_shape(::google::protobuf::int32 value) {
  mesh_shape_.Add(value);
  // @@protoc_insertion_point(field_add:diplomacy.tensorflow.tpu.TopologyProto.mesh_shape)
}
inline const ::google::protobuf::RepeatedField< ::google::protobuf::int32 >&
TopologyProto::mesh_shape() const {
  // @@protoc_insertion_point(field_list:diplomacy.tensorflow.tpu.TopologyProto.mesh_shape)
  return mesh_shape_;
}
inline ::google::protobuf::RepeatedField< ::google::protobuf::int32 >*
TopologyProto::mutable_mesh_shape() {
  // @@protoc_insertion_point(field_mutable_list:diplomacy.tensorflow.tpu.TopologyProto.mesh_shape)
  return &mesh_shape_;
}

// int32 num_tasks = 2;
inline void TopologyProto::clear_num_tasks() {
  num_tasks_ = 0;
}
inline ::google::protobuf::int32 TopologyProto::num_tasks() const {
  // @@protoc_insertion_point(field_get:diplomacy.tensorflow.tpu.TopologyProto.num_tasks)
  return num_tasks_;
}
inline void TopologyProto::set_num_tasks(::google::protobuf::int32 value) {
  
  num_tasks_ = value;
  // @@protoc_insertion_point(field_set:diplomacy.tensorflow.tpu.TopologyProto.num_tasks)
}

// int32 num_tpu_devices_per_task = 3;
inline void TopologyProto::clear_num_tpu_devices_per_task() {
  num_tpu_devices_per_task_ = 0;
}
inline ::google::protobuf::int32 TopologyProto::num_tpu_devices_per_task() const {
  // @@protoc_insertion_point(field_get:diplomacy.tensorflow.tpu.TopologyProto.num_tpu_devices_per_task)
  return num_tpu_devices_per_task_;
}
inline void TopologyProto::set_num_tpu_devices_per_task(::google::protobuf::int32 value) {
  
  num_tpu_devices_per_task_ = value;
  // @@protoc_insertion_point(field_set:diplomacy.tensorflow.tpu.TopologyProto.num_tpu_devices_per_task)
}

// repeated int32 device_coordinates = 4;
inline int TopologyProto::device_coordinates_size() const {
  return device_coordinates_.size();
}
inline void TopologyProto::clear_device_coordinates() {
  device_coordinates_.Clear();
}
inline ::google::protobuf::int32 TopologyProto::device_coordinates(int index) const {
  // @@protoc_insertion_point(field_get:diplomacy.tensorflow.tpu.TopologyProto.device_coordinates)
  return device_coordinates_.Get(index);
}
inline void TopologyProto::set_device_coordinates(int index, ::google::protobuf::int32 value) {
  device_coordinates_.Set(index, value);
  // @@protoc_insertion_point(field_set:diplomacy.tensorflow.tpu.TopologyProto.device_coordinates)
}
inline void TopologyProto::add_device_coordinates(::google::protobuf::int32 value) {
  device_coordinates_.Add(value);
  // @@protoc_insertion_point(field_add:diplomacy.tensorflow.tpu.TopologyProto.device_coordinates)
}
inline const ::google::protobuf::RepeatedField< ::google::protobuf::int32 >&
TopologyProto::device_coordinates() const {
  // @@protoc_insertion_point(field_list:diplomacy.tensorflow.tpu.TopologyProto.device_coordinates)
  return device_coordinates_;
}
inline ::google::protobuf::RepeatedField< ::google::protobuf::int32 >*
TopologyProto::mutable_device_coordinates() {
  // @@protoc_insertion_point(field_mutable_list:diplomacy.tensorflow.tpu.TopologyProto.device_coordinates)
  return &device_coordinates_;
}

#ifdef __GNUC__
  #pragma GCC diagnostic pop
#endif  // __GNUC__

// @@protoc_insertion_point(namespace_scope)

}  // namespace tpu
}  // namespace tensorflow
}  // namespace diplomacy

// @@protoc_insertion_point(global_scope)

#endif  // PROTOBUF_INCLUDED_diplomacy_5ftensorflow_2fcontrib_2ftpu_2fproto_2ftopology_2eproto