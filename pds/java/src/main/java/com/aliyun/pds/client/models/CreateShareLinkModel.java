// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class CreateShareLinkModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public CreateShareLinkResponse body;

    public static CreateShareLinkModel build(java.util.Map<String, ?> map) throws Exception {
        CreateShareLinkModel self = new CreateShareLinkModel();
        return TeaModel.build(map, self);
    }

    public CreateShareLinkModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public CreateShareLinkModel setBody(CreateShareLinkResponse body) {
        this.body = body;
        return this;
    }
    public CreateShareLinkResponse getBody() {
        return this.body;
    }

}
