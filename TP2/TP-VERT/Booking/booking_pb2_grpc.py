# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import booking_pb2 as booking__pb2


class BookingStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.getBookings = channel.unary_stream(
                '/Booking/getBookings',
                request_serializer=booking__pb2.EmptyBooking.SerializeToString,
                response_deserializer=booking__pb2.BookingData.FromString,
                )
        self.getBookingForUser = channel.unary_unary(
                '/Booking/getBookingForUser',
                request_serializer=booking__pb2.UserIDBooking.SerializeToString,
                response_deserializer=booking__pb2.BookingData.FromString,
                )
        self.addBookingByUser = channel.unary_unary(
                '/Booking/addBookingByUser',
                request_serializer=booking__pb2.newBooking.SerializeToString,
                response_deserializer=booking__pb2.returnInfoBooking.FromString,
                )


class BookingServicer(object):
    """Missing associated documentation comment in .proto file."""

    def getBookings(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getBookingForUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def addBookingByUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BookingServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'getBookings': grpc.unary_stream_rpc_method_handler(
                    servicer.getBookings,
                    request_deserializer=booking__pb2.EmptyBooking.FromString,
                    response_serializer=booking__pb2.BookingData.SerializeToString,
            ),
            'getBookingForUser': grpc.unary_unary_rpc_method_handler(
                    servicer.getBookingForUser,
                    request_deserializer=booking__pb2.UserIDBooking.FromString,
                    response_serializer=booking__pb2.BookingData.SerializeToString,
            ),
            'addBookingByUser': grpc.unary_unary_rpc_method_handler(
                    servicer.addBookingByUser,
                    request_deserializer=booking__pb2.newBooking.FromString,
                    response_serializer=booking__pb2.returnInfoBooking.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Booking', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Booking(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def getBookings(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/Booking/getBookings',
            booking__pb2.EmptyBooking.SerializeToString,
            booking__pb2.BookingData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getBookingForUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Booking/getBookingForUser',
            booking__pb2.UserIDBooking.SerializeToString,
            booking__pb2.BookingData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def addBookingByUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Booking/addBookingByUser',
            booking__pb2.newBooking.SerializeToString,
            booking__pb2.returnInfoBooking.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
