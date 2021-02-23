// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class ListDirectChildMembershipsModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public ListDirectChildMembershipsResponse body;

    public static ListDirectChildMembershipsModel build(java.util.Map<String, ?> map) throws Exception {
        ListDirectChildMembershipsModel self = new ListDirectChildMembershipsModel();
        return TeaModel.build(map, self);
    }

    public ListDirectChildMembershipsModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public ListDirectChildMembershipsModel setBody(ListDirectChildMembershipsResponse body) {
        this.body = body;
        return this;
    }
    public ListDirectChildMembershipsResponse getBody() {
        return this.body;
    }

}
