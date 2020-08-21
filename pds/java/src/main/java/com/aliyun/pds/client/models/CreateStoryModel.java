// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class CreateStoryModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public CreateStoryResponse body;

    public static CreateStoryModel build(java.util.Map<String, ?> map) throws Exception {
        CreateStoryModel self = new CreateStoryModel();
        return TeaModel.build(map, self);
    }

    public CreateStoryModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public CreateStoryModel setBody(CreateStoryResponse body) {
        this.body = body;
        return this;
    }
    public CreateStoryResponse getBody() {
        return this.body;
    }

}
