// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class GetShareLinkModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public BaseShareLinkResponse body;

    public static GetShareLinkModel build(java.util.Map<String, ?> map) throws Exception {
        GetShareLinkModel self = new GetShareLinkModel();
        return TeaModel.build(map, self);
    }

    public GetShareLinkModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public GetShareLinkModel setBody(BaseShareLinkResponse body) {
        this.body = body;
        return this;
    }
    public BaseShareLinkResponse getBody() {
        return this.body;
    }

}
