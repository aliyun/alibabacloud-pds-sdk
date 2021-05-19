// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

public class UpdateNameModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public GetDomainResponse body;

    public static UpdateNameModel build(java.util.Map<String, ?> map) throws Exception {
        UpdateNameModel self = new UpdateNameModel();
        return TeaModel.build(map, self);
    }

    public UpdateNameModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public UpdateNameModel setBody(GetDomainResponse body) {
        this.body = body;
        return this;
    }
    public GetDomainResponse getBody() {
        return this.body;
    }

}
