// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class UpdateGroupRequest extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    // 描述
    @NameInMap("description")
    public String description;

    // group id
    @NameInMap("group_id")
    public String groupId;

    // 名称
    @NameInMap("group_name")
    @Validation(required = true)
    public String groupName;

    // 是否是根group
    @NameInMap("is_root")
    public Boolean isRoot;

    // subdomain id
    @NameInMap("subdomain_id")
    public String subdomainId;

    public static UpdateGroupRequest build(java.util.Map<String, ?> map) throws Exception {
        UpdateGroupRequest self = new UpdateGroupRequest();
        return TeaModel.build(map, self);
    }

    public UpdateGroupRequest setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public UpdateGroupRequest setDescription(String description) {
        this.description = description;
        return this;
    }
    public String getDescription() {
        return this.description;
    }

    public UpdateGroupRequest setGroupId(String groupId) {
        this.groupId = groupId;
        return this;
    }
    public String getGroupId() {
        return this.groupId;
    }

    public UpdateGroupRequest setGroupName(String groupName) {
        this.groupName = groupName;
        return this;
    }
    public String getGroupName() {
        return this.groupName;
    }

    public UpdateGroupRequest setIsRoot(Boolean isRoot) {
        this.isRoot = isRoot;
        return this;
    }
    public Boolean getIsRoot() {
        return this.isRoot;
    }

    public UpdateGroupRequest setSubdomainId(String subdomainId) {
        this.subdomainId = subdomainId;
        return this;
    }
    public String getSubdomainId() {
        return this.subdomainId;
    }

}
