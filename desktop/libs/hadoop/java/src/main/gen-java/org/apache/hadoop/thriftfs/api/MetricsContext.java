/**
 * Autogenerated by Thrift Compiler (0.9.0)
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */
package org.apache.hadoop.thriftfs.api;

import org.apache.thrift.scheme.IScheme;
import org.apache.thrift.scheme.SchemeFactory;
import org.apache.thrift.scheme.StandardScheme;

import org.apache.thrift.scheme.TupleScheme;
import org.apache.thrift.protocol.TTupleProtocol;
import org.apache.thrift.protocol.TProtocolException;
import org.apache.thrift.EncodingUtils;
import org.apache.thrift.TException;
import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;
import java.util.EnumMap;
import java.util.Set;
import java.util.HashSet;
import java.util.EnumSet;
import java.util.Collections;
import java.util.BitSet;
import java.nio.ByteBuffer;
import java.util.Arrays;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class MetricsContext implements org.apache.thrift.TBase<MetricsContext, MetricsContext._Fields>, java.io.Serializable, Cloneable {
  private static final org.apache.thrift.protocol.TStruct STRUCT_DESC = new org.apache.thrift.protocol.TStruct("MetricsContext");

  private static final org.apache.thrift.protocol.TField NAME_FIELD_DESC = new org.apache.thrift.protocol.TField("name", org.apache.thrift.protocol.TType.STRING, (short)1);
  private static final org.apache.thrift.protocol.TField IS_MONITORING_FIELD_DESC = new org.apache.thrift.protocol.TField("isMonitoring", org.apache.thrift.protocol.TType.BOOL, (short)2);
  private static final org.apache.thrift.protocol.TField PERIOD_FIELD_DESC = new org.apache.thrift.protocol.TField("period", org.apache.thrift.protocol.TType.I32, (short)3);
  private static final org.apache.thrift.protocol.TField RECORDS_FIELD_DESC = new org.apache.thrift.protocol.TField("records", org.apache.thrift.protocol.TType.MAP, (short)4);

  private static final Map<Class<? extends IScheme>, SchemeFactory> schemes = new HashMap<Class<? extends IScheme>, SchemeFactory>();
  static {
    schemes.put(StandardScheme.class, new MetricsContextStandardSchemeFactory());
    schemes.put(TupleScheme.class, new MetricsContextTupleSchemeFactory());
  }

  public String name; // required
  public boolean isMonitoring; // required
  public int period; // required
  public Map<String,List<MetricsRecord>> records; // required

  /** The set of fields this struct contains, along with convenience methods for finding and manipulating them. */
  public enum _Fields implements org.apache.thrift.TFieldIdEnum {
    NAME((short)1, "name"),
    IS_MONITORING((short)2, "isMonitoring"),
    PERIOD((short)3, "period"),
    RECORDS((short)4, "records");

    private static final Map<String, _Fields> byName = new HashMap<String, _Fields>();

    static {
      for (_Fields field : EnumSet.allOf(_Fields.class)) {
        byName.put(field.getFieldName(), field);
      }
    }

    /**
     * Find the _Fields constant that matches fieldId, or null if its not found.
     */
    public static _Fields findByThriftId(int fieldId) {
      switch(fieldId) {
        case 1: // NAME
          return NAME;
        case 2: // IS_MONITORING
          return IS_MONITORING;
        case 3: // PERIOD
          return PERIOD;
        case 4: // RECORDS
          return RECORDS;
        default:
          return null;
      }
    }

    /**
     * Find the _Fields constant that matches fieldId, throwing an exception
     * if it is not found.
     */
    public static _Fields findByThriftIdOrThrow(int fieldId) {
      _Fields fields = findByThriftId(fieldId);
      if (fields == null) throw new IllegalArgumentException("Field " + fieldId + " doesn't exist!");
      return fields;
    }

    /**
     * Find the _Fields constant that matches name, or null if its not found.
     */
    public static _Fields findByName(String name) {
      return byName.get(name);
    }

    private final short _thriftId;
    private final String _fieldName;

    _Fields(short thriftId, String fieldName) {
      _thriftId = thriftId;
      _fieldName = fieldName;
    }

    public short getThriftFieldId() {
      return _thriftId;
    }

    public String getFieldName() {
      return _fieldName;
    }
  }

  // isset id assignments
  private static final int __ISMONITORING_ISSET_ID = 0;
  private static final int __PERIOD_ISSET_ID = 1;
  private byte __isset_bitfield = 0;
  public static final Map<_Fields, org.apache.thrift.meta_data.FieldMetaData> metaDataMap;
  static {
    Map<_Fields, org.apache.thrift.meta_data.FieldMetaData> tmpMap = new EnumMap<_Fields, org.apache.thrift.meta_data.FieldMetaData>(_Fields.class);
    tmpMap.put(_Fields.NAME, new org.apache.thrift.meta_data.FieldMetaData("name", org.apache.thrift.TFieldRequirementType.DEFAULT, 
        new org.apache.thrift.meta_data.FieldValueMetaData(org.apache.thrift.protocol.TType.STRING)));
    tmpMap.put(_Fields.IS_MONITORING, new org.apache.thrift.meta_data.FieldMetaData("isMonitoring", org.apache.thrift.TFieldRequirementType.DEFAULT, 
        new org.apache.thrift.meta_data.FieldValueMetaData(org.apache.thrift.protocol.TType.BOOL)));
    tmpMap.put(_Fields.PERIOD, new org.apache.thrift.meta_data.FieldMetaData("period", org.apache.thrift.TFieldRequirementType.DEFAULT, 
        new org.apache.thrift.meta_data.FieldValueMetaData(org.apache.thrift.protocol.TType.I32)));
    tmpMap.put(_Fields.RECORDS, new org.apache.thrift.meta_data.FieldMetaData("records", org.apache.thrift.TFieldRequirementType.DEFAULT, 
        new org.apache.thrift.meta_data.MapMetaData(org.apache.thrift.protocol.TType.MAP, 
            new org.apache.thrift.meta_data.FieldValueMetaData(org.apache.thrift.protocol.TType.STRING), 
            new org.apache.thrift.meta_data.ListMetaData(org.apache.thrift.protocol.TType.LIST, 
                new org.apache.thrift.meta_data.StructMetaData(org.apache.thrift.protocol.TType.STRUCT, MetricsRecord.class)))));
    metaDataMap = Collections.unmodifiableMap(tmpMap);
    org.apache.thrift.meta_data.FieldMetaData.addStructMetaDataMap(MetricsContext.class, metaDataMap);
  }

  public MetricsContext() {
  }

  public MetricsContext(
    String name,
    boolean isMonitoring,
    int period,
    Map<String,List<MetricsRecord>> records)
  {
    this();
    this.name = name;
    this.isMonitoring = isMonitoring;
    setIsMonitoringIsSet(true);
    this.period = period;
    setPeriodIsSet(true);
    this.records = records;
  }

  /**
   * Performs a deep copy on <i>other</i>.
   */
  public MetricsContext(MetricsContext other) {
    __isset_bitfield = other.__isset_bitfield;
    if (other.isSetName()) {
      this.name = other.name;
    }
    this.isMonitoring = other.isMonitoring;
    this.period = other.period;
    if (other.isSetRecords()) {
      Map<String,List<MetricsRecord>> __this__records = new HashMap<String,List<MetricsRecord>>();
      for (Map.Entry<String, List<MetricsRecord>> other_element : other.records.entrySet()) {

        String other_element_key = other_element.getKey();
        List<MetricsRecord> other_element_value = other_element.getValue();

        String __this__records_copy_key = other_element_key;

        List<MetricsRecord> __this__records_copy_value = new ArrayList<MetricsRecord>();
        for (MetricsRecord other_element_value_element : other_element_value) {
          __this__records_copy_value.add(new MetricsRecord(other_element_value_element));
        }

        __this__records.put(__this__records_copy_key, __this__records_copy_value);
      }
      this.records = __this__records;
    }
  }

  public MetricsContext deepCopy() {
    return new MetricsContext(this);
  }

  @Override
  public void clear() {
    this.name = null;
    setIsMonitoringIsSet(false);
    this.isMonitoring = false;
    setPeriodIsSet(false);
    this.period = 0;
    this.records = null;
  }

  public String getName() {
    return this.name;
  }

  public MetricsContext setName(String name) {
    this.name = name;
    return this;
  }

  public void unsetName() {
    this.name = null;
  }

  /** Returns true if field name is set (has been assigned a value) and false otherwise */
  public boolean isSetName() {
    return this.name != null;
  }

  public void setNameIsSet(boolean value) {
    if (!value) {
      this.name = null;
    }
  }

  public boolean isIsMonitoring() {
    return this.isMonitoring;
  }

  public MetricsContext setIsMonitoring(boolean isMonitoring) {
    this.isMonitoring = isMonitoring;
    setIsMonitoringIsSet(true);
    return this;
  }

  public void unsetIsMonitoring() {
    __isset_bitfield = EncodingUtils.clearBit(__isset_bitfield, __ISMONITORING_ISSET_ID);
  }

  /** Returns true if field isMonitoring is set (has been assigned a value) and false otherwise */
  public boolean isSetIsMonitoring() {
    return EncodingUtils.testBit(__isset_bitfield, __ISMONITORING_ISSET_ID);
  }

  public void setIsMonitoringIsSet(boolean value) {
    __isset_bitfield = EncodingUtils.setBit(__isset_bitfield, __ISMONITORING_ISSET_ID, value);
  }

  public int getPeriod() {
    return this.period;
  }

  public MetricsContext setPeriod(int period) {
    this.period = period;
    setPeriodIsSet(true);
    return this;
  }

  public void unsetPeriod() {
    __isset_bitfield = EncodingUtils.clearBit(__isset_bitfield, __PERIOD_ISSET_ID);
  }

  /** Returns true if field period is set (has been assigned a value) and false otherwise */
  public boolean isSetPeriod() {
    return EncodingUtils.testBit(__isset_bitfield, __PERIOD_ISSET_ID);
  }

  public void setPeriodIsSet(boolean value) {
    __isset_bitfield = EncodingUtils.setBit(__isset_bitfield, __PERIOD_ISSET_ID, value);
  }

  public int getRecordsSize() {
    return (this.records == null) ? 0 : this.records.size();
  }

  public void putToRecords(String key, List<MetricsRecord> val) {
    if (this.records == null) {
      this.records = new HashMap<String,List<MetricsRecord>>();
    }
    this.records.put(key, val);
  }

  public Map<String,List<MetricsRecord>> getRecords() {
    return this.records;
  }

  public MetricsContext setRecords(Map<String,List<MetricsRecord>> records) {
    this.records = records;
    return this;
  }

  public void unsetRecords() {
    this.records = null;
  }

  /** Returns true if field records is set (has been assigned a value) and false otherwise */
  public boolean isSetRecords() {
    return this.records != null;
  }

  public void setRecordsIsSet(boolean value) {
    if (!value) {
      this.records = null;
    }
  }

  public void setFieldValue(_Fields field, Object value) {
    switch (field) {
    case NAME:
      if (value == null) {
        unsetName();
      } else {
        setName((String)value);
      }
      break;

    case IS_MONITORING:
      if (value == null) {
        unsetIsMonitoring();
      } else {
        setIsMonitoring((Boolean)value);
      }
      break;

    case PERIOD:
      if (value == null) {
        unsetPeriod();
      } else {
        setPeriod((Integer)value);
      }
      break;

    case RECORDS:
      if (value == null) {
        unsetRecords();
      } else {
        setRecords((Map<String,List<MetricsRecord>>)value);
      }
      break;

    }
  }

  public Object getFieldValue(_Fields field) {
    switch (field) {
    case NAME:
      return getName();

    case IS_MONITORING:
      return Boolean.valueOf(isIsMonitoring());

    case PERIOD:
      return Integer.valueOf(getPeriod());

    case RECORDS:
      return getRecords();

    }
    throw new IllegalStateException();
  }

  /** Returns true if field corresponding to fieldID is set (has been assigned a value) and false otherwise */
  public boolean isSet(_Fields field) {
    if (field == null) {
      throw new IllegalArgumentException();
    }

    switch (field) {
    case NAME:
      return isSetName();
    case IS_MONITORING:
      return isSetIsMonitoring();
    case PERIOD:
      return isSetPeriod();
    case RECORDS:
      return isSetRecords();
    }
    throw new IllegalStateException();
  }

  @Override
  public boolean equals(Object that) {
    if (that == null)
      return false;
    if (that instanceof MetricsContext)
      return this.equals((MetricsContext)that);
    return false;
  }

  public boolean equals(MetricsContext that) {
    if (that == null)
      return false;

    boolean this_present_name = true && this.isSetName();
    boolean that_present_name = true && that.isSetName();
    if (this_present_name || that_present_name) {
      if (!(this_present_name && that_present_name))
        return false;
      if (!this.name.equals(that.name))
        return false;
    }

    boolean this_present_isMonitoring = true;
    boolean that_present_isMonitoring = true;
    if (this_present_isMonitoring || that_present_isMonitoring) {
      if (!(this_present_isMonitoring && that_present_isMonitoring))
        return false;
      if (this.isMonitoring != that.isMonitoring)
        return false;
    }

    boolean this_present_period = true;
    boolean that_present_period = true;
    if (this_present_period || that_present_period) {
      if (!(this_present_period && that_present_period))
        return false;
      if (this.period != that.period)
        return false;
    }

    boolean this_present_records = true && this.isSetRecords();
    boolean that_present_records = true && that.isSetRecords();
    if (this_present_records || that_present_records) {
      if (!(this_present_records && that_present_records))
        return false;
      if (!this.records.equals(that.records))
        return false;
    }

    return true;
  }

  @Override
  public int hashCode() {
    return 0;
  }

  public int compareTo(MetricsContext other) {
    if (!getClass().equals(other.getClass())) {
      return getClass().getName().compareTo(other.getClass().getName());
    }

    int lastComparison = 0;
    MetricsContext typedOther = (MetricsContext)other;

    lastComparison = Boolean.valueOf(isSetName()).compareTo(typedOther.isSetName());
    if (lastComparison != 0) {
      return lastComparison;
    }
    if (isSetName()) {
      lastComparison = org.apache.thrift.TBaseHelper.compareTo(this.name, typedOther.name);
      if (lastComparison != 0) {
        return lastComparison;
      }
    }
    lastComparison = Boolean.valueOf(isSetIsMonitoring()).compareTo(typedOther.isSetIsMonitoring());
    if (lastComparison != 0) {
      return lastComparison;
    }
    if (isSetIsMonitoring()) {
      lastComparison = org.apache.thrift.TBaseHelper.compareTo(this.isMonitoring, typedOther.isMonitoring);
      if (lastComparison != 0) {
        return lastComparison;
      }
    }
    lastComparison = Boolean.valueOf(isSetPeriod()).compareTo(typedOther.isSetPeriod());
    if (lastComparison != 0) {
      return lastComparison;
    }
    if (isSetPeriod()) {
      lastComparison = org.apache.thrift.TBaseHelper.compareTo(this.period, typedOther.period);
      if (lastComparison != 0) {
        return lastComparison;
      }
    }
    lastComparison = Boolean.valueOf(isSetRecords()).compareTo(typedOther.isSetRecords());
    if (lastComparison != 0) {
      return lastComparison;
    }
    if (isSetRecords()) {
      lastComparison = org.apache.thrift.TBaseHelper.compareTo(this.records, typedOther.records);
      if (lastComparison != 0) {
        return lastComparison;
      }
    }
    return 0;
  }

  public _Fields fieldForId(int fieldId) {
    return _Fields.findByThriftId(fieldId);
  }

  public void read(org.apache.thrift.protocol.TProtocol iprot) throws org.apache.thrift.TException {
    schemes.get(iprot.getScheme()).getScheme().read(iprot, this);
  }

  public void write(org.apache.thrift.protocol.TProtocol oprot) throws org.apache.thrift.TException {
    schemes.get(oprot.getScheme()).getScheme().write(oprot, this);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder("MetricsContext(");
    boolean first = true;

    sb.append("name:");
    if (this.name == null) {
      sb.append("null");
    } else {
      sb.append(this.name);
    }
    first = false;
    if (!first) sb.append(", ");
    sb.append("isMonitoring:");
    sb.append(this.isMonitoring);
    first = false;
    if (!first) sb.append(", ");
    sb.append("period:");
    sb.append(this.period);
    first = false;
    if (!first) sb.append(", ");
    sb.append("records:");
    if (this.records == null) {
      sb.append("null");
    } else {
      sb.append(this.records);
    }
    first = false;
    sb.append(")");
    return sb.toString();
  }

  public void validate() throws org.apache.thrift.TException {
    // check for required fields
    // check for sub-struct validity
  }

  private void writeObject(java.io.ObjectOutputStream out) throws java.io.IOException {
    try {
      write(new org.apache.thrift.protocol.TCompactProtocol(new org.apache.thrift.transport.TIOStreamTransport(out)));
    } catch (org.apache.thrift.TException te) {
      throw new java.io.IOException(te);
    }
  }

  private void readObject(java.io.ObjectInputStream in) throws java.io.IOException, ClassNotFoundException {
    try {
      // it doesn't seem like you should have to do this, but java serialization is wacky, and doesn't call the default constructor.
      __isset_bitfield = 0;
      read(new org.apache.thrift.protocol.TCompactProtocol(new org.apache.thrift.transport.TIOStreamTransport(in)));
    } catch (org.apache.thrift.TException te) {
      throw new java.io.IOException(te);
    }
  }

  private static class MetricsContextStandardSchemeFactory implements SchemeFactory {
    public MetricsContextStandardScheme getScheme() {
      return new MetricsContextStandardScheme();
    }
  }

  private static class MetricsContextStandardScheme extends StandardScheme<MetricsContext> {

    public void read(org.apache.thrift.protocol.TProtocol iprot, MetricsContext struct) throws org.apache.thrift.TException {
      org.apache.thrift.protocol.TField schemeField;
      iprot.readStructBegin();
      while (true)
      {
        schemeField = iprot.readFieldBegin();
        if (schemeField.type == org.apache.thrift.protocol.TType.STOP) { 
          break;
        }
        switch (schemeField.id) {
          case 1: // NAME
            if (schemeField.type == org.apache.thrift.protocol.TType.STRING) {
              struct.name = iprot.readString();
              struct.setNameIsSet(true);
            } else { 
              org.apache.thrift.protocol.TProtocolUtil.skip(iprot, schemeField.type);
            }
            break;
          case 2: // IS_MONITORING
            if (schemeField.type == org.apache.thrift.protocol.TType.BOOL) {
              struct.isMonitoring = iprot.readBool();
              struct.setIsMonitoringIsSet(true);
            } else { 
              org.apache.thrift.protocol.TProtocolUtil.skip(iprot, schemeField.type);
            }
            break;
          case 3: // PERIOD
            if (schemeField.type == org.apache.thrift.protocol.TType.I32) {
              struct.period = iprot.readI32();
              struct.setPeriodIsSet(true);
            } else { 
              org.apache.thrift.protocol.TProtocolUtil.skip(iprot, schemeField.type);
            }
            break;
          case 4: // RECORDS
            if (schemeField.type == org.apache.thrift.protocol.TType.MAP) {
              {
                org.apache.thrift.protocol.TMap _map38 = iprot.readMapBegin();
                struct.records = new HashMap<String,List<MetricsRecord>>(2*_map38.size);
                for (int _i39 = 0; _i39 < _map38.size; ++_i39)
                {
                  String _key40; // required
                  List<MetricsRecord> _val41; // required
                  _key40 = iprot.readString();
                  {
                    org.apache.thrift.protocol.TList _list42 = iprot.readListBegin();
                    _val41 = new ArrayList<MetricsRecord>(_list42.size);
                    for (int _i43 = 0; _i43 < _list42.size; ++_i43)
                    {
                      MetricsRecord _elem44; // required
                      _elem44 = new MetricsRecord();
                      _elem44.read(iprot);
                      _val41.add(_elem44);
                    }
                    iprot.readListEnd();
                  }
                  struct.records.put(_key40, _val41);
                }
                iprot.readMapEnd();
              }
              struct.setRecordsIsSet(true);
            } else { 
              org.apache.thrift.protocol.TProtocolUtil.skip(iprot, schemeField.type);
            }
            break;
          default:
            org.apache.thrift.protocol.TProtocolUtil.skip(iprot, schemeField.type);
        }
        iprot.readFieldEnd();
      }
      iprot.readStructEnd();

      // check for required fields of primitive type, which can't be checked in the validate method
      struct.validate();
    }

    public void write(org.apache.thrift.protocol.TProtocol oprot, MetricsContext struct) throws org.apache.thrift.TException {
      struct.validate();

      oprot.writeStructBegin(STRUCT_DESC);
      if (struct.name != null) {
        oprot.writeFieldBegin(NAME_FIELD_DESC);
        oprot.writeString(struct.name);
        oprot.writeFieldEnd();
      }
      oprot.writeFieldBegin(IS_MONITORING_FIELD_DESC);
      oprot.writeBool(struct.isMonitoring);
      oprot.writeFieldEnd();
      oprot.writeFieldBegin(PERIOD_FIELD_DESC);
      oprot.writeI32(struct.period);
      oprot.writeFieldEnd();
      if (struct.records != null) {
        oprot.writeFieldBegin(RECORDS_FIELD_DESC);
        {
          oprot.writeMapBegin(new org.apache.thrift.protocol.TMap(org.apache.thrift.protocol.TType.STRING, org.apache.thrift.protocol.TType.LIST, struct.records.size()));
          for (Map.Entry<String, List<MetricsRecord>> _iter45 : struct.records.entrySet())
          {
            oprot.writeString(_iter45.getKey());
            {
              oprot.writeListBegin(new org.apache.thrift.protocol.TList(org.apache.thrift.protocol.TType.STRUCT, _iter45.getValue().size()));
              for (MetricsRecord _iter46 : _iter45.getValue())
              {
                _iter46.write(oprot);
              }
              oprot.writeListEnd();
            }
          }
          oprot.writeMapEnd();
        }
        oprot.writeFieldEnd();
      }
      oprot.writeFieldStop();
      oprot.writeStructEnd();
    }

  }

  private static class MetricsContextTupleSchemeFactory implements SchemeFactory {
    public MetricsContextTupleScheme getScheme() {
      return new MetricsContextTupleScheme();
    }
  }

  private static class MetricsContextTupleScheme extends TupleScheme<MetricsContext> {

    @Override
    public void write(org.apache.thrift.protocol.TProtocol prot, MetricsContext struct) throws org.apache.thrift.TException {
      TTupleProtocol oprot = (TTupleProtocol) prot;
      BitSet optionals = new BitSet();
      if (struct.isSetName()) {
        optionals.set(0);
      }
      if (struct.isSetIsMonitoring()) {
        optionals.set(1);
      }
      if (struct.isSetPeriod()) {
        optionals.set(2);
      }
      if (struct.isSetRecords()) {
        optionals.set(3);
      }
      oprot.writeBitSet(optionals, 4);
      if (struct.isSetName()) {
        oprot.writeString(struct.name);
      }
      if (struct.isSetIsMonitoring()) {
        oprot.writeBool(struct.isMonitoring);
      }
      if (struct.isSetPeriod()) {
        oprot.writeI32(struct.period);
      }
      if (struct.isSetRecords()) {
        {
          oprot.writeI32(struct.records.size());
          for (Map.Entry<String, List<MetricsRecord>> _iter47 : struct.records.entrySet())
          {
            oprot.writeString(_iter47.getKey());
            {
              oprot.writeI32(_iter47.getValue().size());
              for (MetricsRecord _iter48 : _iter47.getValue())
              {
                _iter48.write(oprot);
              }
            }
          }
        }
      }
    }

    @Override
    public void read(org.apache.thrift.protocol.TProtocol prot, MetricsContext struct) throws org.apache.thrift.TException {
      TTupleProtocol iprot = (TTupleProtocol) prot;
      BitSet incoming = iprot.readBitSet(4);
      if (incoming.get(0)) {
        struct.name = iprot.readString();
        struct.setNameIsSet(true);
      }
      if (incoming.get(1)) {
        struct.isMonitoring = iprot.readBool();
        struct.setIsMonitoringIsSet(true);
      }
      if (incoming.get(2)) {
        struct.period = iprot.readI32();
        struct.setPeriodIsSet(true);
      }
      if (incoming.get(3)) {
        {
          org.apache.thrift.protocol.TMap _map49 = new org.apache.thrift.protocol.TMap(org.apache.thrift.protocol.TType.STRING, org.apache.thrift.protocol.TType.LIST, iprot.readI32());
          struct.records = new HashMap<String,List<MetricsRecord>>(2*_map49.size);
          for (int _i50 = 0; _i50 < _map49.size; ++_i50)
          {
            String _key51; // required
            List<MetricsRecord> _val52; // required
            _key51 = iprot.readString();
            {
              org.apache.thrift.protocol.TList _list53 = new org.apache.thrift.protocol.TList(org.apache.thrift.protocol.TType.STRUCT, iprot.readI32());
              _val52 = new ArrayList<MetricsRecord>(_list53.size);
              for (int _i54 = 0; _i54 < _list53.size; ++_i54)
              {
                MetricsRecord _elem55; // required
                _elem55 = new MetricsRecord();
                _elem55.read(iprot);
                _val52.add(_elem55);
              }
            }
            struct.records.put(_key51, _val52);
          }
        }
        struct.setRecordsIsSet(true);
      }
    }
  }

}

