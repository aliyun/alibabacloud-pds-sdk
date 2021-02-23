// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class GetMembershipModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public GetMembershipResponse body;

    public static GetMembershipModel build(java.util.Map<String, ?> map) throws Exception {
        GetMembershipModel self = new GetMembershipModel();
        return TeaModel.build(map, self);
    }

    public GetMembershipModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public GetMembershipModel setBody(GetMembershipResponse body) {
        this.body = body;
        return this;
    }
    public GetMembershipResponse getBody() {
        return this.body;
    }

}
