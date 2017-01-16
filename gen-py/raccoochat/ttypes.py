#
# Autogenerated by Thrift Compiler (0.10.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
import sys

from thrift.transport import TTransport


class Message(object):
    """
    Attributes:
     - time
     - userName
     - textMessage
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'time', 'UTF8', None, ),  # 1
        (2, TType.STRING, 'userName', 'UTF8', None, ),  # 2
        (3, TType.STRING, 'textMessage', 'UTF8', None, ),  # 3
    )

    def __init__(self, time=None, userName=None, textMessage=None,):
        self.time = time
        self.userName = userName
        self.textMessage = textMessage

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.time = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.userName = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.textMessage = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('Message')
        if self.time is not None:
            oprot.writeFieldBegin('time', TType.STRING, 1)
            oprot.writeString(self.time.encode('utf-8') if sys.version_info[0] == 2 else self.time)
            oprot.writeFieldEnd()
        if self.userName is not None:
            oprot.writeFieldBegin('userName', TType.STRING, 2)
            oprot.writeString(self.userName.encode('utf-8') if sys.version_info[0] == 2 else self.userName)
            oprot.writeFieldEnd()
        if self.textMessage is not None:
            oprot.writeFieldBegin('textMessage', TType.STRING, 3)
            oprot.writeString(self.textMessage.encode('utf-8') if sys.version_info[0] == 2 else self.textMessage)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class InvalidValueException(TException):
    """
    Attributes:
     - errorCode
     - errorMessage
    """

    thrift_spec = (
        None,  # 0
        (1, TType.I32, 'errorCode', None, None, ),  # 1
        (2, TType.STRING, 'errorMessage', 'UTF8', None, ),  # 2
    )

    def __init__(self, errorCode=None, errorMessage=None,):
        self.errorCode = errorCode
        self.errorMessage = errorMessage

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.errorCode = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.errorMessage = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('InvalidValueException')
        if self.errorCode is not None:
            oprot.writeFieldBegin('errorCode', TType.I32, 1)
            oprot.writeI32(self.errorCode)
            oprot.writeFieldEnd()
        if self.errorMessage is not None:
            oprot.writeFieldBegin('errorMessage', TType.STRING, 2)
            oprot.writeString(self.errorMessage.encode('utf-8') if sys.version_info[0] == 2 else self.errorMessage)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __str__(self):
        return repr(self)

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)