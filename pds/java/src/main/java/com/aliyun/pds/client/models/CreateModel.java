// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class CreateModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public BasePermissionResponse body;

    public static CreateModel build(java.util.Map<String, ?> map) throws Exception {
        CreateModel self = new CreateModel();
        return TeaModel.build(map, self);
    }

    public CreateModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public CreateModel setBody(BasePermissionResponse body) {
        this.body = body;
        return this;
    }
    public BasePermissionResponse getBody() {
        return this.body;
    }

}
