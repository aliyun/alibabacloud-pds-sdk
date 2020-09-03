// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.hosting.mode.models;

import com.aliyun.tea.*;

public class LoginModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public AccountAccessTokenResponse body;

    public static LoginModel build(java.util.Map<String, ?> map) throws Exception {
        LoginModel self = new LoginModel();
        return TeaModel.build(map, self);
    }

    public LoginModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public LoginModel setBody(AccountAccessTokenResponse body) {
        this.body = body;
        return this;
    }
    public AccountAccessTokenResponse getBody() {
        return this.body;
    }

}
