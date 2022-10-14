// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class ListGroupRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    @NameInMap("extra_return_info")
    public java.util.List<String> extraReturnInfo;

    // 分页获取的数量，默认为100
    @NameInMap("limit")
    public Integer limit;

    // 游标
    @NameInMap("marker")
    public String marker;

    // 列举 subdomain 下的group
    @NameInMap("subdomain_id")
    public String subdomainId;

    public static ListGroupRequest build(java.util.Map<String, ?> map) throws Exception {
        ListGroupRequest self = new ListGroupRequest();
        return TeaModel.build(map, self);
    }

    public ListGroupRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public ListGroupRequest setExtraReturnInfo(java.util.List<String> extraReturnInfo) {
        this.extraReturnInfo = extraReturnInfo;
        return this;
    }
    public java.util.List<String> getExtraReturnInfo() {
        return this.extraReturnInfo;
    }

    public ListGroupRequest setLimit(Integer limit) {
        this.limit = limit;
        return this;
    }
    public Integer getLimit() {
        return this.limit;
    }

    public ListGroupRequest setMarker(String marker) {
        this.marker = marker;
        return this;
    }
    public String getMarker() {
        return this.marker;
    }

    public ListGroupRequest setSubdomainId(String subdomainId) {
        this.subdomainId = subdomainId;
        return this;
    }
    public String getSubdomainId() {
        return this.subdomainId;
    }

}
