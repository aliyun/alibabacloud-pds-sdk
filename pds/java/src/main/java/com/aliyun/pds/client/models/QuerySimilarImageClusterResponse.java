// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * query similar image cluster response
 */
public class QuerySimilarImageClusterResponse extends TeaModel {
    @NameInMap("next_marker")
    public String nextMarker;

    @NameInMap("similar_image_clusters")
    public java.util.List<SimilarImageCluster> similarImageClusters;

    public static QuerySimilarImageClusterResponse build(java.util.Map<String, ?> map) throws Exception {
        QuerySimilarImageClusterResponse self = new QuerySimilarImageClusterResponse();
        return TeaModel.build(map, self);
    }

    public QuerySimilarImageClusterResponse setNextMarker(String nextMarker) {
        this.nextMarker = nextMarker;
        return this;
    }
    public String getNextMarker() {
        return this.nextMarker;
    }

    public QuerySimilarImageClusterResponse setSimilarImageClusters(java.util.List<SimilarImageCluster> similarImageClusters) {
        this.similarImageClusters = similarImageClusters;
        return this;
    }
    public java.util.List<SimilarImageCluster> getSimilarImageClusters() {
        return this.similarImageClusters;
    }

}
