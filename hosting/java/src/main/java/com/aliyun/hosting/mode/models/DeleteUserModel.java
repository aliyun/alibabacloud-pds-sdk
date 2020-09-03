// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.hosting.mode.models;

import com.aliyun.tea.*;

public class DeleteUserModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    public static DeleteUserModel build(java.util.Map<String, ?> map) throws Exception {
        DeleteUserModel self = new DeleteUserModel();
        return TeaModel.build(map, self);
    }

    public DeleteUserModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

}
