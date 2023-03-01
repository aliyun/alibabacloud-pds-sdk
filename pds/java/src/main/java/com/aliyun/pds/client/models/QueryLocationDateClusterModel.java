// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class QueryLocationDateClusterModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public QueryLocationClustersResponse body;

    public static QueryLocationDateClusterModel build(java.util.Map<String, ?> map) throws Exception {
        QueryLocationDateClusterModel self = new QueryLocationDateClusterModel();
        return TeaModel.build(map, self);
    }

    public QueryLocationDateClusterModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public QueryLocationDateClusterModel setBody(QueryLocationClustersResponse body) {
        this.body = body;
        return this;
    }
    public QueryLocationClustersResponse getBody() {
        return this.body;
    }

}
