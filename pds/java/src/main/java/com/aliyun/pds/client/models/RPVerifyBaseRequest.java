// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 *
 */
public class RPVerifyBaseRequest extends TeaModel {
    // User ID, 当前访问的用户
    @NameInMap("user_id")
    @Validation(required = true)
    public String userId;

    public static RPVerifyBaseRequest build(java.util.Map<String, ?> map) throws Exception {
        RPVerifyBaseRequest self = new RPVerifyBaseRequest();
        return TeaModel.build(map, self);
    }

    public RPVerifyBaseRequest setUserId(String userId) {
        this.userId = userId;
        return this;
    }
    public String getUserId() {
        return this.userId;
    }

}
