// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class RestoreFileModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public RestoreFileResponse body;

    public static RestoreFileModel build(java.util.Map<String, ?> map) throws Exception {
        RestoreFileModel self = new RestoreFileModel();
        return TeaModel.build(map, self);
    }

    public RestoreFileModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public RestoreFileModel setBody(RestoreFileResponse body) {
        this.body = body;
        return this;
    }
    public RestoreFileResponse getBody() {
        return this.body;
    }

}
