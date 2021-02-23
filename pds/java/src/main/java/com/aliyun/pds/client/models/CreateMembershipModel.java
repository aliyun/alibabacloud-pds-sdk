// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class CreateMembershipModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public CreateMembershipResponse body;

    public static CreateMembershipModel build(java.util.Map<String, ?> map) throws Exception {
        CreateMembershipModel self = new CreateMembershipModel();
        return TeaModel.build(map, self);
    }

    public CreateMembershipModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public CreateMembershipModel setBody(CreateMembershipResponse body) {
        this.body = body;
        return this;
    }
    public CreateMembershipResponse getBody() {
        return this.body;
    }

}
