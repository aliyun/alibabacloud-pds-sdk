// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class AddFileModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public AddViewFileResponse body;

    public static AddFileModel build(java.util.Map<String, ?> map) throws Exception {
        AddFileModel self = new AddFileModel();
        return TeaModel.build(map, self);
    }

    public AddFileModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public AddFileModel setBody(AddViewFileResponse body) {
        this.body = body;
        return this;
    }
    public AddViewFileResponse getBody() {
        return this.body;
    }

}
