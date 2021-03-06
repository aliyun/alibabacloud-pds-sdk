// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.hostingmode.client.models;

import com.aliyun.tea.*;

public class CreateFileModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public HostingCreateFileResponse body;

    public static CreateFileModel build(java.util.Map<String, ?> map) throws Exception {
        CreateFileModel self = new CreateFileModel();
        return TeaModel.build(map, self);
    }

    public CreateFileModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public CreateFileModel setBody(HostingCreateFileResponse body) {
        this.body = body;
        return this;
    }
    public HostingCreateFileResponse getBody() {
        return this.body;
    }

}
