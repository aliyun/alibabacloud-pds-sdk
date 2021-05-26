// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class CreateFileWithProofModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public CreateFileResponse body;

    public static CreateFileWithProofModel build(java.util.Map<String, ?> map) throws Exception {
        CreateFileWithProofModel self = new CreateFileWithProofModel();
        return TeaModel.build(map, self);
    }

    public CreateFileWithProofModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public CreateFileWithProofModel setBody(CreateFileResponse body) {
        this.body = body;
        return this;
    }
    public CreateFileResponse getBody() {
        return this.body;
    }

}
