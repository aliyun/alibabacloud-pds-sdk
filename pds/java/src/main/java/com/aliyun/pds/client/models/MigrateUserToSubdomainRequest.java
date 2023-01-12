// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * MigrateUserToSubdomainRequest uc migrate user
 */
public class MigrateUserToSubdomainRequest extends TeaModel {
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

    public static MigrateUserToSubdomainRequest build(java.util.Map<String, ?> map) throws Exception {
        MigrateUserToSubdomainRequest self = new MigrateUserToSubdomainRequest();
        return TeaModel.build(map, self);
    }

    public MigrateUserToSubdomainRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public MigrateUserToSubdomainRequest setSubdomainId(String subdomainId) {
        this.subdomainId = subdomainId;
        return this;
    }
    public String getSubdomainId() {
        return this.subdomainId;
    }

    public MigrateUserToSubdomainRequest setUserId(String userId) {
        this.userId = userId;
        return this;
    }
    public String getUserId() {
        return this.userId;
    }

}
