// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class GetViewFileModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public GetViewFileResponse body;

    public static GetViewFileModel build(java.util.Map<String, ?> map) throws Exception {
        GetViewFileModel self = new GetViewFileModel();
        return TeaModel.build(map, self);
    }

    public GetViewFileModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public GetViewFileModel setBody(GetViewFileResponse body) {
        this.body = body;
        return this;
    }
    public GetViewFileResponse getBody() {
        return this.body;
    }

}
