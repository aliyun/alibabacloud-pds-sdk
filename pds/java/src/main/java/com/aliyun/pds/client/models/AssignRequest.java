// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 分配角色请求
 */
public class AssignRequest extends TeaModel {
    @NameInMap("identity")
    @Validation(required = true)
    public Identity identity;

    // 管辖的资源ID
    @NameInMap("manage_resource_id")
    @Validation(required = true)
    public String manageResourceId;

    // 管辖的资源类型，目前只支持团队: IT_Group
    @NameInMap("manage_resource_type")
    @Validation(required = true)
    public String manageResourceType;

    // 授予的角色，目前支持：SystemGroupAdmin(团队管理员)
    @NameInMap("role_id")
    @Validation(required = true)
    public String roleId;

    @NameInMap("subdomain_id")
    public String subdomainId;

    public static AssignRequest build(java.util.Map<String, ?> map) throws Exception {
        AssignRequest self = new AssignRequest();
        return TeaModel.build(map, self);
    }

    public AssignRequest setIdentity(Identity identity) {
        this.identity = identity;
        return this;
    }
    public Identity getIdentity() {
        return this.identity;
    }

    public AssignRequest setManageResourceId(String manageResourceId) {
        this.manageResourceId = manageResourceId;
        return this;
    }
    public String getManageResourceId() {
        return this.manageResourceId;
    }

    public AssignRequest setManageResourceType(String manageResourceType) {
        this.manageResourceType = manageResourceType;
        return this;
    }
    public String getManageResourceType() {
        return this.manageResourceType;
    }

    public AssignRequest setRoleId(String roleId) {
        this.roleId = roleId;
        return this;
    }
    public String getRoleId() {
        return this.roleId;
    }

    public AssignRequest setSubdomainId(String subdomainId) {
        this.subdomainId = subdomainId;
        return this;
    }
    public String getSubdomainId() {
        return this.subdomainId;
    }

}
