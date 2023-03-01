// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class ShareLogDetail extends TeaModel {
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
     * <p>parent_path</p>
     */
    @NameInMap("parent_path")
    public String parentPath;

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

    /**
     * <p>share_to_id</p>
     */
    @NameInMap("share_to_id")
    public String shareToId;

    /**
     * <p>share_to_name</p>
     */
    @NameInMap("share_to_name")
    public String shareToName;

    /**
     * <p>share_to_type</p>
     */
    @NameInMap("share_to_type")
    public String shareToType;

    /**
     * <p>type</p>
     */
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
