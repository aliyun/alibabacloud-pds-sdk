// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * RollbackUserFromSubdomainRequest uc migrate user
 */
public class RollbackUserFromSubdomainRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    /**
     * <p>subdomain_id</p>
     */
    @NameInMap("subdomain_id")
    public String subdomainId;

    /**
     * <p>user_id</p>
     */
    @NameInMap("user_id")
    public String userId;

    public static RollbackUserFromSubdomainRequest build(java.util.Map<String, ?> map) throws Exception {
        RollbackUserFromSubdomainRequest self = new RollbackUserFromSubdomainRequest();
        return TeaModel.build(map, self);
    }

    public RollbackUserFromSubdomainRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public RollbackUserFromSubdomainRequest setSubdomainId(String subdomainId) {
        this.subdomainId = subdomainId;
        return this;
    }
    public String getSubdomainId() {
        return this.subdomainId;
    }

    public RollbackUserFromSubdomainRequest setUserId(String userId) {
        this.userId = userId;
        return this;
    }
    public String getUserId() {
        return this.userId;
    }

}
