// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

public class SetSubdomainBizCnameModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public SetBizCNameResponse body;

    public static SetSubdomainBizCnameModel build(java.util.Map<String, ?> map) throws Exception {
        SetSubdomainBizCnameModel self = new SetSubdomainBizCnameModel();
        return TeaModel.build(map, self);
    }

    public SetSubdomainBizCnameModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public SetSubdomainBizCnameModel setBody(SetBizCNameResponse body) {
        this.body = body;
        return this;
    }
    public SetBizCNameResponse getBody() {
        return this.body;
    }

}
