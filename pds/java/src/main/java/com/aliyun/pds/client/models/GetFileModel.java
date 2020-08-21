// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class GetFileModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public GetFileResponse body;

    public static GetFileModel build(java.util.Map<String, ?> map) throws Exception {
        GetFileModel self = new GetFileModel();
        return TeaModel.build(map, self);
    }

    public GetFileModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public GetFileModel setBody(GetFileResponse body) {
        this.body = body;
        return this;
    }
    public GetFileResponse getBody() {
        return this.body;
    }

}
