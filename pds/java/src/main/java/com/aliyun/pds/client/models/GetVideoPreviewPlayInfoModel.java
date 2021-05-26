// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class GetVideoPreviewPlayInfoModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public CCPGetVideoPreviewPlayInfoResponse body;

    public static GetVideoPreviewPlayInfoModel build(java.util.Map<String, ?> map) throws Exception {
        GetVideoPreviewPlayInfoModel self = new GetVideoPreviewPlayInfoModel();
        return TeaModel.build(map, self);
    }

    public GetVideoPreviewPlayInfoModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public GetVideoPreviewPlayInfoModel setBody(CCPGetVideoPreviewPlayInfoResponse body) {
        this.body = body;
        return this;
    }
    public CCPGetVideoPreviewPlayInfoResponse getBody() {
        return this.body;
    }

}
