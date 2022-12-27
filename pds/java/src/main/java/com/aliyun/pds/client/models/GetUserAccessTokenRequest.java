// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class GetUserAccessTokenRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    /**
     * <p>subdomain ID</p>
     */
    @NameInMap("subdomain_id")
    public String subdomainId;

    /**
     * <p>用户 ID</p>
     */
    @NameInMap("user_id")
    @Validation(required = true)
    public String userId;

    public static GetUserAccessTokenRequest build(java.util.Map<String, ?> map) throws Exception {
        GetUserAccessTokenRequest self = new GetUserAccessTokenRequest();
        return TeaModel.build(map, self);
    }

    public GetUserAccessTokenRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public GetUserAccessTokenRequest setSubdomainId(String subdomainId) {
        this.subdomainId = subdomainId;
        return this;
    }
    public String getSubdomainId() {
        return this.subdomainId;
    }

    public GetUserAccessTokenRequest setUserId(String userId) {
        this.userId = userId;
        return this;
    }
    public String getUserId() {
        return this.userId;
    }

}
