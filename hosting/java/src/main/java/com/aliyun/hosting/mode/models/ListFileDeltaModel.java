// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.hosting.mode.models;

import com.aliyun.tea.*;

public class ListFileDeltaModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public ListFileDeltaResponse body;

    public static ListFileDeltaModel build(java.util.Map<String, ?> map) throws Exception {
        ListFileDeltaModel self = new ListFileDeltaModel();
        return TeaModel.build(map, self);
    }

    public ListFileDeltaModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public ListFileDeltaModel setBody(ListFileDeltaResponse body) {
        this.body = body;
        return this;
    }
    public ListFileDeltaResponse getBody() {
        return this.body;
    }

}
