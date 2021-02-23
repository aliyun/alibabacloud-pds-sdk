// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class DeleteGroupModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public DeleteGroupResponse body;

    public static DeleteGroupModel build(java.util.Map<String, ?> map) throws Exception {
        DeleteGroupModel self = new DeleteGroupModel();
        return TeaModel.build(map, self);
    }

    public DeleteGroupModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public DeleteGroupModel setBody(DeleteGroupResponse body) {
        this.body = body;
        return this;
    }
    public DeleteGroupResponse getBody() {
        return this.body;
    }

}
