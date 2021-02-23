// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class GetGroupModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public GetGroupResponse body;

    public static GetGroupModel build(java.util.Map<String, ?> map) throws Exception {
        GetGroupModel self = new GetGroupModel();
        return TeaModel.build(map, self);
    }

    public GetGroupModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public GetGroupModel setBody(GetGroupResponse body) {
        this.body = body;
        return this;
    }
    public GetGroupResponse getBody() {
        return this.body;
    }

}
