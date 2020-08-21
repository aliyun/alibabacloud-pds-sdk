// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.standard.client.models;

import com.aliyun.tea.*;

public class BatchOperationModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public BatchResponse body;

    public static BatchOperationModel build(java.util.Map<String, ?> map) throws Exception {
        BatchOperationModel self = new BatchOperationModel();
        return TeaModel.build(map, self);
    }

    public BatchOperationModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public BatchOperationModel setBody(BatchResponse body) {
        this.body = body;
        return this;
    }
    public BatchResponse getBody() {
        return this.body;
    }

}
