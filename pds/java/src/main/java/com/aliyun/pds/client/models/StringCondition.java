// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 *
 */
public class StringCondition extends TeaModel {
    @NameInMap("vpc_id")
    public java.util.List<String> vpcId;

    public static StringCondition build(java.util.Map<String, ?> map) throws Exception {
        StringCondition self = new StringCondition();
        return TeaModel.build(map, self);
    }

    public StringCondition setVpcId(java.util.List<String> vpcId) {
        this.vpcId = vpcId;
        return this;
    }
    public java.util.List<String> getVpcId() {
        return this.vpcId;
    }

}
