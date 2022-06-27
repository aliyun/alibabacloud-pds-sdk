// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * Search user and group request
 */
public class SearchUserAndGroupRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    // 搜索实体对象类型
    @NameInMap("identity_type_list")
    public java.util.List<String> identityTypeList;

    // 每页大小限制
    @NameInMap("limit")
    @Validation(maximum = 100, minimum = 1)
    public Integer limit;

    // 翻页标记
    @NameInMap("marker")
    public String marker;

    // 名称前缀搜索，Group名，或者用户昵称
    @NameInMap("name")
    public String name;

    // 名称模糊搜索，Group名，或者用户昵称
    @NameInMap("name_for_fuzzy")
    public String nameForFuzzy;

    // 用户状态
    // status: enabled
    @NameInMap("status")
    public String status;

    // subdomain id
    @NameInMap("subdomain_id")
    public String subdomainId;

    public static SearchUserAndGroupRequest build(java.util.Map<String, ?> map) throws Exception {
        SearchUserAndGroupRequest self = new SearchUserAndGroupRequest();
        return TeaModel.build(map, self);
    }

    public SearchUserAndGroupRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public SearchUserAndGroupRequest setIdentityTypeList(java.util.List<String> identityTypeList) {
        this.identityTypeList = identityTypeList;
        return this;
    }
    public java.util.List<String> getIdentityTypeList() {
        return this.identityTypeList;
    }

    public SearchUserAndGroupRequest setLimit(Integer limit) {
        this.limit = limit;
        return this;
    }
    public Integer getLimit() {
        return this.limit;
    }

    public SearchUserAndGroupRequest setMarker(String marker) {
        this.marker = marker;
        return this;
    }
    public String getMarker() {
        return this.marker;
    }

    public SearchUserAndGroupRequest setName(String name) {
        this.name = name;
        return this;
    }
    public String getName() {
        return this.name;
    }

    public SearchUserAndGroupRequest setNameForFuzzy(String nameForFuzzy) {
        this.nameForFuzzy = nameForFuzzy;
        return this;
    }
    public String getNameForFuzzy() {
        return this.nameForFuzzy;
    }

    public SearchUserAndGroupRequest setStatus(String status) {
        this.status = status;
        return this;
    }
    public String getStatus() {
        return this.status;
    }

    public SearchUserAndGroupRequest setSubdomainId(String subdomainId) {
        this.subdomainId = subdomainId;
        return this;
    }
    public String getSubdomainId() {
        return this.subdomainId;
    }

}
