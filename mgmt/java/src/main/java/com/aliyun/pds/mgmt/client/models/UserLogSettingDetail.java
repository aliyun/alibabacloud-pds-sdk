// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class UserLogSettingDetail extends TeaModel {
    // name
    @NameInMap("name")
    public String name;

    // role_id
    @NameInMap("role_id")
    public String roleId;

    public static UserLogSettingDetail build(java.util.Map<String, ?> map) throws Exception {
        UserLogSettingDetail self = new UserLogSettingDetail();
        return TeaModel.build(map, self);
    }

    public UserLogSettingDetail setName(String name) {
        this.name = name;
        return this;
    }
    public String getName() {
        return this.name;
    }

    public UserLogSettingDetail setRoleId(String roleId) {
        this.roleId = roleId;
        return this;
    }
    public String getRoleId() {
        return this.roleId;
    }

}
