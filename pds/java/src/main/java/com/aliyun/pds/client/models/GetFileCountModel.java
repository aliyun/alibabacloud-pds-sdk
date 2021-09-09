// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class GetFileCountModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public GetFileCountResponse body;

    public static GetFileCountModel build(java.util.Map<String, ?> map) throws Exception {
        GetFileCountModel self = new GetFileCountModel();
        return TeaModel.build(map, self);
    }

    public GetFileCountModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public GetFileCountModel setBody(GetFileCountResponse body) {
        this.body = body;
        return this;
    }
    public GetFileCountResponse getBody() {
        return this.body;
    }

}
