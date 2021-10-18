// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class AddPermissionModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    public static AddPermissionModel build(java.util.Map<String, ?> map) throws Exception {
        AddPermissionModel self = new AddPermissionModel();
        return TeaModel.build(map, self);
    }

    public AddPermissionModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

}
