// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.hostingmode.client.models;

import com.aliyun.tea.*;

public class ListDrivesModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public ListDriveResponse body;

    public static ListDrivesModel build(java.util.Map<String, ?> map) throws Exception {
        ListDrivesModel self = new ListDrivesModel();
        return TeaModel.build(map, self);
    }

    public ListDrivesModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public ListDrivesModel setBody(ListDriveResponse body) {
        this.body = body;
        return this;
    }
    public ListDriveResponse getBody() {
        return this.body;
    }

}
