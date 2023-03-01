// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class AggregationsGroup extends TeaModel {
    @NameInMap("count")
    public Long count;

    @NameInMap("value")
    public String value;

    public static AggregationsGroup build(java.util.Map<String, ?> map) throws Exception {
        AggregationsGroup self = new AggregationsGroup();
        return TeaModel.build(map, self);
    }

    public AggregationsGroup setCount(Long count) {
        this.count = count;
        return this;
    }
    public Long getCount() {
        return this.count;
    }

    public AggregationsGroup setValue(String value) {
        this.value = value;
        return this;
    }
    public String getValue() {
        return this.value;
    }

}
