// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class UpdateMembershipModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public UpdateMembershipResponse body;

    public static UpdateMembershipModel build(java.util.Map<String, ?> map) throws Exception {
        UpdateMembershipModel self = new UpdateMembershipModel();
        return TeaModel.build(map, self);
    }

    public UpdateMembershipModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public UpdateMembershipModel setBody(UpdateMembershipResponse body) {
        this.body = body;
        return this;
    }
    public UpdateMembershipResponse getBody() {
        return this.body;
    }

}
