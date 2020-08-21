// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.standard.client.models;

import com.aliyun.tea.*;

public class GetAsyncTaskInfoModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public GetAsyncTaskResponse body;

    public static GetAsyncTaskInfoModel build(java.util.Map<String, ?> map) throws Exception {
        GetAsyncTaskInfoModel self = new GetAsyncTaskInfoModel();
        return TeaModel.build(map, self);
    }

    public GetAsyncTaskInfoModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public GetAsyncTaskInfoModel setBody(GetAsyncTaskResponse body) {
        this.body = body;
        return this;
    }
    public GetAsyncTaskResponse getBody() {
        return this.body;
    }

}
