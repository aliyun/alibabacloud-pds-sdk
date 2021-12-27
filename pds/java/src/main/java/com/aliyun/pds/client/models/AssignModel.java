// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class AssignModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    public static AssignModel build(java.util.Map<String, ?> map) throws Exception {
        AssignModel self = new AssignModel();
        return TeaModel.build(map, self);
    }

    public AssignModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

}
