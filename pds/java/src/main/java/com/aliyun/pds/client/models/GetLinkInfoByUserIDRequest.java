// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class GetLinkInfoByUserIDRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    /**
     * <p>user ID</p>
     */
    @NameInMap("user_id")
    @Validation(required = true)
    public String userId;

    public static GetLinkInfoByUserIDRequest build(java.util.Map<String, ?> map) throws Exception {
        GetLinkInfoByUserIDRequest self = new GetLinkInfoByUserIDRequest();
        return TeaModel.build(map, self);
    }

    public GetLinkInfoByUserIDRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public GetLinkInfoByUserIDRequest setUserId(String userId) {
        this.userId = userId;
        return this;
    }
    public String getUserId() {
        return this.userId;
    }

}
