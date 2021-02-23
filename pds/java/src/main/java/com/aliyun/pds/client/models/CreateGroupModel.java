// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class CreateGroupModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public CreateGroupResponse body;

    public static CreateGroupModel build(java.util.Map<String, ?> map) throws Exception {
        CreateGroupModel self = new CreateGroupModel();
        return TeaModel.build(map, self);
    }

    public CreateGroupModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public CreateGroupModel setBody(CreateGroupResponse body) {
        this.body = body;
        return this;
    }
    public CreateGroupResponse getBody() {
        return this.body;
    }

}
