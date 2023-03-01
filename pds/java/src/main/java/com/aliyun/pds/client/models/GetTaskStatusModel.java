// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class GetTaskStatusModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public GetTaskStatusResponse body;

    public static GetTaskStatusModel build(java.util.Map<String, ?> map) throws Exception {
        GetTaskStatusModel self = new GetTaskStatusModel();
        return TeaModel.build(map, self);
    }

    public GetTaskStatusModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public GetTaskStatusModel setBody(GetTaskStatusResponse body) {
        this.body = body;
        return this;
    }
    public GetTaskStatusResponse getBody() {
        return this.body;
    }

}
