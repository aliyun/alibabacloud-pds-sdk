// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class ListDirectParentMembershipsRequest extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    // 分页获取的数量，默认为100
    @NameInMap("limit")
    public Integer limit;

    // 游标
    @NameInMap("marker")
    public String marker;

    @NameInMap("member_type")
    public String memberType;

    @NameInMap("sub_group_id")
    public String subGroupId;

    // subdomain id
    @NameInMap("subdomain_id")
    public String subdomainId;

    @NameInMap("user_id")
    public String userId;

    public static ListDirectParentMembershipsRequest build(java.util.Map<String, ?> map) throws Exception {
        ListDirectParentMembershipsRequest self = new ListDirectParentMembershipsRequest();
        return TeaModel.build(map, self);
    }

    public ListDirectParentMembershipsRequest setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public ListDirectParentMembershipsRequest setLimit(Integer limit) {
        this.limit = limit;
        return this;
    }
    public Integer getLimit() {
        return this.limit;
    }

    public ListDirectParentMembershipsRequest setMarker(String marker) {
        this.marker = marker;
        return this;
    }
    public String getMarker() {
        return this.marker;
    }

    public ListDirectParentMembershipsRequest setMemberType(String memberType) {
        this.memberType = memberType;
        return this;
    }
    public String getMemberType() {
        return this.memberType;
    }

    public ListDirectParentMembershipsRequest setSubGroupId(String subGroupId) {
        this.subGroupId = subGroupId;
        return this;
    }
    public String getSubGroupId() {
        return this.subGroupId;
    }

    public ListDirectParentMembershipsRequest setSubdomainId(String subdomainId) {
        this.subdomainId = subdomainId;
        return this;
    }
    public String getSubdomainId() {
        return this.subdomainId;
    }

    public ListDirectParentMembershipsRequest setUserId(String userId) {
        this.userId = userId;
        return this;
    }
    public String getUserId() {
        return this.userId;
    }

}
