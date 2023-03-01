// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 查询审计日志request
 */
public class SearchAuditLogRequest extends TeaModel {
    /**
     * <p>limit</p>
     */
    @NameInMap("limit")
    @Validation(maximum = 200, minimum = 1)
    public Integer limit;

    /**
     * <p>Marker</p>
     */
    @NameInMap("marker")
    public String marker;

    /**
     * <p>order_by</p>
     */
    @NameInMap("order_by")
    public String orderBy;

    /**
     * <p>query</p>
     */
    @NameInMap("query")
    @Validation(maxLength = 4096)
    public String query;

    public static SearchAuditLogRequest build(java.util.Map<String, ?> map) throws Exception {
        SearchAuditLogRequest self = new SearchAuditLogRequest();
        return TeaModel.build(map, self);
    }

    public SearchAuditLogRequest setLimit(Integer limit) {
        this.limit = limit;
        return this;
    }
    public Integer getLimit() {
        return this.limit;
    }

    public SearchAuditLogRequest setMarker(String marker) {
        this.marker = marker;
        return this;
    }
    public String getMarker() {
        return this.marker;
    }

    public SearchAuditLogRequest setOrderBy(String orderBy) {
        this.orderBy = orderBy;
        return this;
    }
    public String getOrderBy() {
        return this.orderBy;
    }

    public SearchAuditLogRequest setQuery(String query) {
        this.query = query;
        return this;
    }
    public String getQuery() {
        return this.query;
    }

}
