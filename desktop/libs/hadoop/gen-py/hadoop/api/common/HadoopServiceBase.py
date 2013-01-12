#
# Autogenerated by Thrift Compiler (0.9.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py:new_style
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException
from ttypes import *
from thrift.Thrift import TProcessor
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class Iface(object):
  def getVersionInfo(self, ctx):
    """
    Return the version information for this server

    Parameters:
     - ctx
    """
    pass

  def getRuntimeInfo(self, ctx):
    """
    Parameters:
     - ctx
    """
    pass

  def getThreadDump(self, ctx):
    """
    Parameters:
     - ctx
    """
    pass

  def getAllMetrics(self, ctx):
    """
    Parameters:
     - ctx
    """
    pass

  def getMetricsContext(self, ctx, contextName):
    """
    Parameters:
     - ctx
     - contextName
    """
    pass


class Client(Iface):
  def __init__(self, iprot, oprot=None):
    self._iprot = self._oprot = iprot
    if oprot is not None:
      self._oprot = oprot
    self._seqid = 0

  def getVersionInfo(self, ctx):
    """
    Return the version information for this server

    Parameters:
     - ctx
    """
    self.send_getVersionInfo(ctx)
    return self.recv_getVersionInfo()

  def send_getVersionInfo(self, ctx):
    self._oprot.writeMessageBegin('getVersionInfo', TMessageType.CALL, self._seqid)
    args = getVersionInfo_args()
    args.ctx = ctx
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_getVersionInfo(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = getVersionInfo_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "getVersionInfo failed: unknown result");

  def getRuntimeInfo(self, ctx):
    """
    Parameters:
     - ctx
    """
    self.send_getRuntimeInfo(ctx)
    return self.recv_getRuntimeInfo()

  def send_getRuntimeInfo(self, ctx):
    self._oprot.writeMessageBegin('getRuntimeInfo', TMessageType.CALL, self._seqid)
    args = getRuntimeInfo_args()
    args.ctx = ctx
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_getRuntimeInfo(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = getRuntimeInfo_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "getRuntimeInfo failed: unknown result");

  def getThreadDump(self, ctx):
    """
    Parameters:
     - ctx
    """
    self.send_getThreadDump(ctx)
    return self.recv_getThreadDump()

  def send_getThreadDump(self, ctx):
    self._oprot.writeMessageBegin('getThreadDump', TMessageType.CALL, self._seqid)
    args = getThreadDump_args()
    args.ctx = ctx
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_getThreadDump(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = getThreadDump_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "getThreadDump failed: unknown result");

  def getAllMetrics(self, ctx):
    """
    Parameters:
     - ctx
    """
    self.send_getAllMetrics(ctx)
    return self.recv_getAllMetrics()

  def send_getAllMetrics(self, ctx):
    self._oprot.writeMessageBegin('getAllMetrics', TMessageType.CALL, self._seqid)
    args = getAllMetrics_args()
    args.ctx = ctx
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_getAllMetrics(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = getAllMetrics_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    if result.err is not None:
      raise result.err
    raise TApplicationException(TApplicationException.MISSING_RESULT, "getAllMetrics failed: unknown result");

  def getMetricsContext(self, ctx, contextName):
    """
    Parameters:
     - ctx
     - contextName
    """
    self.send_getMetricsContext(ctx, contextName)
    return self.recv_getMetricsContext()

  def send_getMetricsContext(self, ctx, contextName):
    self._oprot.writeMessageBegin('getMetricsContext', TMessageType.CALL, self._seqid)
    args = getMetricsContext_args()
    args.ctx = ctx
    args.contextName = contextName
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_getMetricsContext(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = getMetricsContext_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    if result.err is not None:
      raise result.err
    raise TApplicationException(TApplicationException.MISSING_RESULT, "getMetricsContext failed: unknown result");


class Processor(Iface, TProcessor):
  def __init__(self, handler):
    self._handler = handler
    self._processMap = {}
    self._processMap["getVersionInfo"] = Processor.process_getVersionInfo
    self._processMap["getRuntimeInfo"] = Processor.process_getRuntimeInfo
    self._processMap["getThreadDump"] = Processor.process_getThreadDump
    self._processMap["getAllMetrics"] = Processor.process_getAllMetrics
    self._processMap["getMetricsContext"] = Processor.process_getMetricsContext

  def process(self, iprot, oprot):
    (name, type, seqid) = iprot.readMessageBegin()
    if name not in self._processMap:
      iprot.skip(TType.STRUCT)
      iprot.readMessageEnd()
      x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % (name))
      oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
      x.write(oprot)
      oprot.writeMessageEnd()
      oprot.trans.flush()
      return
    else:
      self._processMap[name](self, seqid, iprot, oprot)
    return True

  def process_getVersionInfo(self, seqid, iprot, oprot):
    args = getVersionInfo_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = getVersionInfo_result()
    result.success = self._handler.getVersionInfo(args.ctx)
    oprot.writeMessageBegin("getVersionInfo", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_getRuntimeInfo(self, seqid, iprot, oprot):
    args = getRuntimeInfo_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = getRuntimeInfo_result()
    result.success = self._handler.getRuntimeInfo(args.ctx)
    oprot.writeMessageBegin("getRuntimeInfo", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_getThreadDump(self, seqid, iprot, oprot):
    args = getThreadDump_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = getThreadDump_result()
    result.success = self._handler.getThreadDump(args.ctx)
    oprot.writeMessageBegin("getThreadDump", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_getAllMetrics(self, seqid, iprot, oprot):
    args = getAllMetrics_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = getAllMetrics_result()
    try:
      result.success = self._handler.getAllMetrics(args.ctx)
    except IOException as err:
      result.err = err
    oprot.writeMessageBegin("getAllMetrics", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_getMetricsContext(self, seqid, iprot, oprot):
    args = getMetricsContext_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = getMetricsContext_result()
    try:
      result.success = self._handler.getMetricsContext(args.ctx, args.contextName)
    except IOException as err:
      result.err = err
    oprot.writeMessageBegin("getMetricsContext", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()


# HELPER FUNCTIONS AND STRUCTURES

class getVersionInfo_args(object):
  """
  Attributes:
   - ctx
  """

  thrift_spec = (
    None, # 0
    None, # 1
    None, # 2
    None, # 3
    None, # 4
    None, # 5
    None, # 6
    None, # 7
    None, # 8
    None, # 9
    (10, TType.STRUCT, 'ctx', (RequestContext, RequestContext.thrift_spec), None, ), # 10
  )

  def __init__(self, ctx=None,):
    self.ctx = ctx

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 10:
        if ftype == TType.STRUCT:
          self.ctx = RequestContext()
          self.ctx.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('getVersionInfo_args')
    if self.ctx is not None:
      oprot.writeFieldBegin('ctx', TType.STRUCT, 10)
      self.ctx.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class getVersionInfo_result(object):
  """
  Attributes:
   - success
  """

  thrift_spec = (
    (0, TType.STRUCT, 'success', (VersionInfo, VersionInfo.thrift_spec), None, ), # 0
  )

  def __init__(self, success=None,):
    self.success = success

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.STRUCT:
          self.success = VersionInfo()
          self.success.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('getVersionInfo_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.STRUCT, 0)
      self.success.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class getRuntimeInfo_args(object):
  """
  Attributes:
   - ctx
  """

  thrift_spec = (
    None, # 0
    None, # 1
    None, # 2
    None, # 3
    None, # 4
    None, # 5
    None, # 6
    None, # 7
    None, # 8
    None, # 9
    (10, TType.STRUCT, 'ctx', (RequestContext, RequestContext.thrift_spec), None, ), # 10
  )

  def __init__(self, ctx=None,):
    self.ctx = ctx

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 10:
        if ftype == TType.STRUCT:
          self.ctx = RequestContext()
          self.ctx.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('getRuntimeInfo_args')
    if self.ctx is not None:
      oprot.writeFieldBegin('ctx', TType.STRUCT, 10)
      self.ctx.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class getRuntimeInfo_result(object):
  """
  Attributes:
   - success
  """

  thrift_spec = (
    (0, TType.STRUCT, 'success', (RuntimeInfo, RuntimeInfo.thrift_spec), None, ), # 0
  )

  def __init__(self, success=None,):
    self.success = success

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.STRUCT:
          self.success = RuntimeInfo()
          self.success.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('getRuntimeInfo_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.STRUCT, 0)
      self.success.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class getThreadDump_args(object):
  """
  Attributes:
   - ctx
  """

  thrift_spec = (
    None, # 0
    None, # 1
    None, # 2
    None, # 3
    None, # 4
    None, # 5
    None, # 6
    None, # 7
    None, # 8
    None, # 9
    (10, TType.STRUCT, 'ctx', (RequestContext, RequestContext.thrift_spec), None, ), # 10
  )

  def __init__(self, ctx=None,):
    self.ctx = ctx

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 10:
        if ftype == TType.STRUCT:
          self.ctx = RequestContext()
          self.ctx.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('getThreadDump_args')
    if self.ctx is not None:
      oprot.writeFieldBegin('ctx', TType.STRUCT, 10)
      self.ctx.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class getThreadDump_result(object):
  """
  Attributes:
   - success
  """

  thrift_spec = (
    (0, TType.LIST, 'success', (TType.STRUCT,(ThreadStackTrace, ThreadStackTrace.thrift_spec)), None, ), # 0
  )

  def __init__(self, success=None,):
    self.success = success

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.LIST:
          self.success = []
          (_etype53, _size50) = iprot.readListBegin()
          for _i54 in xrange(_size50):
            _elem55 = ThreadStackTrace()
            _elem55.read(iprot)
            self.success.append(_elem55)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('getThreadDump_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.LIST, 0)
      oprot.writeListBegin(TType.STRUCT, len(self.success))
      for iter56 in self.success:
        iter56.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class getAllMetrics_args(object):
  """
  Attributes:
   - ctx
  """

  thrift_spec = (
    None, # 0
    None, # 1
    None, # 2
    None, # 3
    None, # 4
    None, # 5
    None, # 6
    None, # 7
    None, # 8
    None, # 9
    (10, TType.STRUCT, 'ctx', (RequestContext, RequestContext.thrift_spec), None, ), # 10
  )

  def __init__(self, ctx=None,):
    self.ctx = ctx

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 10:
        if ftype == TType.STRUCT:
          self.ctx = RequestContext()
          self.ctx.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('getAllMetrics_args')
    if self.ctx is not None:
      oprot.writeFieldBegin('ctx', TType.STRUCT, 10)
      self.ctx.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class getAllMetrics_result(object):
  """
  Attributes:
   - success
   - err
  """

  thrift_spec = (
    (0, TType.LIST, 'success', (TType.STRUCT,(MetricsContext, MetricsContext.thrift_spec)), None, ), # 0
    (1, TType.STRUCT, 'err', (IOException, IOException.thrift_spec), None, ), # 1
  )

  def __init__(self, success=None, err=None,):
    self.success = success
    self.err = err

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.LIST:
          self.success = []
          (_etype60, _size57) = iprot.readListBegin()
          for _i61 in xrange(_size57):
            _elem62 = MetricsContext()
            _elem62.read(iprot)
            self.success.append(_elem62)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 1:
        if ftype == TType.STRUCT:
          self.err = IOException()
          self.err.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('getAllMetrics_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.LIST, 0)
      oprot.writeListBegin(TType.STRUCT, len(self.success))
      for iter63 in self.success:
        iter63.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.err is not None:
      oprot.writeFieldBegin('err', TType.STRUCT, 1)
      self.err.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class getMetricsContext_args(object):
  """
  Attributes:
   - ctx
   - contextName
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'contextName', None, None, ), # 1
    None, # 2
    None, # 3
    None, # 4
    None, # 5
    None, # 6
    None, # 7
    None, # 8
    None, # 9
    (10, TType.STRUCT, 'ctx', (RequestContext, RequestContext.thrift_spec), None, ), # 10
  )

  def __init__(self, ctx=None, contextName=None,):
    self.ctx = ctx
    self.contextName = contextName

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 10:
        if ftype == TType.STRUCT:
          self.ctx = RequestContext()
          self.ctx.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 1:
        if ftype == TType.STRING:
          self.contextName = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('getMetricsContext_args')
    if self.contextName is not None:
      oprot.writeFieldBegin('contextName', TType.STRING, 1)
      oprot.writeString(self.contextName)
      oprot.writeFieldEnd()
    if self.ctx is not None:
      oprot.writeFieldBegin('ctx', TType.STRUCT, 10)
      self.ctx.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class getMetricsContext_result(object):
  """
  Attributes:
   - success
   - err
  """

  thrift_spec = (
    (0, TType.STRUCT, 'success', (MetricsContext, MetricsContext.thrift_spec), None, ), # 0
    (1, TType.STRUCT, 'err', (IOException, IOException.thrift_spec), None, ), # 1
  )

  def __init__(self, success=None, err=None,):
    self.success = success
    self.err = err

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.STRUCT:
          self.success = MetricsContext()
          self.success.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 1:
        if ftype == TType.STRUCT:
          self.err = IOException()
          self.err.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('getMetricsContext_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.STRUCT, 0)
      self.success.write(oprot)
      oprot.writeFieldEnd()
    if self.err is not None:
      oprot.writeFieldBegin('err', TType.STRUCT, 1)
      self.err.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
