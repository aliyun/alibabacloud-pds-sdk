// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class GetRPVerifyTokenRequest extends TeaModel {
    /**
     * <p>User ID, 当前访问的用户</p>
     */
    @NameInMap("user_id")
    @Validation(required = true)
    public String userId;

    public static GetRPVerifyTokenRequest build(java.util.Map<String, ?> map) throws Exception {
        GetRPVerifyTokenRequest self = new GetRPVerifyTokenRequest();
        return TeaModel.build(map, self);
    }

    public GetRPVerifyTokenRequest setUserId(String userId) {
        this.userId = userId;
        return this;
    }
    public String getUserId() {
        return this.userId;
    }

}
