// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class DeleteFileRevisionModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public DeleteRevisionResponse body;

    public static DeleteFileRevisionModel build(java.util.Map<String, ?> map) throws Exception {
        DeleteFileRevisionModel self = new DeleteFileRevisionModel();
        return TeaModel.build(map, self);
    }

    public DeleteFileRevisionModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public DeleteFileRevisionModel setBody(DeleteRevisionResponse body) {
        this.body = body;
        return this;
    }
    public DeleteRevisionResponse getBody() {
        return this.body;
    }

}
