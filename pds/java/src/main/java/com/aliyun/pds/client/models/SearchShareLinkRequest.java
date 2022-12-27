// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * search_share_link request
 */
public class SearchShareLinkRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    /**
     * <p>categories</p>
     */
    @NameInMap("categories")
    public java.util.List<String> categories;

    /**
     * <p>creators</p>
     */
    @NameInMap("creators")
    public java.util.List<String> creators;

    /**
     * <p>limit</p>
     */
    @NameInMap("limit")
    @Validation(maximum = 100, minimum = 1)
    public Integer limit;

    /**
     * <p>marker</p>
     */
    @NameInMap("marker")
    public String marker;

    /**
     * <p>order_by</p>
     */
    @NameInMap("order_by")
    public String orderBy;

    /**
     * <p>order_direction</p>
     */
    @NameInMap("order_direction")
    public String orderDirection;

    /**
     * <p>query</p>
     */
    @NameInMap("query")
    @Validation(maxLength = 4096)
    public String query;

    /**
     * <p>return_total_count 是否返回查询总数</p>
     */
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

    public SearchShareLinkRequest setCategories(java.util.List<String> categories) {
        this.categories = categories;
        return this;
    }
    public java.util.List<String> getCategories() {
        return this.categories;
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
