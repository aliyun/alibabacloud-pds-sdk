// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class UnionDomainUserBind extends TeaModel {
    @NameInMap("AuthenticationType")
    public String AuthenticationType;

    @NameInMap("DomainID")
    public String DomainID;

    @NameInMap("Extra")
    public String Extra;

    @NameInMap("Identity")
    public String Identity;

    @NameInMap("UnionID")
    public String UnionID;

    @NameInMap("UserID")
    public String UserID;

    public static UnionDomainUserBind build(java.util.Map<String, ?> map) throws Exception {
        UnionDomainUserBind self = new UnionDomainUserBind();
        return TeaModel.build(map, self);
    }

    public UnionDomainUserBind setAuthenticationType(String AuthenticationType) {
        this.AuthenticationType = AuthenticationType;
        return this;
    }
    public String getAuthenticationType() {
        return this.AuthenticationType;
    }

    public UnionDomainUserBind setDomainID(String DomainID) {
        this.DomainID = DomainID;
        return this;
    }
    public String getDomainID() {
        return this.DomainID;
    }

    public UnionDomainUserBind setExtra(String Extra) {
        this.Extra = Extra;
        return this;
    }
    public String getExtra() {
        return this.Extra;
    }

    public UnionDomainUserBind setIdentity(String Identity) {
        this.Identity = Identity;
        return this;
    }
    public String getIdentity() {
        return this.Identity;
    }

    public UnionDomainUserBind setUnionID(String UnionID) {
        this.UnionID = UnionID;
        return this;
    }
    public String getUnionID() {
        return this.UnionID;
    }

    public UnionDomainUserBind setUserID(String UserID) {
        this.UserID = UserID;
        return this;
    }
    public String getUserID() {
        return this.UserID;
    }

}
