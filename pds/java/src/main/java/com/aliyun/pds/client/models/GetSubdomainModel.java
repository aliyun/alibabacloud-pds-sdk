// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class GetSubdomainModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public GetSubdomainResponse body;

    public static GetSubdomainModel build(java.util.Map<String, ?> map) throws Exception {
        GetSubdomainModel self = new GetSubdomainModel();
        return TeaModel.build(map, self);
    }

    public GetSubdomainModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public GetSubdomainModel setBody(GetSubdomainResponse body) {
        this.body = body;
        return this;
    }
    public GetSubdomainResponse getBody() {
        return this.body;
    }

}
