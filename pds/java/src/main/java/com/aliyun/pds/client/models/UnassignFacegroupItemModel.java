// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class UnassignFacegroupItemModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    public static UnassignFacegroupItemModel build(java.util.Map<String, ?> map) throws Exception {
        UnassignFacegroupItemModel self = new UnassignFacegroupItemModel();
        return TeaModel.build(map, self);
    }

    public UnassignFacegroupItemModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

}
