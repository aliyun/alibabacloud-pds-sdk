// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * simple query response
 */
public class SimpleQueryResponse extends TeaModel {
    @NameInMap("aggregations")
    public java.util.List<Aggregation> aggregations;

    @NameInMap("files")
    public java.util.List<BaseCCPFileResponse> files;

    @NameInMap("next_marker")
    public String nextMarker;

    public static SimpleQueryResponse build(java.util.Map<String, ?> map) throws Exception {
        SimpleQueryResponse self = new SimpleQueryResponse();
        return TeaModel.build(map, self);
    }

    public SimpleQueryResponse setAggregations(java.util.List<Aggregation> aggregations) {
        this.aggregations = aggregations;
        return this;
    }
    public java.util.List<Aggregation> getAggregations() {
        return this.aggregations;
    }

    public SimpleQueryResponse setFiles(java.util.List<BaseCCPFileResponse> files) {
        this.files = files;
        return this;
    }
    public java.util.List<BaseCCPFileResponse> getFiles() {
        return this.files;
    }

    public SimpleQueryResponse setNextMarker(String nextMarker) {
        this.nextMarker = nextMarker;
        return this;
    }
    public String getNextMarker() {
        return this.nextMarker;
    }

}
