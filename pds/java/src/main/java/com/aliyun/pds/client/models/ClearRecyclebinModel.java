// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class ClearRecyclebinModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public ClearRecycleBinResponse body;

    public static ClearRecyclebinModel build(java.util.Map<String, ?> map) throws Exception {
        ClearRecyclebinModel self = new ClearRecyclebinModel();
        return TeaModel.build(map, self);
    }

    public ClearRecyclebinModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public ClearRecyclebinModel setBody(ClearRecycleBinResponse body) {
        this.body = body;
        return this;
    }
    public ClearRecycleBinResponse getBody() {
        return this.body;
    }

}
