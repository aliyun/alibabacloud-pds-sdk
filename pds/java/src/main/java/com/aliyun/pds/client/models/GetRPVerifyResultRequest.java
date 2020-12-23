// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class GetRPVerifyResultRequest extends TeaModel {
    // User ID, 当前访问的用户
    @NameInMap("user_id")
    @Validation(required = true)
    public String userId;

    public static GetRPVerifyResultRequest build(java.util.Map<String, ?> map) throws Exception {
        GetRPVerifyResultRequest self = new GetRPVerifyResultRequest();
        return TeaModel.build(map, self);
    }

    public GetRPVerifyResultRequest setUserId(String userId) {
        this.userId = userId;
        return this;
    }
    public String getUserId() {
        return this.userId;
    }

}
