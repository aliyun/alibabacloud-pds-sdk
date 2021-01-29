// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.hosting.mode.models;

import com.aliyun.tea.*;

public class ScanFileMetaModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public ScanFileMetaResponse body;

    public static ScanFileMetaModel build(java.util.Map<String, ?> map) throws Exception {
        ScanFileMetaModel self = new ScanFileMetaModel();
        return TeaModel.build(map, self);
    }

    public ScanFileMetaModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public ScanFileMetaModel setBody(ScanFileMetaResponse body) {
        this.body = body;
        return this;
    }
    public ScanFileMetaResponse getBody() {
        return this.body;
    }

}
