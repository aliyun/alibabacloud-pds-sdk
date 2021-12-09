// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 表示用户或团队
 */
public class Identity extends TeaModel {
    // 用户或团队的ID
    @NameInMap("identity_id")
    @Validation(required = true)
    public String identityId;

    // 显示名称
    @NameInMap("identity_name")
    public String identityName;

    // 类型，目前可传：IT_User(用户)、IT_Group(团队)
    @NameInMap("identity_type")
    @Validation(required = true)
    public String identityType;

    public static Identity build(java.util.Map<String, ?> map) throws Exception {
        Identity self = new Identity();
        return TeaModel.build(map, self);
    }

    public Identity setIdentityId(String identityId) {
        this.identityId = identityId;
        return this;
    }
    public String getIdentityId() {
        return this.identityId;
    }

    public Identity setIdentityName(String identityName) {
        this.identityName = identityName;
        return this;
    }
    public String getIdentityName() {
        return this.identityName;
    }

    public Identity setIdentityType(String identityType) {
        this.identityType = identityType;
        return this;
    }
    public String getIdentityType() {
        return this.identityType;
    }

}
