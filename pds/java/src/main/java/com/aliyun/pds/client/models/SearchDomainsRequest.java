// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * search domain request
 */
public class SearchDomainsRequest extends TeaModel {
    // 分页大小
    @NameInMap("limit")
    @Validation(maximum = 100, minimum = 1)
    public Integer limit;

    // 查询游标
    @NameInMap("marker")
    public String marker;

    // domain名称，模糊匹配
    @NameInMap("name")
    public String name;

    // 排序规则
    @NameInMap("order_by")
    public String orderBy;

    public static SearchDomainsRequest build(java.util.Map<String, ?> map) throws Exception {
        SearchDomainsRequest self = new SearchDomainsRequest();
        return TeaModel.build(map, self);
    }

    public SearchDomainsRequest setLimit(Integer limit) {
        this.limit = limit;
        return this;
    }
    public Integer getLimit() {
        return this.limit;
    }

    public SearchDomainsRequest setMarker(String marker) {
        this.marker = marker;
        return this;
    }
    public String getMarker() {
        return this.marker;
    }

    public SearchDomainsRequest setName(String name) {
        this.name = name;
        return this;
    }
    public String getName() {
        return this.name;
    }

    public SearchDomainsRequest setOrderBy(String orderBy) {
        this.orderBy = orderBy;
        return this;
    }
    public String getOrderBy() {
        return this.orderBy;
    }

}
