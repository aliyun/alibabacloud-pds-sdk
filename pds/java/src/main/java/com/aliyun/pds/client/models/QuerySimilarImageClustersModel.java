// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class QuerySimilarImageClustersModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public QuerySimilarImageClusterResponse body;

    public static QuerySimilarImageClustersModel build(java.util.Map<String, ?> map) throws Exception {
        QuerySimilarImageClustersModel self = new QuerySimilarImageClustersModel();
        return TeaModel.build(map, self);
    }

    public QuerySimilarImageClustersModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public QuerySimilarImageClustersModel setBody(QuerySimilarImageClusterResponse body) {
        this.body = body;
        return this;
    }
    public QuerySimilarImageClusterResponse getBody() {
        return this.body;
    }

}
