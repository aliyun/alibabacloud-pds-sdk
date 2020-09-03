// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.hosting.mode.models;

import com.aliyun.tea.*;

public class GetUserAccessTokenModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public AccessTokenResponse body;

    public static GetUserAccessTokenModel build(java.util.Map<String, ?> map) throws Exception {
        GetUserAccessTokenModel self = new GetUserAccessTokenModel();
        return TeaModel.build(map, self);
    }

    public GetUserAccessTokenModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public GetUserAccessTokenModel setBody(AccessTokenResponse body) {
        this.body = body;
        return this;
    }
    public AccessTokenResponse getBody() {
        return this.body;
    }

}
