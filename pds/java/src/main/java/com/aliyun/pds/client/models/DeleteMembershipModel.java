// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class DeleteMembershipModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public DeleteMembershipResponse body;

    public static DeleteMembershipModel build(java.util.Map<String, ?> map) throws Exception {
        DeleteMembershipModel self = new DeleteMembershipModel();
        return TeaModel.build(map, self);
    }

    public DeleteMembershipModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public DeleteMembershipModel setBody(DeleteMembershipResponse body) {
        this.body = body;
        return this;
    }
    public DeleteMembershipResponse getBody() {
        return this.body;
    }

}
