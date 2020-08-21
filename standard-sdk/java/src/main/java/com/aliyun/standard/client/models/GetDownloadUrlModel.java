// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.standard.client.models;

import com.aliyun.tea.*;

public class GetDownloadUrlModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public GetDownloadUrlResponse body;

    public static GetDownloadUrlModel build(java.util.Map<String, ?> map) throws Exception {
        GetDownloadUrlModel self = new GetDownloadUrlModel();
        return TeaModel.build(map, self);
    }

    public GetDownloadUrlModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public GetDownloadUrlModel setBody(GetDownloadUrlResponse body) {
        this.body = body;
        return this;
    }
    public GetDownloadUrlResponse getBody() {
        return this.body;
    }

}
