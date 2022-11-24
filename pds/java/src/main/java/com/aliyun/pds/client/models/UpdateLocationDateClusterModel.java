// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class UpdateLocationDateClusterModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public UpdateLocationDateClusterResponse body;

    public static UpdateLocationDateClusterModel build(java.util.Map<String, ?> map) throws Exception {
        UpdateLocationDateClusterModel self = new UpdateLocationDateClusterModel();
        return TeaModel.build(map, self);
    }

    public UpdateLocationDateClusterModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public UpdateLocationDateClusterModel setBody(UpdateLocationDateClusterResponse body) {
        this.body = body;
        return this;
    }
    public UpdateLocationDateClusterResponse getBody() {
        return this.body;
    }

}
