// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * search_share_link request
 */
public class SearchShareLinkRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    // creators
    // type: string
    @NameInMap("creators")
    public java.util.List<String> creators;

    // limit
    @NameInMap("limit")
    @Validation(maximum = 100, minimum = 1)
    public Integer limit;

    // marker
    @NameInMap("marker")
    public String marker;

    // order_by
    @NameInMap("order_by")
    public String orderBy;

    // order_direction
    @NameInMap("order_direction")
    public String orderDirection;

    // query
    @NameInMap("query")
    @Validation(maxLength = 4096)
    public String query;

    // return_total_count 是否返回查询总数
    @NameInMap("return_total_count")
    public Boolean returnTotalCount;

    public static SearchShareLinkRequest build(java.util.Map<String, ?> map) throws Exception {
        SearchShareLinkRequest self = new SearchShareLinkRequest();
        return TeaModel.build(map, self);
    }

    public SearchShareLinkRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public SearchShareLinkRequest setCreators(java.util.List<String> creators) {
        this.creators = creators;
        return this;
    }
    public java.util.List<String> getCreators() {
        return this.creators;
    }

    public SearchShareLinkRequest setLimit(Integer limit) {
        this.limit = limit;
        return this;
    }
    public Integer getLimit() {
        return this.limit;
    }

    public SearchShareLinkRequest setMarker(String marker) {
        this.marker = marker;
        return this;
    }
    public String getMarker() {
        return this.marker;
    }

    public SearchShareLinkRequest setOrderBy(String orderBy) {
        this.orderBy = orderBy;
        return this;
    }
    public String getOrderBy() {
        return this.orderBy;
    }

    public SearchShareLinkRequest setOrderDirection(String orderDirection) {
        this.orderDirection = orderDirection;
        return this;
    }
    public String getOrderDirection() {
        return this.orderDirection;
    }

    public SearchShareLinkRequest setQuery(String query) {
        this.query = query;
        return this;
    }
    public String getQuery() {
        return this.query;
    }

    public SearchShareLinkRequest setReturnTotalCount(Boolean returnTotalCount) {
        this.returnTotalCount = returnTotalCount;
        return this;
    }
    public Boolean getReturnTotalCount() {
        return this.returnTotalCount;
    }

}
