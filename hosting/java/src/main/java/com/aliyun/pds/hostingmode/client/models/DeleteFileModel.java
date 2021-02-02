// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.hostingmode.client.models;

import com.aliyun.tea.*;

public class DeleteFileModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    public static DeleteFileModel build(java.util.Map<String, ?> map) throws Exception {
        DeleteFileModel self = new DeleteFileModel();
        return TeaModel.build(map, self);
    }

    public DeleteFileModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

}
