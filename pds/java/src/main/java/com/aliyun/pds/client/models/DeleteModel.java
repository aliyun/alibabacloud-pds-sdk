// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class DeleteModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    public static DeleteModel build(java.util.Map<String, ?> map) throws Exception {
        DeleteModel self = new DeleteModel();
        return TeaModel.build(map, self);
    }

    public DeleteModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

}
