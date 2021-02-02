// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.hostingmode.client.models;

import com.aliyun.tea.*;

public class CopyFileModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public HostingCopyFileResponse body;

    public static CopyFileModel build(java.util.Map<String, ?> map) throws Exception {
        CopyFileModel self = new CopyFileModel();
        return TeaModel.build(map, self);
    }

    public CopyFileModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public CopyFileModel setBody(HostingCopyFileResponse body) {
        this.body = body;
        return this;
    }
    public HostingCopyFileResponse getBody() {
        return this.body;
    }

}
