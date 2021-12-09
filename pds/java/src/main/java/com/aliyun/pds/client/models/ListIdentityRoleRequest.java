// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 列举用户或团队的角色列表请求
 */
public class ListIdentityRoleRequest extends TeaModel {
    @NameInMap("identity")
    @Validation(required = true)
    public Identity identity;

    // 是否包含所属父级团队的角色
    @NameInMap("include_group_role")
    @Validation(required = true)
    public Boolean includeGroupRole;

    @NameInMap("subdomain_id")
    public String subdomainId;

    public static ListIdentityRoleRequest build(java.util.Map<String, ?> map) throws Exception {
        ListIdentityRoleRequest self = new ListIdentityRoleRequest();
        return TeaModel.build(map, self);
    }

    public ListIdentityRoleRequest setIdentity(Identity identity) {
        this.identity = identity;
        return this;
    }
    public Identity getIdentity() {
        return this.identity;
    }

    public ListIdentityRoleRequest setIncludeGroupRole(Boolean includeGroupRole) {
        this.includeGroupRole = includeGroupRole;
        return this;
    }
    public Boolean getIncludeGroupRole() {
        return this.includeGroupRole;
    }

    public ListIdentityRoleRequest setSubdomainId(String subdomainId) {
        this.subdomainId = subdomainId;
        return this;
    }
    public String getSubdomainId() {
        return this.subdomainId;
    }

}
