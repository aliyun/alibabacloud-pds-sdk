// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class ListMyDrivesModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public ListDriveResponse body;

    public static ListMyDrivesModel build(java.util.Map<String, ?> map) throws Exception {
        ListMyDrivesModel self = new ListMyDrivesModel();
        return TeaModel.build(map, self);
    }

    public ListMyDrivesModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public ListMyDrivesModel setBody(ListDriveResponse body) {
        this.body = body;
        return this;
    }
    public ListDriveResponse getBody() {
        return this.body;
    }

}
