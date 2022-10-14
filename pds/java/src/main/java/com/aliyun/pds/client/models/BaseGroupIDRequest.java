// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class BaseGroupIDRequest extends TeaModel {
    // group id
    @NameInMap("group_id")
    public String groupId;

    // subdomain id
    @NameInMap("subdomain_id")
    public String subdomainId;

    public static BaseGroupIDRequest build(java.util.Map<String, ?> map) throws Exception {
        BaseGroupIDRequest self = new BaseGroupIDRequest();
        return TeaModel.build(map, self);
    }

    public BaseGroupIDRequest setGroupId(String groupId) {
        this.groupId = groupId;
        return this;
    }
    public String getGroupId() {
        return this.groupId;
    }

    public BaseGroupIDRequest setSubdomainId(String subdomainId) {
        this.subdomainId = subdomainId;
        return this;
    }
    public String getSubdomainId() {
        return this.subdomainId;
    }

}
