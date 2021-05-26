// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class DomainSuperAdminConfig extends TeaModel {
    @NameInMap("phone_number")
    public String phoneNumber;

    @NameInMap("phone_region")
    public String phoneRegion;

    @NameInMap("user_id")
    public String userId;

    public static DomainSuperAdminConfig build(java.util.Map<String, ?> map) throws Exception {
        DomainSuperAdminConfig self = new DomainSuperAdminConfig();
        return TeaModel.build(map, self);
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

    public DomainSuperAdminConfig setUserId(String userId) {
        this.userId = userId;
        return this;
    }
    public String getUserId() {
        return this.userId;
    }

}
