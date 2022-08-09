// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class GetFileRevisionModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public GetRevisionResponse body;

    public static GetFileRevisionModel build(java.util.Map<String, ?> map) throws Exception {
        GetFileRevisionModel self = new GetFileRevisionModel();
        return TeaModel.build(map, self);
    }

    public GetFileRevisionModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public GetFileRevisionModel setBody(GetRevisionResponse body) {
        this.body = body;
        return this;
    }
    public GetRevisionResponse getBody() {
        return this.body;
    }

}
