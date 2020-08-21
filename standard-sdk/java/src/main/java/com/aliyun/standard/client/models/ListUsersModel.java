// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.standard.client.models;

import com.aliyun.tea.*;

public class ListUsersModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public ListUserResponse body;

    public static ListUsersModel build(java.util.Map<String, ?> map) throws Exception {
        ListUsersModel self = new ListUsersModel();
        return TeaModel.build(map, self);
    }

    public ListUsersModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public ListUsersModel setBody(ListUserResponse body) {
        this.body = body;
        return this;
    }
    public ListUserResponse getBody() {
        return this.body;
    }

}
