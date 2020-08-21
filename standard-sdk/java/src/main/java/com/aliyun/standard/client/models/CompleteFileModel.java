// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.standard.client.models;

import com.aliyun.tea.*;

public class CompleteFileModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public CompleteFileResponse body;

    public static CompleteFileModel build(java.util.Map<String, ?> map) throws Exception {
        CompleteFileModel self = new CompleteFileModel();
        return TeaModel.build(map, self);
    }

    public CompleteFileModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public CompleteFileModel setBody(CompleteFileResponse body) {
        this.body = body;
        return this;
    }
    public CompleteFileResponse getBody() {
        return this.body;
    }

}
