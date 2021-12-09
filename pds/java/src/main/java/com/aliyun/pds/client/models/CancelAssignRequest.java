// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 取消角色请求
 */
public class CancelAssignRequest extends TeaModel {
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

    public static CancelAssignRequest build(java.util.Map<String, ?> map) throws Exception {
        CancelAssignRequest self = new CancelAssignRequest();
        return TeaModel.build(map, self);
    }

    public CancelAssignRequest setIdentity(Identity identity) {
        this.identity = identity;
        return this;
    }
    public Identity getIdentity() {
        return this.identity;
    }

    public CancelAssignRequest setManageResourceId(String manageResourceId) {
        this.manageResourceId = manageResourceId;
        return this;
    }
    public String getManageResourceId() {
        return this.manageResourceId;
    }

    public CancelAssignRequest setManageResourceType(String manageResourceType) {
        this.manageResourceType = manageResourceType;
        return this;
    }
    public String getManageResourceType() {
        return this.manageResourceType;
    }

    public CancelAssignRequest setRoleId(String roleId) {
        this.roleId = roleId;
        return this;
    }
    public String getRoleId() {
        return this.roleId;
    }

    public CancelAssignRequest setSubdomainId(String subdomainId) {
        this.subdomainId = subdomainId;
        return this;
    }
    public String getSubdomainId() {
        return this.subdomainId;
    }

}
