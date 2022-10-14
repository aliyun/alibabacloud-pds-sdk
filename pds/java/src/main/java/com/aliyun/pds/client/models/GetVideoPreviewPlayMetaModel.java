// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class GetVideoPreviewPlayMetaModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public CCPGetVideoPreviewPlayMetaResponse body;

    public static GetVideoPreviewPlayMetaModel build(java.util.Map<String, ?> map) throws Exception {
        GetVideoPreviewPlayMetaModel self = new GetVideoPreviewPlayMetaModel();
        return TeaModel.build(map, self);
    }

    public GetVideoPreviewPlayMetaModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public GetVideoPreviewPlayMetaModel setBody(CCPGetVideoPreviewPlayMetaResponse body) {
        this.body = body;
        return this;
    }
    public CCPGetVideoPreviewPlayMetaResponse getBody() {
        return this.body;
    }

}
