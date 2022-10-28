// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class DeleteLocationDateClusterModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public DeleteLocationDateClusterResponse body;

    public static DeleteLocationDateClusterModel build(java.util.Map<String, ?> map) throws Exception {
        DeleteLocationDateClusterModel self = new DeleteLocationDateClusterModel();
        return TeaModel.build(map, self);
    }

    public DeleteLocationDateClusterModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public DeleteLocationDateClusterModel setBody(DeleteLocationDateClusterResponse body) {
        this.body = body;
        return this;
    }
    public DeleteLocationDateClusterResponse getBody() {
        return this.body;
    }

}
