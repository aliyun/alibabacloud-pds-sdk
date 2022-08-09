// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 *
 */
public class ShareLogDetail extends TeaModel {
    // disinherit_sub_group
    @NameInMap("disinherit_sub_group")
    public Boolean disinheritSubGroup;

    // expiration
    @NameInMap("expiration")
    public String expiration;

    // parent_path
    @NameInMap("parent_path")
    public String parentPath;

    // permissions
    @NameInMap("permissions")
    public java.util.List<String> permissions;

    // role_id
    @NameInMap("role_id")
    public String roleId;

    // role_name
    @NameInMap("role_name")
    public String roleName;

    // share_to_id
    @NameInMap("share_to_id")
    public String shareToId;

    // share_to_name
    @NameInMap("share_to_name")
    public String shareToName;

    // share_to_type
    @NameInMap("share_to_type")
    public String shareToType;

    // type
    @NameInMap("type")
    public String type;

    @NameInMap("update_to")
    public ShareLogSettingDetail updateTo;

    public static ShareLogDetail build(java.util.Map<String, ?> map) throws Exception {
        ShareLogDetail self = new ShareLogDetail();
        return TeaModel.build(map, self);
    }

    public ShareLogDetail setDisinheritSubGroup(Boolean disinheritSubGroup) {
        this.disinheritSubGroup = disinheritSubGroup;
        return this;
    }
    public Boolean getDisinheritSubGroup() {
        return this.disinheritSubGroup;
    }

    public ShareLogDetail setExpiration(String expiration) {
        this.expiration = expiration;
        return this;
    }
    public String getExpiration() {
        return this.expiration;
    }

    public ShareLogDetail setParentPath(String parentPath) {
        this.parentPath = parentPath;
        return this;
    }
    public String getParentPath() {
        return this.parentPath;
    }

    public ShareLogDetail setPermissions(java.util.List<String> permissions) {
        this.permissions = permissions;
        return this;
    }
    public java.util.List<String> getPermissions() {
        return this.permissions;
    }

    public ShareLogDetail setRoleId(String roleId) {
        this.roleId = roleId;
        return this;
    }
    public String getRoleId() {
        return this.roleId;
    }

    public ShareLogDetail setRoleName(String roleName) {
        this.roleName = roleName;
        return this;
    }
    public String getRoleName() {
        return this.roleName;
    }

    public ShareLogDetail setShareToId(String shareToId) {
        this.shareToId = shareToId;
        return this;
    }
    public String getShareToId() {
        return this.shareToId;
    }

    public ShareLogDetail setShareToName(String shareToName) {
        this.shareToName = shareToName;
        return this;
    }
    public String getShareToName() {
        return this.shareToName;
    }

    public ShareLogDetail setShareToType(String shareToType) {
        this.shareToType = shareToType;
        return this;
    }
    public String getShareToType() {
        return this.shareToType;
    }

    public ShareLogDetail setType(String type) {
        this.type = type;
        return this;
    }
    public String getType() {
        return this.type;
    }

    public ShareLogDetail setUpdateTo(ShareLogSettingDetail updateTo) {
        this.updateTo = updateTo;
        return this;
    }
    public ShareLogSettingDetail getUpdateTo() {
        return this.updateTo;
    }

}
