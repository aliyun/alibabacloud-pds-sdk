// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.hostingmode.client.models;

import com.aliyun.tea.*;

public class GetAccessTokenByLinkInfoModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public AccountAccessTokenResponse body;

    public static GetAccessTokenByLinkInfoModel build(java.util.Map<String, ?> map) throws Exception {
        GetAccessTokenByLinkInfoModel self = new GetAccessTokenByLinkInfoModel();
        return TeaModel.build(map, self);
    }

    public GetAccessTokenByLinkInfoModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public GetAccessTokenByLinkInfoModel setBody(AccountAccessTokenResponse body) {
        this.body = body;
        return this;
    }
    public AccountAccessTokenResponse getBody() {
        return this.body;
    }

}
