// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.standard.client.models;

import com.aliyun.tea.*;

public class CreateUserModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public CreateUserResponse body;

    public static CreateUserModel build(java.util.Map<String, ?> map) throws Exception {
        CreateUserModel self = new CreateUserModel();
        return TeaModel.build(map, self);
    }

    public CreateUserModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public CreateUserModel setBody(CreateUserResponse body) {
        this.body = body;
        return this;
    }
    public CreateUserResponse getBody() {
        return this.body;
    }

}
