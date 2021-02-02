// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.hostingmode.client.models;

import com.aliyun.tea.*;

public class DeleteDriveModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    public static DeleteDriveModel build(java.util.Map<String, ?> map) throws Exception {
        DeleteDriveModel self = new DeleteDriveModel();
        return TeaModel.build(map, self);
    }

    public DeleteDriveModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

}
