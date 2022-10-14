// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class HasMembershipResponse extends TeaModel {
    @NameInMap("result")
    public Boolean result;

    public static HasMembershipResponse build(java.util.Map<String, ?> map) throws Exception {
        HasMembershipResponse self = new HasMembershipResponse();
        return TeaModel.build(map, self);
    }

    public HasMembershipResponse setResult(Boolean result) {
        this.result = result;
        return this;
    }
    public Boolean getResult() {
        return this.result;
    }

}
