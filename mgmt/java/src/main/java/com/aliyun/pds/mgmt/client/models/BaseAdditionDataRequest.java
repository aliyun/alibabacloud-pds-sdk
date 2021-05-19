// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class BaseAdditionDataRequest extends TeaModel {
    // addition_data
    @NameInMap("addition_data")
    public java.util.Map<String, ?> additionData;

    public static BaseAdditionDataRequest build(java.util.Map<String, ?> map) throws Exception {
        BaseAdditionDataRequest self = new BaseAdditionDataRequest();
        return TeaModel.build(map, self);
    }

    public BaseAdditionDataRequest setAdditionData(java.util.Map<String, ?> additionData) {
        this.additionData = additionData;
        return this;
    }
    public java.util.Map<String, ?> getAdditionData() {
        return this.additionData;
    }

}
