// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class ShareLogSettingDetail extends TeaModel {
    /**
     * <p>disinherit_sub_group</p>
     */
    @NameInMap("disinherit_sub_group")
    public Boolean disinheritSubGroup;

    /**
     * <p>expiration</p>
     */
    @NameInMap("expiration")
    public String expiration;

    /**
     * <p>permissions</p>
     */
    @NameInMap("permissions")
    public java.util.List<String> permissions;

    /**
     * <p>role_id</p>
     */
    @NameInMap("role_id")
    public String roleId;

    /**
     * <p>role_name</p>
     */
    @NameInMap("role_name")
    public String roleName;

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

    public ShareLogSettingDetail setRoleName(String roleName) {
        this.roleName = roleName;
        return this;
    }
    public String getRoleName() {
        return this.roleName;
    }

}
