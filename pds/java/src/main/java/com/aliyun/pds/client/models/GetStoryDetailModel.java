// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class GetStoryDetailModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public GetStoryDetailResponse body;

    public static GetStoryDetailModel build(java.util.Map<String, ?> map) throws Exception {
        GetStoryDetailModel self = new GetStoryDetailModel();
        return TeaModel.build(map, self);
    }

    public GetStoryDetailModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public GetStoryDetailModel setBody(GetStoryDetailResponse body) {
        this.body = body;
        return this;
    }
    public GetStoryDetailResponse getBody() {
        return this.body;
    }

}
