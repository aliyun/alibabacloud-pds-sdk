// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class UpdateShareLinkModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public UpdateShareLinkResponse body;

    public static UpdateShareLinkModel build(java.util.Map<String, ?> map) throws Exception {
        UpdateShareLinkModel self = new UpdateShareLinkModel();
        return TeaModel.build(map, self);
    }

    public UpdateShareLinkModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public UpdateShareLinkModel setBody(UpdateShareLinkResponse body) {
        this.body = body;
        return this;
    }
    public UpdateShareLinkResponse getBody() {
        return this.body;
    }

}
