// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.mgmt.mode.models;

import com.aliyun.tea.*;

public class SetDataCnameModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public SetDataCNameResponse body;

    public static SetDataCnameModel build(java.util.Map<String, ?> map) throws Exception {
        SetDataCnameModel self = new SetDataCnameModel();
        return TeaModel.build(map, self);
    }

    public SetDataCnameModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public SetDataCnameModel setBody(SetDataCNameResponse body) {
        this.body = body;
        return this;
    }
    public SetDataCNameResponse getBody() {
        return this.body;
    }

}
