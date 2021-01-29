// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.hosting.mode.models;

import com.aliyun.tea.*;

public class DeleteFileModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public DeleteFileResponse body;

    public static DeleteFileModel build(java.util.Map<String, ?> map) throws Exception {
        DeleteFileModel self = new DeleteFileModel();
        return TeaModel.build(map, self);
    }

    public DeleteFileModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public DeleteFileModel setBody(DeleteFileResponse body) {
        this.body = body;
        return this;
    }
    public DeleteFileResponse getBody() {
        return this.body;
    }

}
