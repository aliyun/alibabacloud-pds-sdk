// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class SearchGroupRequest extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    // group_name
    @NameInMap("group_name")
    public String groupName;

    // 分页获取的数量，默认为100
    @NameInMap("limit")
    public Integer limit;

    // 游标
    @NameInMap("marker")
    public String marker;

    // 列举 subdomain 下的group
    @NameInMap("subdomain_id")
    public String subdomainId;

    public static SearchGroupRequest build(java.util.Map<String, ?> map) throws Exception {
        SearchGroupRequest self = new SearchGroupRequest();
        return TeaModel.build(map, self);
    }

    public SearchGroupRequest setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public SearchGroupRequest setGroupName(String groupName) {
        this.groupName = groupName;
        return this;
    }
    public String getGroupName() {
        return this.groupName;
    }

    public SearchGroupRequest setLimit(Integer limit) {
        this.limit = limit;
        return this;
    }
    public Integer getLimit() {
        return this.limit;
    }

    public SearchGroupRequest setMarker(String marker) {
        this.marker = marker;
        return this;
    }
    public String getMarker() {
        return this.marker;
    }

    public SearchGroupRequest setSubdomainId(String subdomainId) {
        this.subdomainId = subdomainId;
        return this;
    }
    public String getSubdomainId() {
        return this.subdomainId;
    }

}
