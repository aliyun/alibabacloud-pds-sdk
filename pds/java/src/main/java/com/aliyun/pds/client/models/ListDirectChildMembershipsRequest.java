// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class ListDirectChildMembershipsRequest extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    // group id
    @NameInMap("group_id")
    public String groupId;

    // 分页获取的数量，默认为100
    @NameInMap("limit")
    public Integer limit;

    // 游标
    @NameInMap("marker")
    public String marker;

    // 角色，可选值，["", "member", "admin"], ""表示获取所有类型
    @NameInMap("member_type")
    public String memberType;

    // subdomain id
    @NameInMap("subdomain_id")
    public String subdomainId;

    public static ListDirectChildMembershipsRequest build(java.util.Map<String, ?> map) throws Exception {
        ListDirectChildMembershipsRequest self = new ListDirectChildMembershipsRequest();
        return TeaModel.build(map, self);
    }

    public ListDirectChildMembershipsRequest setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public ListDirectChildMembershipsRequest setGroupId(String groupId) {
        this.groupId = groupId;
        return this;
    }
    public String getGroupId() {
        return this.groupId;
    }

    public ListDirectChildMembershipsRequest setLimit(Integer limit) {
        this.limit = limit;
        return this;
    }
    public Integer getLimit() {
        return this.limit;
    }

    public ListDirectChildMembershipsRequest setMarker(String marker) {
        this.marker = marker;
        return this;
    }
    public String getMarker() {
        return this.marker;
    }

    public ListDirectChildMembershipsRequest setMemberType(String memberType) {
        this.memberType = memberType;
        return this;
    }
    public String getMemberType() {
        return this.memberType;
    }

    public ListDirectChildMembershipsRequest setSubdomainId(String subdomainId) {
        this.subdomainId = subdomainId;
        return this;
    }
    public String getSubdomainId() {
        return this.subdomainId;
    }

}
