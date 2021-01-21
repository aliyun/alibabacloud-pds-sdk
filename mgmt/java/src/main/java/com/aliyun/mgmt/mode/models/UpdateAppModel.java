// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.mgmt.mode.models;

import com.aliyun.tea.*;

public class UpdateAppModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public GetAppResponse body;

    public static UpdateAppModel build(java.util.Map<String, ?> map) throws Exception {
        UpdateAppModel self = new UpdateAppModel();
        return TeaModel.build(map, self);
    }

    public UpdateAppModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public UpdateAppModel setBody(GetAppResponse body) {
        this.body = body;
        return this;
    }
    public GetAppResponse getBody() {
        return this.body;
    }

}
