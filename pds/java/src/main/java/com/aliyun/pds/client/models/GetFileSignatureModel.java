// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class GetFileSignatureModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public UCGetSignatureResponse body;

    public static GetFileSignatureModel build(java.util.Map<String, ?> map) throws Exception {
        GetFileSignatureModel self = new GetFileSignatureModel();
        return TeaModel.build(map, self);
    }

    public GetFileSignatureModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public GetFileSignatureModel setBody(UCGetSignatureResponse body) {
        this.body = body;
        return this;
    }
    public UCGetSignatureResponse getBody() {
        return this.body;
    }

}
