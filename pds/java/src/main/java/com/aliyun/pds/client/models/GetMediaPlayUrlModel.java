// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class GetMediaPlayUrlModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public GetMediaPlayURLResponse body;

    public static GetMediaPlayUrlModel build(java.util.Map<String, ?> map) throws Exception {
        GetMediaPlayUrlModel self = new GetMediaPlayUrlModel();
        return TeaModel.build(map, self);
    }

    public GetMediaPlayUrlModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public GetMediaPlayUrlModel setBody(GetMediaPlayURLResponse body) {
        this.body = body;
        return this;
    }
    public GetMediaPlayURLResponse getBody() {
        return this.body;
    }

}
