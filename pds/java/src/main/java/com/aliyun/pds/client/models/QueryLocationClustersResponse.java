// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * query locationCluster response
 */
public class QueryLocationClustersResponse extends TeaModel {
    @NameInMap("location_date_clusters")
    public java.util.List<LocationDateCluster> locationDateClusters;

    @NameInMap("next_marker")
    public String nextMarker;

    public static QueryLocationClustersResponse build(java.util.Map<String, ?> map) throws Exception {
        QueryLocationClustersResponse self = new QueryLocationClustersResponse();
        return TeaModel.build(map, self);
    }

    public QueryLocationClustersResponse setLocationDateClusters(java.util.List<LocationDateCluster> locationDateClusters) {
        this.locationDateClusters = locationDateClusters;
        return this;
    }
    public java.util.List<LocationDateCluster> getLocationDateClusters() {
        return this.locationDateClusters;
    }

    public QueryLocationClustersResponse setNextMarker(String nextMarker) {
        this.nextMarker = nextMarker;
        return this;
    }
    public String getNextMarker() {
        return this.nextMarker;
    }

}
