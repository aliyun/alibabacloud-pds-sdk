// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.hosting.mode.models;

import com.aliyun.tea.*;

public class GetLastCursorModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public GetLastCursorResponse body;

    public static GetLastCursorModel build(java.util.Map<String, ?> map) throws Exception {
        GetLastCursorModel self = new GetLastCursorModel();
        return TeaModel.build(map, self);
    }

    public GetLastCursorModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public GetLastCursorModel setBody(GetLastCursorResponse body) {
        this.body = body;
        return this;
    }
    public GetLastCursorResponse getBody() {
        return this.body;
    }

}
