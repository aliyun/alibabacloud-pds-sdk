// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.hostingmode.client.models;

import com.aliyun.tea.*;

public class DeleteShareModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    public static DeleteShareModel build(java.util.Map<String, ?> map) throws Exception {
        DeleteShareModel self = new DeleteShareModel();
        return TeaModel.build(map, self);
    }

    public DeleteShareModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

}
