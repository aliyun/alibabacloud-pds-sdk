// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class ListDeviceModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public ListDeviceResponse body;

    public static ListDeviceModel build(java.util.Map<String, ?> map) throws Exception {
        ListDeviceModel self = new ListDeviceModel();
        return TeaModel.build(map, self);
    }

    public ListDeviceModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public ListDeviceModel setBody(ListDeviceResponse body) {
        this.body = body;
        return this;
    }
    public ListDeviceResponse getBody() {
        return this.body;
    }

}
