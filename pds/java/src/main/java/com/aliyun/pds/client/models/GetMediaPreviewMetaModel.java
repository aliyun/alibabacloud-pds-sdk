// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class GetMediaPreviewMetaModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public CCPGetVideoPreviewPlayMetaResponse body;

    public static GetMediaPreviewMetaModel build(java.util.Map<String, ?> map) throws Exception {
        GetMediaPreviewMetaModel self = new GetMediaPreviewMetaModel();
        return TeaModel.build(map, self);
    }

    public GetMediaPreviewMetaModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public GetMediaPreviewMetaModel setBody(CCPGetVideoPreviewPlayMetaResponse body) {
        this.body = body;
        return this;
    }
    public CCPGetVideoPreviewPlayMetaResponse getBody() {
        return this.body;
    }

}
