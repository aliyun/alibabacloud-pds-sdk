// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.hostingmode.client.models;

import com.aliyun.tea.*;

public class VerifyCodeModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public VerifyCodeResponse body;

    public static VerifyCodeModel build(java.util.Map<String, ?> map) throws Exception {
        VerifyCodeModel self = new VerifyCodeModel();
        return TeaModel.build(map, self);
    }

    public VerifyCodeModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public VerifyCodeModel setBody(VerifyCodeResponse body) {
        this.body = body;
        return this;
    }
    public VerifyCodeResponse getBody() {
        return this.body;
    }

}
