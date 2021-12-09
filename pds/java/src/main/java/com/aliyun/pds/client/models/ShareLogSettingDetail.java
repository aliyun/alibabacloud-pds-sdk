// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class ShareLogSettingDetail extends TeaModel {
    // disinherit_sub_group
    @NameInMap("disinherit_sub_group")
    public Boolean disinheritSubGroup;

    // expiration
    @NameInMap("expiration")
    public String expiration;

    // permissions
    @NameInMap("permissions")
    public java.util.List<String> permissions;

    // role_id
    @NameInMap("role_id")
    public String roleId;

    public static ShareLogSettingDetail build(java.util.Map<String, ?> map) throws Exception {
        ShareLogSettingDetail self = new ShareLogSettingDetail();
        return TeaModel.build(map, self);
    }

    public ShareLogSettingDetail setDisinheritSubGroup(Boolean disinheritSubGroup) {
        this.disinheritSubGroup = disinheritSubGroup;
        return this;
    }
    public Boolean getDisinheritSubGroup() {
        return this.disinheritSubGroup;
    }

    public ShareLogSettingDetail setExpiration(String expiration) {
        this.expiration = expiration;
        return this;
    }
    public String getExpiration() {
        return this.expiration;
    }

    public ShareLogSettingDetail setPermissions(java.util.List<String> permissions) {
        this.permissions = permissions;
        return this;
    }
    public java.util.List<String> getPermissions() {
        return this.permissions;
    }

    public ShareLogSettingDetail setRoleId(String roleId) {
        this.roleId = roleId;
        return this;
    }
    public String getRoleId() {
        return this.roleId;
    }

}
