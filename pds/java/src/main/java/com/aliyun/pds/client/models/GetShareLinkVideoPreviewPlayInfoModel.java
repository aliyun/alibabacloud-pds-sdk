// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class GetShareLinkVideoPreviewPlayInfoModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public CCPGetShareLinkVideoPreviewPlayInfoResponse body;

    public static GetShareLinkVideoPreviewPlayInfoModel build(java.util.Map<String, ?> map) throws Exception {
        GetShareLinkVideoPreviewPlayInfoModel self = new GetShareLinkVideoPreviewPlayInfoModel();
        return TeaModel.build(map, self);
    }

    public GetShareLinkVideoPreviewPlayInfoModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public GetShareLinkVideoPreviewPlayInfoModel setBody(CCPGetShareLinkVideoPreviewPlayInfoResponse body) {
        this.body = body;
        return this;
    }
    public CCPGetShareLinkVideoPreviewPlayInfoResponse getBody() {
        return this.body;
    }

}
