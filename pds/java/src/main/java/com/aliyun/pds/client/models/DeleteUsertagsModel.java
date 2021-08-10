// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class DeleteUsertagsModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    public static DeleteUsertagsModel build(java.util.Map<String, ?> map) throws Exception {
        DeleteUsertagsModel self = new DeleteUsertagsModel();
        return TeaModel.build(map, self);
    }

    public DeleteUsertagsModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

}
