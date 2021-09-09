// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class CreateViewModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public CreateViewResponse body;

    public static CreateViewModel build(java.util.Map<String, ?> map) throws Exception {
        CreateViewModel self = new CreateViewModel();
        return TeaModel.build(map, self);
    }

    public CreateViewModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public CreateViewModel setBody(CreateViewResponse body) {
        this.body = body;
        return this;
    }
    public CreateViewResponse getBody() {
        return this.body;
    }

}
