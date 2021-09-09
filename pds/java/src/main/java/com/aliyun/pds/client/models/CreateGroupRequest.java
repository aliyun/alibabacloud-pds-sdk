// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class CreateGroupRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    // 描述
    @NameInMap("description")
    public String description;

    // 名称
    @NameInMap("group_name")
    @Validation(required = true)
    public String groupName;

    // 是否是根group
    @NameInMap("is_root")
    public Boolean isRoot;

    // parent group id
    @NameInMap("parent_group_id")
    public String parentGroupId;

    // subdomain id
    @NameInMap("subdomain_id")
    public String subdomainId;

    public static CreateGroupRequest build(java.util.Map<String, ?> map) throws Exception {
        CreateGroupRequest self = new CreateGroupRequest();
        return TeaModel.build(map, self);
    }

    public CreateGroupRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public CreateGroupRequest setDescription(String description) {
        this.description = description;
        return this;
    }
    public String getDescription() {
        return this.description;
    }

    public CreateGroupRequest setGroupName(String groupName) {
        this.groupName = groupName;
        return this;
    }
    public String getGroupName() {
        return this.groupName;
    }

    public CreateGroupRequest setIsRoot(Boolean isRoot) {
        this.isRoot = isRoot;
        return this;
    }
    public Boolean getIsRoot() {
        return this.isRoot;
    }

    public CreateGroupRequest setParentGroupId(String parentGroupId) {
        this.parentGroupId = parentGroupId;
        return this;
    }
    public String getParentGroupId() {
        return this.parentGroupId;
    }

    public CreateGroupRequest setSubdomainId(String subdomainId) {
        this.subdomainId = subdomainId;
        return this;
    }
    public String getSubdomainId() {
        return this.subdomainId;
    }

}
