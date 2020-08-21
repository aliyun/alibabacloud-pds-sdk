// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class GetVideoPreviewSpriteUrlModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public GetVideoPreviewSpriteURLResponse body;

    public static GetVideoPreviewSpriteUrlModel build(java.util.Map<String, ?> map) throws Exception {
        GetVideoPreviewSpriteUrlModel self = new GetVideoPreviewSpriteUrlModel();
        return TeaModel.build(map, self);
    }

    public GetVideoPreviewSpriteUrlModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public GetVideoPreviewSpriteUrlModel setBody(GetVideoPreviewSpriteURLResponse body) {
        this.body = body;
        return this;
    }
    public GetVideoPreviewSpriteURLResponse getBody() {
        return this.body;
    }

}
