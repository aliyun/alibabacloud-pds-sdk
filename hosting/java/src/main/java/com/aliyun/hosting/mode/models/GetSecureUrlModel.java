// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.hosting.mode.models;

import com.aliyun.tea.*;

public class GetSecureUrlModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public HostingGetSecureUrlResponse body;

    public static GetSecureUrlModel build(java.util.Map<String, ?> map) throws Exception {
        GetSecureUrlModel self = new GetSecureUrlModel();
        return TeaModel.build(map, self);
    }

    public GetSecureUrlModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public GetSecureUrlModel setBody(HostingGetSecureUrlResponse body) {
        this.body = body;
        return this;
    }
    public HostingGetSecureUrlResponse getBody() {
        return this.body;
    }

}
