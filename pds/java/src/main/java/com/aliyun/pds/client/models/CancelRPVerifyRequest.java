// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class CancelRPVerifyRequest extends TeaModel {
    // User ID, 当前访问的用户
    @NameInMap("user_id")
    @Validation(required = true)
    public String userId;

    public static CancelRPVerifyRequest build(java.util.Map<String, ?> map) throws Exception {
        CancelRPVerifyRequest self = new CancelRPVerifyRequest();
        return TeaModel.build(map, self);
    }

    public CancelRPVerifyRequest setUserId(String userId) {
        this.userId = userId;
        return this;
    }
    public String getUserId() {
        return this.userId;
    }

}
