// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class ChangePasswordModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public AccountAccessTokenResponse body;

    public static ChangePasswordModel build(java.util.Map<String, ?> map) throws Exception {
        ChangePasswordModel self = new ChangePasswordModel();
        return TeaModel.build(map, self);
    }

    public ChangePasswordModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public ChangePasswordModel setBody(AccountAccessTokenResponse body) {
        this.body = body;
        return this;
    }
    public AccountAccessTokenResponse getBody() {
        return this.body;
    }

}
