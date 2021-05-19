// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

public class SetShareStatusModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public BaseDomainResponse body;

    public static SetShareStatusModel build(java.util.Map<String, ?> map) throws Exception {
        SetShareStatusModel self = new SetShareStatusModel();
        return TeaModel.build(map, self);
    }

    public SetShareStatusModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public SetShareStatusModel setBody(BaseDomainResponse body) {
        this.body = body;
        return this;
    }
    public BaseDomainResponse getBody() {
        return this.body;
    }

}
