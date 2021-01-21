// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.mgmt.mode.models;

import com.aliyun.tea.*;

public class SetBizCnameModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public SetBizCNameResponse body;

    public static SetBizCnameModel build(java.util.Map<String, ?> map) throws Exception {
        SetBizCnameModel self = new SetBizCnameModel();
        return TeaModel.build(map, self);
    }

    public SetBizCnameModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public SetBizCnameModel setBody(SetBizCNameResponse body) {
        this.body = body;
        return this;
    }
    public SetBizCNameResponse getBody() {
        return this.body;
    }

}
