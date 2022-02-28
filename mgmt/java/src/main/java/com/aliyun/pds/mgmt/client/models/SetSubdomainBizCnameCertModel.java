// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

public class SetSubdomainBizCnameCertModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public SetBizCNameCertResponse body;

    public static SetSubdomainBizCnameCertModel build(java.util.Map<String, ?> map) throws Exception {
        SetSubdomainBizCnameCertModel self = new SetSubdomainBizCnameCertModel();
        return TeaModel.build(map, self);
    }

    public SetSubdomainBizCnameCertModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public SetSubdomainBizCnameCertModel setBody(SetBizCNameCertResponse body) {
        this.body = body;
        return this;
    }
    public SetBizCNameCertResponse getBody() {
        return this.body;
    }

}
