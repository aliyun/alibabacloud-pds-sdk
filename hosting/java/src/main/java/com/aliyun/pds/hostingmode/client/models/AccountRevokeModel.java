// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.hostingmode.client.models;

import com.aliyun.tea.*;

public class AccountRevokeModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    public static AccountRevokeModel build(java.util.Map<String, ?> map) throws Exception {
        AccountRevokeModel self = new AccountRevokeModel();
        return TeaModel.build(map, self);
    }

    public AccountRevokeModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

}
