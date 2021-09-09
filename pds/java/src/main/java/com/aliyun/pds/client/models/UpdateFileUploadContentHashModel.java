// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class UpdateFileUploadContentHashModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public UCUpdateUploadContentHashResponse body;

    public static UpdateFileUploadContentHashModel build(java.util.Map<String, ?> map) throws Exception {
        UpdateFileUploadContentHashModel self = new UpdateFileUploadContentHashModel();
        return TeaModel.build(map, self);
    }

    public UpdateFileUploadContentHashModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public UpdateFileUploadContentHashModel setBody(UCUpdateUploadContentHashResponse body) {
        this.body = body;
        return this;
    }
    public UCUpdateUploadContentHashResponse getBody() {
        return this.body;
    }

}
