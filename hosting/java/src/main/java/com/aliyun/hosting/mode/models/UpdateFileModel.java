// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.hosting.mode.models;

import com.aliyun.tea.*;

public class UpdateFileModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public UpdateFileMetaResponse body;

    public static UpdateFileModel build(java.util.Map<String, ?> map) throws Exception {
        UpdateFileModel self = new UpdateFileModel();
        return TeaModel.build(map, self);
    }

    public UpdateFileModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public UpdateFileModel setBody(UpdateFileMetaResponse body) {
        this.body = body;
        return this;
    }
    public UpdateFileMetaResponse getBody() {
        return this.body;
    }

}
