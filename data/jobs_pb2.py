# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: jobs.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pb2
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor.FileDescriptor(
        name='jobs.proto',
        package='jobs',
        syntax='proto3',
        serialized_pb=b'\n\njobs.proto\x12\x04jobs\"4\n\rSearchOptions\x12\x0e\n\x06offset\x18\x01 \x01(\x05\x12\x13\n\x0bresultLimit\x18\x02 \x01(\x05\"\xf7\x02\n\x07JobInfo\x12\x10\n\x08id_icims\x18\x01 \x01(\x05\x12\x19\n\x11\x62usiness_category\x18\x02 \x01(\t\x12\x15\n\rteam_category\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\r\n\x05title\x18\x05 \x01(\t\x12\x1c\n\x14\x62\x61sic_qualifications\x18\x06 \x01(\t\x12\x11\n\tfeed_date\x18\x07 \x01(\t\x12 \n\x18preferred_qualifications\x18\x08 \x01(\t\x12\x15\n\rurl_next_step\x18\t \x01(\t\x12\x14\n\x0c\x63ompany_name\x18\n \x01(\t\x12\x14\n\x0cjob_category\x18\x0b \x01(\t\x12\x1c\n\x14primary_search_label\x18\x0c \x01(\t\x12\x19\n\x11\x64\x65scription_short\x18\r \x01(\t\x12\x10\n\x08time_ago\x18\x0e \x01(\t\x12\x10\n\x08location\x18\x0f \x01(\t\x12\x11\n\ttimestamp\x18\x10 \x01(\x05\"\x06\n\x04Void\"\x15\n\x03Int\x12\x0e\n\x06number\x18\x01 \x01(\x05\x32\x61\n\x0bJobsService\x12/\n\x07GetJobs\x12\x13.jobs.SearchOptions\x1a\r.jobs.JobInfo0\x01\x12!\n\x08GetCount\x12\n.jobs.Void\x1a\t.jobs.IntB\x0f\n\x07\x65x.grpc\xa2\x02\x03RTGb\x06proto3'
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_SEARCHOPTIONS = _descriptor.Descriptor(
        name='SearchOptions',
        full_name='jobs.SearchOptions',
        filename=None,
        file=DESCRIPTOR,
        containing_type=None,
        fields=[
            _descriptor.FieldDescriptor(
                    name='offset', full_name='jobs.SearchOptions.offset', index=0,
                    number=1, type=5, cpp_type=1, label=1,
                    has_default_value=False, default_value=0,
                    message_type=None, enum_type=None, containing_type=None,
                    is_extension=False, extension_scope=None,
                    options=None),
            _descriptor.FieldDescriptor(
                    name='resultLimit', full_name='jobs.SearchOptions.resultLimit', index=1,
                    number=2, type=5, cpp_type=1, label=1,
                    has_default_value=False, default_value=0,
                    message_type=None, enum_type=None, containing_type=None,
                    is_extension=False, extension_scope=None,
                    options=None),
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
        serialized_start=20,
        serialized_end=72,
)

_JOBINFO = _descriptor.Descriptor(
        name='JobInfo',
        full_name='jobs.JobInfo',
        filename=None,
        file=DESCRIPTOR,
        containing_type=None,
        fields=[
            _descriptor.FieldDescriptor(
                    name='id_icims', full_name='jobs.JobInfo.id_icims', index=0,
                    number=1, type=5, cpp_type=1, label=1,
                    has_default_value=False, default_value=0,
                    message_type=None, enum_type=None, containing_type=None,
                    is_extension=False, extension_scope=None,
                    options=None),
            _descriptor.FieldDescriptor(
                    name='business_category', full_name='jobs.JobInfo.business_category', index=1,
                    number=2, type=9, cpp_type=9, label=1,
                    has_default_value=False, default_value=b"".decode('utf-8'),
                    message_type=None, enum_type=None, containing_type=None,
                    is_extension=False, extension_scope=None,
                    options=None),
            _descriptor.FieldDescriptor(
                    name='team_category', full_name='jobs.JobInfo.team_category', index=2,
                    number=3, type=9, cpp_type=9, label=1,
                    has_default_value=False, default_value=b"".decode('utf-8'),
                    message_type=None, enum_type=None, containing_type=None,
                    is_extension=False, extension_scope=None,
                    options=None),
            _descriptor.FieldDescriptor(
                    name='description', full_name='jobs.JobInfo.description', index=3,
                    number=4, type=9, cpp_type=9, label=1,
                    has_default_value=False, default_value=b"".decode('utf-8'),
                    message_type=None, enum_type=None, containing_type=None,
                    is_extension=False, extension_scope=None,
                    options=None),
            _descriptor.FieldDescriptor(
                    name='title', full_name='jobs.JobInfo.title', index=4,
                    number=5, type=9, cpp_type=9, label=1,
                    has_default_value=False, default_value=b"".decode('utf-8'),
                    message_type=None, enum_type=None, containing_type=None,
                    is_extension=False, extension_scope=None,
                    options=None),
            _descriptor.FieldDescriptor(
                    name='basic_qualifications', full_name='jobs.JobInfo.basic_qualifications', index=5,
                    number=6, type=9, cpp_type=9, label=1,
                    has_default_value=False, default_value=b"".decode('utf-8'),
                    message_type=None, enum_type=None, containing_type=None,
                    is_extension=False, extension_scope=None,
                    options=None),
            _descriptor.FieldDescriptor(
                    name='feed_date', full_name='jobs.JobInfo.feed_date', index=6,
                    number=7, type=9, cpp_type=9, label=1,
                    has_default_value=False, default_value=b"".decode('utf-8'),
                    message_type=None, enum_type=None, containing_type=None,
                    is_extension=False, extension_scope=None,
                    options=None),
            _descriptor.FieldDescriptor(
                    name='preferred_qualifications', full_name='jobs.JobInfo.preferred_qualifications', index=7,
                    number=8, type=9, cpp_type=9, label=1,
                    has_default_value=False, default_value=b"".decode('utf-8'),
                    message_type=None, enum_type=None, containing_type=None,
                    is_extension=False, extension_scope=None,
                    options=None),
            _descriptor.FieldDescriptor(
                    name='url_next_step', full_name='jobs.JobInfo.url_next_step', index=8,
                    number=9, type=9, cpp_type=9, label=1,
                    has_default_value=False, default_value=b"".decode('utf-8'),
                    message_type=None, enum_type=None, containing_type=None,
                    is_extension=False, extension_scope=None,
                    options=None),
            _descriptor.FieldDescriptor(
                    name='company_name', full_name='jobs.JobInfo.company_name', index=9,
                    number=10, type=9, cpp_type=9, label=1,
                    has_default_value=False, default_value=b"".decode('utf-8'),
                    message_type=None, enum_type=None, containing_type=None,
                    is_extension=False, extension_scope=None,
                    options=None),
            _descriptor.FieldDescriptor(
                    name='job_category', full_name='jobs.JobInfo.job_category', index=10,
                    number=11, type=9, cpp_type=9, label=1,
                    has_default_value=False, default_value=b"".decode('utf-8'),
                    message_type=None, enum_type=None, containing_type=None,
                    is_extension=False, extension_scope=None,
                    options=None),
            _descriptor.FieldDescriptor(
                    name='primary_search_label', full_name='jobs.JobInfo.primary_search_label', index=11,
                    number=12, type=9, cpp_type=9, label=1,
                    has_default_value=False, default_value=b"".decode('utf-8'),
                    message_type=None, enum_type=None, containing_type=None,
                    is_extension=False, extension_scope=None,
                    options=None),
            _descriptor.FieldDescriptor(
                    name='description_short', full_name='jobs.JobInfo.description_short', index=12,
                    number=13, type=9, cpp_type=9, label=1,
                    has_default_value=False, default_value=b"".decode('utf-8'),
                    message_type=None, enum_type=None, containing_type=None,
                    is_extension=False, extension_scope=None,
                    options=None),
            _descriptor.FieldDescriptor(
                    name='time_ago', full_name='jobs.JobInfo.time_ago', index=13,
                    number=14, type=9, cpp_type=9, label=1,
                    has_default_value=False, default_value=b"".decode('utf-8'),
                    message_type=None, enum_type=None, containing_type=None,
                    is_extension=False, extension_scope=None,
                    options=None),
            _descriptor.FieldDescriptor(
                    name='location', full_name='jobs.JobInfo.location', index=14,
                    number=15, type=9, cpp_type=9, label=1,
                    has_default_value=False, default_value=b"".decode('utf-8'),
                    message_type=None, enum_type=None, containing_type=None,
                    is_extension=False, extension_scope=None,
                    options=None),
            _descriptor.FieldDescriptor(
                    name='timestamp', full_name='jobs.JobInfo.timestamp', index=15,
                    number=16, type=5, cpp_type=1, label=1,
                    has_default_value=False, default_value=0,
                    message_type=None, enum_type=None, containing_type=None,
                    is_extension=False, extension_scope=None,
                    options=None),
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
        serialized_start=75,
        serialized_end=450,
)

_VOID = _descriptor.Descriptor(
        name='Void',
        full_name='jobs.Void',
        filename=None,
        file=DESCRIPTOR,
        containing_type=None,
        fields=[
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
        serialized_start=452,
        serialized_end=458,
)

_INT = _descriptor.Descriptor(
        name='Int',
        full_name='jobs.Int',
        filename=None,
        file=DESCRIPTOR,
        containing_type=None,
        fields=[
            _descriptor.FieldDescriptor(
                    name='number', full_name='jobs.Int.number', index=0,
                    number=1, type=5, cpp_type=1, label=1,
                    has_default_value=False, default_value=0,
                    message_type=None, enum_type=None, containing_type=None,
                    is_extension=False, extension_scope=None,
                    options=None),
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
        serialized_start=460,
        serialized_end=481,
)

DESCRIPTOR.message_types_by_name['SearchOptions'] = _SEARCHOPTIONS
DESCRIPTOR.message_types_by_name['JobInfo'] = _JOBINFO
DESCRIPTOR.message_types_by_name['Void'] = _VOID
DESCRIPTOR.message_types_by_name['Int'] = _INT

SearchOptions = _reflection.GeneratedProtocolMessageType('SearchOptions', (_message.Message,), dict(
        DESCRIPTOR=_SEARCHOPTIONS,
        __module__='jobs_pb2'
        # @@protoc_insertion_point(class_scope:jobs.SearchOptions)
))
_sym_db.RegisterMessage(SearchOptions)

JobInfo = _reflection.GeneratedProtocolMessageType('JobInfo', (_message.Message,), dict(
        DESCRIPTOR=_JOBINFO,
        __module__='jobs_pb2'
        # @@protoc_insertion_point(class_scope:jobs.JobInfo)
))
_sym_db.RegisterMessage(JobInfo)

Void = _reflection.GeneratedProtocolMessageType('Void', (_message.Message,), dict(
        DESCRIPTOR=_VOID,
        __module__='jobs_pb2'
        # @@protoc_insertion_point(class_scope:jobs.Void)
))
_sym_db.RegisterMessage(Void)

Int = _reflection.GeneratedProtocolMessageType('Int', (_message.Message,), dict(
        DESCRIPTOR=_INT,
        __module__='jobs_pb2'
        # @@protoc_insertion_point(class_scope:jobs.Int)
))
_sym_db.RegisterMessage(Int)

DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), b'\n\007ex.grpc\242\002\003RTG')
import abc
from grpc.beta import implementations as beta_implementations
from grpc.early_adopter import implementations as early_adopter_implementations
from grpc.framework.alpha import utilities as alpha_utilities
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities


class EarlyAdopterJobsServiceServicer(object):
    """<fill me in later!>"""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def GetJobs(self, request, context):
        raise NotImplementedError()

    @abc.abstractmethod
    def GetCount(self, request, context):
        raise NotImplementedError()


class EarlyAdopterJobsServiceServer(object):
    """<fill me in later!>"""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def start(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def stop(self):
        raise NotImplementedError()


class EarlyAdopterJobsServiceStub(object):
    """<fill me in later!>"""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def GetJobs(self, request):
        raise NotImplementedError()

    GetJobs.async = None

    @abc.abstractmethod
    def GetCount(self, request):
        raise NotImplementedError()

    GetCount.async = None


def early_adopter_create_JobsService_server(servicer, port, private_key=None, certificate_chain=None):
    import jobs_pb2
    method_service_descriptions = {
        "GetCount": alpha_utilities.unary_unary_service_description(
                servicer.GetCount,
                jobs_pb2.Void.FromString,
                jobs_pb2.Int.SerializeToString,
        ),
        "GetJobs": alpha_utilities.unary_stream_service_description(
                servicer.GetJobs,
                jobs_pb2.SearchOptions.FromString,
                jobs_pb2.JobInfo.SerializeToString,
        ),
    }
    return early_adopter_implementations.server("jobs.JobsService", method_service_descriptions, port,
                                                private_key=private_key, certificate_chain=certificate_chain)


def early_adopter_create_JobsService_stub(host, port, metadata_transformer=None, secure=False, root_certificates=None,
                                          private_key=None, certificate_chain=None, server_host_override=None):
    import jobs_pb2
    method_invocation_descriptions = {
        "GetCount": alpha_utilities.unary_unary_invocation_description(
                jobs_pb2.Void.SerializeToString,
                jobs_pb2.Int.FromString,
        ),
        "GetJobs": alpha_utilities.unary_stream_invocation_description(
                jobs_pb2.SearchOptions.SerializeToString,
                jobs_pb2.JobInfo.FromString,
        ),
    }
    return early_adopter_implementations.stub("jobs.JobsService", method_invocation_descriptions, host, port,
                                              metadata_transformer=metadata_transformer, secure=secure,
                                              root_certificates=root_certificates, private_key=private_key,
                                              certificate_chain=certificate_chain,
                                              server_host_override=server_host_override)


class BetaJobsServiceServicer(object):
    """<fill me in later!>"""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def GetJobs(self, request, context):
        raise NotImplementedError()

    @abc.abstractmethod
    def GetCount(self, request, context):
        raise NotImplementedError()


class BetaJobsServiceStub(object):
    """The interface to which stubs will conform."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def GetJobs(self, request, timeout):
        raise NotImplementedError()

    @abc.abstractmethod
    def GetCount(self, request, timeout):
        raise NotImplementedError()

    GetCount.future = None


def beta_create_JobsService_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    import jobs_pb2
    request_deserializers = {
        ('jobs.JobsService', 'GetCount'): jobs_pb2.Void.FromString,
        ('jobs.JobsService', 'GetJobs'): jobs_pb2.SearchOptions.FromString,
    }
    response_serializers = {
        ('jobs.JobsService', 'GetCount'): jobs_pb2.Int.SerializeToString,
        ('jobs.JobsService', 'GetJobs'): jobs_pb2.JobInfo.SerializeToString,
    }
    method_implementations = {
        ('jobs.JobsService', 'GetCount'): face_utilities.unary_unary_inline(servicer.GetCount),
        ('jobs.JobsService', 'GetJobs'): face_utilities.unary_stream_inline(servicer.GetJobs),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers,
                                                         response_serializers=response_serializers, thread_pool=pool,
                                                         thread_pool_size=pool_size, default_timeout=default_timeout,
                                                         maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


def beta_create_JobsService_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    import jobs_pb2
    request_serializers = {
        ('jobs.JobsService', 'GetCount'): jobs_pb2.Void.SerializeToString,
        ('jobs.JobsService', 'GetJobs'): jobs_pb2.SearchOptions.SerializeToString,
    }
    response_deserializers = {
        ('jobs.JobsService', 'GetCount'): jobs_pb2.Int.FromString,
        ('jobs.JobsService', 'GetJobs'): jobs_pb2.JobInfo.FromString,
    }
    cardinalities = {
        'GetCount': cardinality.Cardinality.UNARY_UNARY,
        'GetJobs': cardinality.Cardinality.UNARY_STREAM,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer,
                                                     request_serializers=request_serializers,
                                                     response_deserializers=response_deserializers, thread_pool=pool,
                                                     thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'jobs.JobsService', cardinalities, options=stub_options)

# @@protoc_insertion_point(module_scope)