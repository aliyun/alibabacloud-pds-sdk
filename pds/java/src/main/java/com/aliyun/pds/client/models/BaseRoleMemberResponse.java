// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * List identity role response
 */
public class BaseRoleMemberResponse extends TeaModel {
    // 当前用户或团队分配的角色列表
    @NameInMap("assignment_list")
    @Validation(required = true)
    public java.util.List<BaseAssignmentResponse> assignmentList;

    // domain_id
    @NameInMap("domain_id")
    @Validation(required = true)
    public String domainId;

    @NameInMap("identity")
    @Validation(required = true)
    public Identity identity;

    // 查询的用户或团队的名称
    @NameInMap("identity_name")
    @Validation(required = true)
    public String identityName;

    // 是否为管理员
    @NameInMap("is_admin")
    @Validation(required = true)
    public Boolean isAdmin;

    @NameInMap("subdomain_id")
    public String subdomainId;

    public static BaseRoleMemberResponse build(java.util.Map<String, ?> map) throws Exception {
        BaseRoleMemberResponse self = new BaseRoleMemberResponse();
        return TeaModel.build(map, self);
    }

    public BaseRoleMemberResponse setAssignmentList(java.util.List<BaseAssignmentResponse> assignmentList) {
        this.assignmentList = assignmentList;
        return this;
    }
    public java.util.List<BaseAssignmentResponse> getAssignmentList() {
        return this.assignmentList;
    }

    public BaseRoleMemberResponse setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

    public BaseRoleMemberResponse setIdentity(Identity identity) {
        this.identity = identity;
        return this;
    }
    public Identity getIdentity() {
        return this.identity;
    }

    public BaseRoleMemberResponse setIdentityName(String identityName) {
        this.identityName = identityName;
        return this;
    }
    public String getIdentityName() {
        return this.identityName;
    }

    public BaseRoleMemberResponse setIsAdmin(Boolean isAdmin) {
        this.isAdmin = isAdmin;
        return this;
    }
    public Boolean getIsAdmin() {
        return this.isAdmin;
    }

    public BaseRoleMemberResponse setSubdomainId(String subdomainId) {
        this.subdomainId = subdomainId;
        return this;
    }
    public String getSubdomainId() {
        return this.subdomainId;
    }

}
