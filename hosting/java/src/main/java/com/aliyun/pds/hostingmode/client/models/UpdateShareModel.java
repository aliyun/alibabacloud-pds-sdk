// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.hostingmode.client.models;

import com.aliyun.tea.*;

public class UpdateShareModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public UpdateShareResponse body;

    public static UpdateShareModel build(java.util.Map<String, ?> map) throws Exception {
        UpdateShareModel self = new UpdateShareModel();
        return TeaModel.build(map, self);
    }

    public UpdateShareModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public UpdateShareModel setBody(UpdateShareResponse body) {
        this.body = body;
        return this;
    }
    public UpdateShareResponse getBody() {
        return this.body;
    }

}
