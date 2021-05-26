// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class GetUserAccessTokenModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public GetUserAccessTokenResponse body;

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

    public GetUserAccessTokenModel setBody(GetUserAccessTokenResponse body) {
        this.body = body;
        return this;
    }
    public GetUserAccessTokenResponse getBody() {
        return this.body;
    }

}
