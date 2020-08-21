// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class GetStoryTaskModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public GetStoryTaskResponse body;

    public static GetStoryTaskModel build(java.util.Map<String, ?> map) throws Exception {
        GetStoryTaskModel self = new GetStoryTaskModel();
        return TeaModel.build(map, self);
    }

    public GetStoryTaskModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public GetStoryTaskModel setBody(GetStoryTaskResponse body) {
        this.body = body;
        return this;
    }
    public GetStoryTaskResponse getBody() {
        return this.body;
    }

}
