// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.hosting.mode.models;

import com.aliyun.tea.*;

public class AccountTokenModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public AccountAccessTokenResponse body;

    public static AccountTokenModel build(java.util.Map<String, ?> map) throws Exception {
        AccountTokenModel self = new AccountTokenModel();
        return TeaModel.build(map, self);
    }

    public AccountTokenModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public AccountTokenModel setBody(AccountAccessTokenResponse body) {
        this.body = body;
        return this;
    }
    public AccountAccessTokenResponse getBody() {
        return this.body;
    }

}
