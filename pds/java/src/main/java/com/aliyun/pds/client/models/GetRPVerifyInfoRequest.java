// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class GetRPVerifyInfoRequest extends TeaModel {
    // Need Identity Info, 是否获取脱敏的身份信息
    @NameInMap("need_identity_info")
    public Boolean needIdentityInfo;

    // User ID, 当前访问的用户
    @NameInMap("user_id")
    @Validation(required = true)
    public String userId;

    public static GetRPVerifyInfoRequest build(java.util.Map<String, ?> map) throws Exception {
        GetRPVerifyInfoRequest self = new GetRPVerifyInfoRequest();
        return TeaModel.build(map, self);
    }

    public GetRPVerifyInfoRequest setNeedIdentityInfo(Boolean needIdentityInfo) {
        this.needIdentityInfo = needIdentityInfo;
        return this;
    }
    public Boolean getNeedIdentityInfo() {
        return this.needIdentityInfo;
    }

    public GetRPVerifyInfoRequest setUserId(String userId) {
        this.userId = userId;
        return this;
    }
    public String getUserId() {
        return this.userId;
    }

}
