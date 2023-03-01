// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * Search view request
 */
public class SearchViewsRequest extends TeaModel {
    /**
     * <p>category</p>
     */
    @NameInMap("category")
    @Validation(required = true)
    public String category;

    /**
     * <p>每页大小限制</p>
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
     * <p>name</p>
     */
    @NameInMap("name")
    public String name;

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
     * <p>owner</p>
     */
    @NameInMap("owner")
    public String owner;

    /**
     * <p>return_total_count 是否返回查询总数</p>
     */
    @NameInMap("return_total_count")
    public Boolean returnTotalCount;

    /**
     * <p>user_id</p>
     */
    @NameInMap("user_id")
    public String userId;

    public static SearchViewsRequest build(java.util.Map<String, ?> map) throws Exception {
        SearchViewsRequest self = new SearchViewsRequest();
        return TeaModel.build(map, self);
    }

    public SearchViewsRequest setCategory(String category) {
        this.category = category;
        return this;
    }
    public String getCategory() {
        return this.category;
    }

    public SearchViewsRequest setLimit(Integer limit) {
        this.limit = limit;
        return this;
    }
    public Integer getLimit() {
        return this.limit;
    }

    public SearchViewsRequest setMarker(String marker) {
        this.marker = marker;
        return this;
    }
    public String getMarker() {
        return this.marker;
    }

    public SearchViewsRequest setName(String name) {
        this.name = name;
        return this;
    }
    public String getName() {
        return this.name;
    }

    public SearchViewsRequest setOrderBy(String orderBy) {
        this.orderBy = orderBy;
        return this;
    }
    public String getOrderBy() {
        return this.orderBy;
    }

    public SearchViewsRequest setOrderDirection(String orderDirection) {
        this.orderDirection = orderDirection;
        return this;
    }
    public String getOrderDirection() {
        return this.orderDirection;
    }

    public SearchViewsRequest setOwner(String owner) {
        this.owner = owner;
        return this;
    }
    public String getOwner() {
        return this.owner;
    }

    public SearchViewsRequest setReturnTotalCount(Boolean returnTotalCount) {
        this.returnTotalCount = returnTotalCount;
        return this;
    }
    public Boolean getReturnTotalCount() {
        return this.returnTotalCount;
    }

    public SearchViewsRequest setUserId(String userId) {
        this.userId = userId;
        return this;
    }
    public String getUserId() {
        return this.userId;
    }

}
