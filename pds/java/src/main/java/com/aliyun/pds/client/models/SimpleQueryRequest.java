// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * simple query request
 */
public class SimpleQueryRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    @NameInMap("aggregations")
    public java.util.List<Aggregation> aggregations;

    /**
     * <p>drive_id</p>
     */
    @NameInMap("drive_id")
    @Validation(required = true, pattern = "[0-9]+")
    public String driveId;

    @NameInMap("limit")
    public Integer limit;

    @NameInMap("marker")
    public String marker;

    @NameInMap("order")
    public String order;

    @NameInMap("query")
    public SimpleQuery query;

    @NameInMap("sort")
    public String sort;

    public static SimpleQueryRequest build(java.util.Map<String, ?> map) throws Exception {
        SimpleQueryRequest self = new SimpleQueryRequest();
        return TeaModel.build(map, self);
    }

    public SimpleQueryRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public SimpleQueryRequest setAggregations(java.util.List<Aggregation> aggregations) {
        this.aggregations = aggregations;
        return this;
    }
    public java.util.List<Aggregation> getAggregations() {
        return this.aggregations;
    }

    public SimpleQueryRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public SimpleQueryRequest setLimit(Integer limit) {
        this.limit = limit;
        return this;
    }
    public Integer getLimit() {
        return this.limit;
    }

    public SimpleQueryRequest setMarker(String marker) {
        this.marker = marker;
        return this;
    }
    public String getMarker() {
        return this.marker;
    }

    public SimpleQueryRequest setOrder(String order) {
        this.order = order;
        return this;
    }
    public String getOrder() {
        return this.order;
    }

    public SimpleQueryRequest setQuery(SimpleQuery query) {
        this.query = query;
        return this;
    }
    public SimpleQuery getQuery() {
        return this.query;
    }

    public SimpleQueryRequest setSort(String sort) {
        this.sort = sort;
        return this;
    }
    public String getSort() {
        return this.sort;
    }

}
