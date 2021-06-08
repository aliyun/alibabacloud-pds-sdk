// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class TrashFileModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public TrashFileResponse body;

    public static TrashFileModel build(java.util.Map<String, ?> map) throws Exception {
        TrashFileModel self = new TrashFileModel();
        return TeaModel.build(map, self);
    }

    public TrashFileModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public TrashFileModel setBody(TrashFileResponse body) {
        this.body = body;
        return this;
    }
    public TrashFileResponse getBody() {
        return this.body;
    }

}
