// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class AssignRoleSettingDetail extends TeaModel {
    /**
     * <p>manage_resource_id</p>
     */
    @NameInMap("manage_resource_id")
    public String manageResourceId;

    /**
     * <p>manage_resource_name</p>
     */
    @NameInMap("manage_resource_name")
    public String manageResourceName;

    /**
     * <p>manage_resource_type</p>
     */
    @NameInMap("manage_resource_type")
    public String manageResourceType;

    /**
     * <p>role_id</p>
     */
    @NameInMap("role_id")
    public String roleId;

    public static AssignRoleSettingDetail build(java.util.Map<String, ?> map) throws Exception {
        AssignRoleSettingDetail self = new AssignRoleSettingDetail();
        return TeaModel.build(map, self);
    }

    public AssignRoleSettingDetail setManageResourceId(String manageResourceId) {
        this.manageResourceId = manageResourceId;
        return this;
    }
    public String getManageResourceId() {
        return this.manageResourceId;
    }

    public AssignRoleSettingDetail setManageResourceName(String manageResourceName) {
        this.manageResourceName = manageResourceName;
        return this;
    }
    public String getManageResourceName() {
        return this.manageResourceName;
    }

    public AssignRoleSettingDetail setManageResourceType(String manageResourceType) {
        this.manageResourceType = manageResourceType;
        return this;
    }
    public String getManageResourceType() {
        return this.manageResourceType;
    }

    public AssignRoleSettingDetail setRoleId(String roleId) {
        this.roleId = roleId;
        return this;
    }
    public String getRoleId() {
        return this.roleId;
    }

}
