// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.standard.client.models;

import com.aliyun.tea.*;

public class GetShareTokenModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public GetShareLinkTokenResponse body;

    public static GetShareTokenModel build(java.util.Map<String, ?> map) throws Exception {
        GetShareTokenModel self = new GetShareTokenModel();
        return TeaModel.build(map, self);
    }

    public GetShareTokenModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public GetShareTokenModel setBody(GetShareLinkTokenResponse body) {
        this.body = body;
        return this;
    }
    public GetShareLinkTokenResponse getBody() {
        return this.body;
    }

}
