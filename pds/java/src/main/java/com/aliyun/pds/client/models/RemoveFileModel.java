// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class RemoveFileModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    public static RemoveFileModel build(java.util.Map<String, ?> map) throws Exception {
        RemoveFileModel self = new RemoveFileModel();
        return TeaModel.build(map, self);
    }

    public RemoveFileModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

}
