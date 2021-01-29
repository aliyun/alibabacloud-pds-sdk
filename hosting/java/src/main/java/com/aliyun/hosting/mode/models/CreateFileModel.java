// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.hosting.mode.models;

import com.aliyun.tea.*;

public class CreateFileModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public CreateFileResponse body;

    public static CreateFileModel build(java.util.Map<String, ?> map) throws Exception {
        CreateFileModel self = new CreateFileModel();
        return TeaModel.build(map, self);
    }

    public CreateFileModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public CreateFileModel setBody(CreateFileResponse body) {
        this.body = body;
        return this;
    }
    public CreateFileResponse getBody() {
        return this.body;
    }

}
