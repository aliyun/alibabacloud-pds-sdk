// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class RestoreFileRevisionModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public GetRevisionResponse body;

    public static RestoreFileRevisionModel build(java.util.Map<String, ?> map) throws Exception {
        RestoreFileRevisionModel self = new RestoreFileRevisionModel();
        return TeaModel.build(map, self);
    }

    public RestoreFileRevisionModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public RestoreFileRevisionModel setBody(GetRevisionResponse body) {
        this.body = body;
        return this;
    }
    public GetRevisionResponse getBody() {
        return this.body;
    }

}
