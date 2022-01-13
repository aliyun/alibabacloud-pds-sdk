// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class CopyFilesModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public CopyViewFilesResponse body;

    public static CopyFilesModel build(java.util.Map<String, ?> map) throws Exception {
        CopyFilesModel self = new CopyFilesModel();
        return TeaModel.build(map, self);
    }

    public CopyFilesModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public CopyFilesModel setBody(CopyViewFilesResponse body) {
        this.body = body;
        return this;
    }
    public CopyViewFilesResponse getBody() {
        return this.body;
    }

}
