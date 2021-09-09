// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class CreateFileWithSignatureModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public UCCreateFileResponse body;

    public static CreateFileWithSignatureModel build(java.util.Map<String, ?> map) throws Exception {
        CreateFileWithSignatureModel self = new CreateFileWithSignatureModel();
        return TeaModel.build(map, self);
    }

    public CreateFileWithSignatureModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public CreateFileWithSignatureModel setBody(UCCreateFileResponse body) {
        this.body = body;
        return this;
    }
    public UCCreateFileResponse getBody() {
        return this.body;
    }

}
