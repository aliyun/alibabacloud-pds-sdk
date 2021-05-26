// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class UnionAuthentication extends TeaModel {
    @NameInMap("AuthenticationType")
    public String AuthenticationType;

    @NameInMap("CreatedAt")
    public Long CreatedAt;

    @NameInMap("Extra")
    public String Extra;

    @NameInMap("Identity")
    public String Identity;

    @NameInMap("Status")
    public String Status;

    @NameInMap("UnionID")
    public String UnionID;

    public static UnionAuthentication build(java.util.Map<String, ?> map) throws Exception {
        UnionAuthentication self = new UnionAuthentication();
        return TeaModel.build(map, self);
    }

    public UnionAuthentication setAuthenticationType(String AuthenticationType) {
        this.AuthenticationType = AuthenticationType;
        return this;
    }
    public String getAuthenticationType() {
        return this.AuthenticationType;
    }

    public UnionAuthentication setCreatedAt(Long CreatedAt) {
        this.CreatedAt = CreatedAt;
        return this;
    }
    public Long getCreatedAt() {
        return this.CreatedAt;
    }

    public UnionAuthentication setExtra(String Extra) {
        this.Extra = Extra;
        return this;
    }
    public String getExtra() {
        return this.Extra;
    }

    public UnionAuthentication setIdentity(String Identity) {
        this.Identity = Identity;
        return this;
    }
    public String getIdentity() {
        return this.Identity;
    }

    public UnionAuthentication setStatus(String Status) {
        this.Status = Status;
        return this;
    }
    public String getStatus() {
        return this.Status;
    }

    public UnionAuthentication setUnionID(String UnionID) {
        this.UnionID = UnionID;
        return this;
    }
    public String getUnionID() {
        return this.UnionID;
    }

}
