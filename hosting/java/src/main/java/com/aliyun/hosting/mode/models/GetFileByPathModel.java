// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.hosting.mode.models;

import com.aliyun.tea.*;

public class GetFileByPathModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public GetFileByPathResponse body;

    public static GetFileByPathModel build(java.util.Map<String, ?> map) throws Exception {
        GetFileByPathModel self = new GetFileByPathModel();
        return TeaModel.build(map, self);
    }

    public GetFileByPathModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public GetFileByPathModel setBody(GetFileByPathResponse body) {
        this.body = body;
        return this;
    }
    public GetFileByPathResponse getBody() {
        return this.body;
    }

}
