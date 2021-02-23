// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class CreateSubdomainModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public CreateSubdomainResponse body;

    public static CreateSubdomainModel build(java.util.Map<String, ?> map) throws Exception {
        CreateSubdomainModel self = new CreateSubdomainModel();
        return TeaModel.build(map, self);
    }

    public CreateSubdomainModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public CreateSubdomainModel setBody(CreateSubdomainResponse body) {
        this.body = body;
        return this;
    }
    public CreateSubdomainResponse getBody() {
        return this.body;
    }

}
