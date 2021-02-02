// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class CNameStatus extends TeaModel {
    // binding state
    @NameInMap("bingding_state")
    @Validation(required = true)
    public String bingdingState;

    // legal state
    @NameInMap("legal_state")
    @Validation(required = true)
    public String legalState;

    // remark
    @NameInMap("remark")
    @Validation(required = true)
    public String remark;

    public static CNameStatus build(java.util.Map<String, ?> map) throws Exception {
        CNameStatus self = new CNameStatus();
        return TeaModel.build(map, self);
    }

    public CNameStatus setBingdingState(String bingdingState) {
        this.bingdingState = bingdingState;
        return this;
    }
    public String getBingdingState() {
        return this.bingdingState;
    }

    public CNameStatus setLegalState(String legalState) {
        this.legalState = legalState;
        return this;
    }
    public String getLegalState() {
        return this.legalState;
    }

    public CNameStatus setRemark(String remark) {
        this.remark = remark;
        return this;
    }
    public String getRemark() {
        return this.remark;
    }

}
