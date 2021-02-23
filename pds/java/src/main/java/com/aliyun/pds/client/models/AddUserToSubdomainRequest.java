// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * Add user to subdomain request
 */
public class AddUserToSubdomainRequest extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    // subdomain id
    @NameInMap("subdomain_id")
    public String subdomainId;

    // 用户 ID
    @NameInMap("user_id")
    @Validation(required = true)
    public String userId;

    public static AddUserToSubdomainRequest build(java.util.Map<String, ?> map) throws Exception {
        AddUserToSubdomainRequest self = new AddUserToSubdomainRequest();
        return TeaModel.build(map, self);
    }

    public AddUserToSubdomainRequest setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public AddUserToSubdomainRequest setSubdomainId(String subdomainId) {
        this.subdomainId = subdomainId;
        return this;
    }
    public String getSubdomainId() {
        return this.subdomainId;
    }

    public AddUserToSubdomainRequest setUserId(String userId) {
        this.userId = userId;
        return this;
    }
    public String getUserId() {
        return this.userId;
    }

}
