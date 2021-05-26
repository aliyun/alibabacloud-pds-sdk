// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class GetStoryModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public GetStoryResponse body;

    public static GetStoryModel build(java.util.Map<String, ?> map) throws Exception {
        GetStoryModel self = new GetStoryModel();
        return TeaModel.build(map, self);
    }

    public GetStoryModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public GetStoryModel setBody(GetStoryResponse body) {
        this.body = body;
        return this;
    }
    public GetStoryResponse getBody() {
        return this.body;
    }

}
