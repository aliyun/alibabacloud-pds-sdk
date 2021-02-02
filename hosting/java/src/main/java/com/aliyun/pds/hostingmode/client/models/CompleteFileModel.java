// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.hostingmode.client.models;

import com.aliyun.tea.*;

public class CompleteFileModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public HostingCompleteFileResponse body;

    public static CompleteFileModel build(java.util.Map<String, ?> map) throws Exception {
        CompleteFileModel self = new CompleteFileModel();
        return TeaModel.build(map, self);
    }

    public CompleteFileModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public CompleteFileModel setBody(HostingCompleteFileResponse body) {
        this.body = body;
        return this;
    }
    public HostingCompleteFileResponse getBody() {
        return this.body;
    }

}
