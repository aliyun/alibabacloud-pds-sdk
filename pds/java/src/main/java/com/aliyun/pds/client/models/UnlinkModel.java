// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class UnlinkModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    public static UnlinkModel build(java.util.Map<String, ?> map) throws Exception {
        UnlinkModel self = new UnlinkModel();
        return TeaModel.build(map, self);
    }

    public UnlinkModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

}
