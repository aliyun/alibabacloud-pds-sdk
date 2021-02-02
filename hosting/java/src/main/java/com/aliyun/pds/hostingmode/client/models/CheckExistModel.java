// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.hostingmode.client.models;

import com.aliyun.tea.*;

public class CheckExistModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public MobileCheckExistResponse body;

    public static CheckExistModel build(java.util.Map<String, ?> map) throws Exception {
        CheckExistModel self = new CheckExistModel();
        return TeaModel.build(map, self);
    }

    public CheckExistModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public CheckExistModel setBody(MobileCheckExistResponse body) {
        this.body = body;
        return this;
    }
    public MobileCheckExistResponse getBody() {
        return this.body;
    }

}
