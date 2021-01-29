// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.mgmt.mode.models;

import com.aliyun.tea.*;

public class SetPublicKeyModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    public static SetPublicKeyModel build(java.util.Map<String, ?> map) throws Exception {
        SetPublicKeyModel self = new SetPublicKeyModel();
        return TeaModel.build(map, self);
    }

    public SetPublicKeyModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

}
