// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class SearchGroupRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    @NameInMap("extra_return_info")
    public java.util.List<String> extraReturnInfo;

    // group_name
    @NameInMap("group_name")
    public String groupName;

    // group_name_for_fuzzy
    @NameInMap("group_name_for_fuzzy")
    public String groupNameForFuzzy;

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

    public SearchGroupRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public SearchGroupRequest setExtraReturnInfo(java.util.List<String> extraReturnInfo) {
        this.extraReturnInfo = extraReturnInfo;
        return this;
    }
    public java.util.List<String> getExtraReturnInfo() {
        return this.extraReturnInfo;
    }

    public SearchGroupRequest setGroupName(String groupName) {
        this.groupName = groupName;
        return this;
    }
    public String getGroupName() {
        return this.groupName;
    }

    public SearchGroupRequest setGroupNameForFuzzy(String groupNameForFuzzy) {
        this.groupNameForFuzzy = groupNameForFuzzy;
        return this;
    }
    public String getGroupNameForFuzzy() {
        return this.groupNameForFuzzy;
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
