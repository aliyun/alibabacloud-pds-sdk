// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class Aggregation extends TeaModel {
    @NameInMap("field")
    public String field;

    @NameInMap("groups")
    public java.util.List<AggregationsGroup> groups;

    @NameInMap("operation")
    public String operation;

    @NameInMap("value")
    public Double value;

    public static Aggregation build(java.util.Map<String, ?> map) throws Exception {
        Aggregation self = new Aggregation();
        return TeaModel.build(map, self);
    }

    public Aggregation setField(String field) {
        this.field = field;
        return this;
    }
    public String getField() {
        return this.field;
    }

    public Aggregation setGroups(java.util.List<AggregationsGroup> groups) {
        this.groups = groups;
        return this;
    }
    public java.util.List<AggregationsGroup> getGroups() {
        return this.groups;
    }

    public Aggregation setOperation(String operation) {
        this.operation = operation;
        return this;
    }
    public String getOperation() {
        return this.operation;
    }

    public Aggregation setValue(Double value) {
        this.value = value;
        return this;
    }
    public Double getValue() {
        return this.value;
    }

}
