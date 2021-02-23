// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class ListGroupModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public ListGroupResponse body;

    public static ListGroupModel build(java.util.Map<String, ?> map) throws Exception {
        ListGroupModel self = new ListGroupModel();
        return TeaModel.build(map, self);
    }

    public ListGroupModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public ListGroupModel setBody(ListGroupResponse body) {
        this.body = body;
        return this;
    }
    public ListGroupResponse getBody() {
        return this.body;
    }

}
