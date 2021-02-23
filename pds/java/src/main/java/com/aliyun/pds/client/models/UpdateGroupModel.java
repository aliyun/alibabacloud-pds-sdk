// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class UpdateGroupModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public UpdateGroupResponse body;

    public static UpdateGroupModel build(java.util.Map<String, ?> map) throws Exception {
        UpdateGroupModel self = new UpdateGroupModel();
        return TeaModel.build(map, self);
    }

    public UpdateGroupModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public UpdateGroupModel setBody(UpdateGroupResponse body) {
        this.body = body;
        return this;
    }
    public UpdateGroupResponse getBody() {
        return this.body;
    }

}
