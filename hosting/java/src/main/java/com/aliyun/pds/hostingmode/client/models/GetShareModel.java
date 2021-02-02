// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.hostingmode.client.models;

import com.aliyun.tea.*;

public class GetShareModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public GetShareResponse body;

    public static GetShareModel build(java.util.Map<String, ?> map) throws Exception {
        GetShareModel self = new GetShareModel();
        return TeaModel.build(map, self);
    }

    public GetShareModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public GetShareModel setBody(GetShareResponse body) {
        this.body = body;
        return this;
    }
    public GetShareResponse getBody() {
        return this.body;
    }

}
