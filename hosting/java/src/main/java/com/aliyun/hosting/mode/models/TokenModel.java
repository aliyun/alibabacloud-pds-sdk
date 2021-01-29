// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.hosting.mode.models;

import com.aliyun.tea.*;

public class TokenModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public RefreshOfficeEditTokenResponse body;

    public static TokenModel build(java.util.Map<String, ?> map) throws Exception {
        TokenModel self = new TokenModel();
        return TeaModel.build(map, self);
    }

    public TokenModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public TokenModel setBody(RefreshOfficeEditTokenResponse body) {
        this.body = body;
        return this;
    }
    public RefreshOfficeEditTokenResponse getBody() {
        return this.body;
    }

}
