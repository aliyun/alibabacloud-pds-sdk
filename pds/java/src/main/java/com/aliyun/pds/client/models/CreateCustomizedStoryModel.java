// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class CreateCustomizedStoryModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public CreateCustomizedStoryResponse body;

    public static CreateCustomizedStoryModel build(java.util.Map<String, ?> map) throws Exception {
        CreateCustomizedStoryModel self = new CreateCustomizedStoryModel();
        return TeaModel.build(map, self);
    }

    public CreateCustomizedStoryModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public CreateCustomizedStoryModel setBody(CreateCustomizedStoryResponse body) {
        this.body = body;
        return this;
    }
    public CreateCustomizedStoryResponse getBody() {
        return this.body;
    }

}
