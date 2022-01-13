// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class BindDeviceModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public BindDeviceResponse body;

    public static BindDeviceModel build(java.util.Map<String, ?> map) throws Exception {
        BindDeviceModel self = new BindDeviceModel();
        return TeaModel.build(map, self);
    }

    public BindDeviceModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public BindDeviceModel setBody(BindDeviceResponse body) {
        this.body = body;
        return this;
    }
    public BindDeviceResponse getBody() {
        return this.body;
    }

}
