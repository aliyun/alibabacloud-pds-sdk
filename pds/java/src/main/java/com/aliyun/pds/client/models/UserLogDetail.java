// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class UserLogDetail extends TeaModel {
    // email
    @NameInMap("email")
    public String email;

    // name
    @NameInMap("name")
    public String name;

    // phone
    @NameInMap("phone")
    public String phone;

    // role_id
    @NameInMap("role_id")
    public String roleId;

    @NameInMap("update_to")
    public UserLogSettingDetail updateTo;

    public static UserLogDetail build(java.util.Map<String, ?> map) throws Exception {
        UserLogDetail self = new UserLogDetail();
        return TeaModel.build(map, self);
    }

    public UserLogDetail setEmail(String email) {
        this.email = email;
        return this;
    }
    public String getEmail() {
        return this.email;
    }

    public UserLogDetail setName(String name) {
        this.name = name;
        return this;
    }
    public String getName() {
        return this.name;
    }

    public UserLogDetail setPhone(String phone) {
        this.phone = phone;
        return this;
    }
    public String getPhone() {
        return this.phone;
    }

    public UserLogDetail setRoleId(String roleId) {
        this.roleId = roleId;
        return this;
    }
    public String getRoleId() {
        return this.roleId;
    }

    public UserLogDetail setUpdateTo(UserLogSettingDetail updateTo) {
        this.updateTo = updateTo;
        return this;
    }
    public UserLogSettingDetail getUpdateTo() {
        return this.updateTo;
    }

}
