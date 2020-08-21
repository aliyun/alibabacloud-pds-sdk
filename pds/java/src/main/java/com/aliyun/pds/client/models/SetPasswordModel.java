// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class SetPasswordModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    public static SetPasswordModel build(java.util.Map<String, ?> map) throws Exception {
        SetPasswordModel self = new SetPasswordModel();
        return TeaModel.build(map, self);
    }

    public SetPasswordModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

}
