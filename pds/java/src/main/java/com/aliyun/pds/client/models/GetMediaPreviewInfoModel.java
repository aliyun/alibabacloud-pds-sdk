// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class GetMediaPreviewInfoModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public CCPGetVideoPreviewPlayInfoResponse body;

    public static GetMediaPreviewInfoModel build(java.util.Map<String, ?> map) throws Exception {
        GetMediaPreviewInfoModel self = new GetMediaPreviewInfoModel();
        return TeaModel.build(map, self);
    }

    public GetMediaPreviewInfoModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public GetMediaPreviewInfoModel setBody(CCPGetVideoPreviewPlayInfoResponse body) {
        this.body = body;
        return this;
    }
    public CCPGetVideoPreviewPlayInfoResponse getBody() {
        return this.body;
    }

}
