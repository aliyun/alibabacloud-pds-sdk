// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.mgmt.mode.models;

import com.aliyun.tea.*;

public class SetBizCnameCertModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public SetBizCNameCertResponse body;

    public static SetBizCnameCertModel build(java.util.Map<String, ?> map) throws Exception {
        SetBizCnameCertModel self = new SetBizCnameCertModel();
        return TeaModel.build(map, self);
    }

    public SetBizCnameCertModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public SetBizCnameCertModel setBody(SetBizCNameCertResponse body) {
        this.body = body;
        return this;
    }
    public SetBizCNameCertResponse getBody() {
        return this.body;
    }

}
