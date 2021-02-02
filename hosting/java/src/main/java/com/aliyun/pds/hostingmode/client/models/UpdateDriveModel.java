// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.hostingmode.client.models;

import com.aliyun.tea.*;

public class UpdateDriveModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public UpdateDriveResponse body;

    public static UpdateDriveModel build(java.util.Map<String, ?> map) throws Exception {
        UpdateDriveModel self = new UpdateDriveModel();
        return TeaModel.build(map, self);
    }

    public UpdateDriveModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public UpdateDriveModel setBody(UpdateDriveResponse body) {
        this.body = body;
        return this;
    }
    public UpdateDriveResponse getBody() {
        return this.body;
    }

}
