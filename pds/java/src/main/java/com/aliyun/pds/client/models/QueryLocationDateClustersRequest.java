// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * query locationCluster request
 */
public class QueryLocationDateClustersRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    @NameInMap("address")
    public Address address;

    @NameInMap("cluster_id")
    public String clusterId;

    @NameInMap("create_time_range")
    public QueryRequestTimeRange createTimeRange;

    @NameInMap("custom_labels")
    public String customLabels;

    /**
     * <p>drive_id</p>
     */
    @NameInMap("drive_id")
    @Validation(required = true, pattern = "[0-9]+")
    public String driveId;

    @NameInMap("end_time_range")
    public QueryRequestTimeRange endTimeRange;

    @NameInMap("levels")
    public java.util.List<String> levels;

    @NameInMap("limit")
    public Integer limit;

    @NameInMap("marker")
    public String marker;

    @NameInMap("order")
    public String order;

    @NameInMap("sort")
    public String sort;

    @NameInMap("start_time_range")
    public QueryRequestTimeRange startTimeRange;

    @NameInMap("title")
    public String title;

    @NameInMap("update_time_range")
    public QueryRequestTimeRange updateTimeRange;

    public static QueryLocationDateClustersRequest build(java.util.Map<String, ?> map) throws Exception {
        QueryLocationDateClustersRequest self = new QueryLocationDateClustersRequest();
        return TeaModel.build(map, self);
    }

    public QueryLocationDateClustersRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public QueryLocationDateClustersRequest setAddress(Address address) {
        this.address = address;
        return this;
    }
    public Address getAddress() {
        return this.address;
    }

    public QueryLocationDateClustersRequest setClusterId(String clusterId) {
        this.clusterId = clusterId;
        return this;
    }
    public String getClusterId() {
        return this.clusterId;
    }

    public QueryLocationDateClustersRequest setCreateTimeRange(QueryRequestTimeRange createTimeRange) {
        this.createTimeRange = createTimeRange;
        return this;
    }
    public QueryRequestTimeRange getCreateTimeRange() {
        return this.createTimeRange;
    }

    public QueryLocationDateClustersRequest setCustomLabels(String customLabels) {
        this.customLabels = customLabels;
        return this;
    }
    public String getCustomLabels() {
        return this.customLabels;
    }

    public QueryLocationDateClustersRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public QueryLocationDateClustersRequest setEndTimeRange(QueryRequestTimeRange endTimeRange) {
        this.endTimeRange = endTimeRange;
        return this;
    }
    public QueryRequestTimeRange getEndTimeRange() {
        return this.endTimeRange;
    }

    public QueryLocationDateClustersRequest setLevels(java.util.List<String> levels) {
        this.levels = levels;
        return this;
    }
    public java.util.List<String> getLevels() {
        return this.levels;
    }

    public QueryLocationDateClustersRequest setLimit(Integer limit) {
        this.limit = limit;
        return this;
    }
    public Integer getLimit() {
        return this.limit;
    }

    public QueryLocationDateClustersRequest setMarker(String marker) {
        this.marker = marker;
        return this;
    }
    public String getMarker() {
        return this.marker;
    }

    public QueryLocationDateClustersRequest setOrder(String order) {
        this.order = order;
        return this;
    }
    public String getOrder() {
        return this.order;
    }

    public QueryLocationDateClustersRequest setSort(String sort) {
        this.sort = sort;
        return this;
    }
    public String getSort() {
        return this.sort;
    }

    public QueryLocationDateClustersRequest setStartTimeRange(QueryRequestTimeRange startTimeRange) {
        this.startTimeRange = startTimeRange;
        return this;
    }
    public QueryRequestTimeRange getStartTimeRange() {
        return this.startTimeRange;
    }

    public QueryLocationDateClustersRequest setTitle(String title) {
        this.title = title;
        return this;
    }
    public String getTitle() {
        return this.title;
    }

    public QueryLocationDateClustersRequest setUpdateTimeRange(QueryRequestTimeRange updateTimeRange) {
        this.updateTimeRange = updateTimeRange;
        return this;
    }
    public QueryRequestTimeRange getUpdateTimeRange() {
        return this.updateTimeRange;
    }

}
