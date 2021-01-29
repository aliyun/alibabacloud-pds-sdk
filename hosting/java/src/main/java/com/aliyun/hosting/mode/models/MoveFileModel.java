// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.hosting.mode.models;

import com.aliyun.tea.*;

public class MoveFileModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public MoveFileResponse body;

    public static MoveFileModel build(java.util.Map<String, ?> map) throws Exception {
        MoveFileModel self = new MoveFileModel();
        return TeaModel.build(map, self);
    }

    public MoveFileModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public MoveFileModel setBody(MoveFileResponse body) {
        this.body = body;
        return this;
    }
    public MoveFileResponse getBody() {
        return this.body;
    }

}
