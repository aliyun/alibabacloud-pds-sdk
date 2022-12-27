// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 从value只支持string升级为支持所有类型的附加数据，按需升级
 */
public class BaseAdditionDataV2Request extends TeaModel {
    /**
     * <p>addition_data</p>
     */
    @NameInMap("addition_data")
    public java.util.Map<String, ?> additionData;

    public static BaseAdditionDataV2Request build(java.util.Map<String, ?> map) throws Exception {
        BaseAdditionDataV2Request self = new BaseAdditionDataV2Request();
        return TeaModel.build(map, self);
    }

    public BaseAdditionDataV2Request setAdditionData(java.util.Map<String, ?> additionData) {
        this.additionData = additionData;
        return this;
    }
    public java.util.Map<String, ?> getAdditionData() {
        return this.additionData;
    }

}
