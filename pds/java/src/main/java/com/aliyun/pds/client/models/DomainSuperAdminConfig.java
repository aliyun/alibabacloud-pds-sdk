// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class DomainSuperAdminConfig extends TeaModel {
    @NameInMap("extra")
    public String extra;

    @NameInMap("identity")
    public String identity;

    @NameInMap("phone_number")
    public String phoneNumber;

    @NameInMap("phone_region")
    public String phoneRegion;

    @NameInMap("type")
    public String type;

    @NameInMap("user_id")
    public String userId;

    public static DomainSuperAdminConfig build(java.util.Map<String, ?> map) throws Exception {
        DomainSuperAdminConfig self = new DomainSuperAdminConfig();
        return TeaModel.build(map, self);
    }

    public DomainSuperAdminConfig setExtra(String extra) {
        this.extra = extra;
        return this;
    }
    public String getExtra() {
        return this.extra;
    }

    public DomainSuperAdminConfig setIdentity(String identity) {
        this.identity = identity;
        return this;
    }
    public String getIdentity() {
        return this.identity;
    }

    public DomainSuperAdminConfig setPhoneNumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
        return this;
    }
    public String getPhoneNumber() {
        return this.phoneNumber;
    }

    public DomainSuperAdminConfig setPhoneRegion(String phoneRegion) {
        this.phoneRegion = phoneRegion;
        return this;
    }
    public String getPhoneRegion() {
        return this.phoneRegion;
    }

    public DomainSuperAdminConfig setType(String type) {
        this.type = type;
        return this;
    }
    public String getType() {
        return this.type;
    }

    public DomainSuperAdminConfig setUserId(String userId) {
        this.userId = userId;
        return this;
    }
    public String getUserId() {
        return this.userId;
    }

}
