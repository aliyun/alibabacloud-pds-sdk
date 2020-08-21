// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.standard.client.models;

import com.aliyun.tea.*;

public class GetVideoPreviewUrlModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public GetVideoPreviewURLResponse body;

    public static GetVideoPreviewUrlModel build(java.util.Map<String, ?> map) throws Exception {
        GetVideoPreviewUrlModel self = new GetVideoPreviewUrlModel();
        return TeaModel.build(map, self);
    }

    public GetVideoPreviewUrlModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public GetVideoPreviewUrlModel setBody(GetVideoPreviewURLResponse body) {
        this.body = body;
        return this;
    }
    public GetVideoPreviewURLResponse getBody() {
        return this.body;
    }

}
