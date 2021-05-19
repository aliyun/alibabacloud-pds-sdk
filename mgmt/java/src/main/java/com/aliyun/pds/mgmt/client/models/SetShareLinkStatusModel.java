// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

public class SetShareLinkStatusModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public BaseDomainResponse body;

    public static SetShareLinkStatusModel build(java.util.Map<String, ?> map) throws Exception {
        SetShareLinkStatusModel self = new SetShareLinkStatusModel();
        return TeaModel.build(map, self);
    }

    public SetShareLinkStatusModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public SetShareLinkStatusModel setBody(BaseDomainResponse body) {
        this.body = body;
        return this;
    }
    public BaseDomainResponse getBody() {
        return this.body;
    }

}
