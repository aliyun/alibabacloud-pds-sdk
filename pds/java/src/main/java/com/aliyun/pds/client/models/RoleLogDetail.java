// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class RoleLogDetail extends TeaModel {
    // manage_resource_id
    @NameInMap("manage_resource_id")
    public String manageResourceId;

    // manage_resource_name
    @NameInMap("manage_resource_name")
    public String manageResourceName;

    // manage_resource_type
    @NameInMap("manage_resource_type")
    public String manageResourceType;

    // member_type
    @NameInMap("member_type")
    public String memberType;

    // role_id
    @NameInMap("role_id")
    public String roleId;

    // role_tag_description
    @NameInMap("role_tag_description")
    public String roleTagDescription;

    // role_tag_name
    @NameInMap("role_tag_name")
    public String roleTagName;

    @NameInMap("update_to")
    public RoleLogSettingDetail updateTo;

    public static RoleLogDetail build(java.util.Map<String, ?> map) throws Exception {
        RoleLogDetail self = new RoleLogDetail();
        return TeaModel.build(map, self);
    }

    public RoleLogDetail setManageResourceId(String manageResourceId) {
        this.manageResourceId = manageResourceId;
        return this;
    }
    public String getManageResourceId() {
        return this.manageResourceId;
    }

    public RoleLogDetail setManageResourceName(String manageResourceName) {
        this.manageResourceName = manageResourceName;
        return this;
    }
    public String getManageResourceName() {
        return this.manageResourceName;
    }

    public RoleLogDetail setManageResourceType(String manageResourceType) {
        this.manageResourceType = manageResourceType;
        return this;
    }
    public String getManageResourceType() {
        return this.manageResourceType;
    }

    public RoleLogDetail setMemberType(String memberType) {
        this.memberType = memberType;
        return this;
    }
    public String getMemberType() {
        return this.memberType;
    }

    public RoleLogDetail setRoleId(String roleId) {
        this.roleId = roleId;
        return this;
    }
    public String getRoleId() {
        return this.roleId;
    }

    public RoleLogDetail setRoleTagDescription(String roleTagDescription) {
        this.roleTagDescription = roleTagDescription;
        return this;
    }
    public String getRoleTagDescription() {
        return this.roleTagDescription;
    }

    public RoleLogDetail setRoleTagName(String roleTagName) {
        this.roleTagName = roleTagName;
        return this;
    }
    public String getRoleTagName() {
        return this.roleTagName;
    }

    public RoleLogDetail setUpdateTo(RoleLogSettingDetail updateTo) {
        this.updateTo = updateTo;
        return this;
    }
    public RoleLogSettingDetail getUpdateTo() {
        return this.updateTo;
    }

}
