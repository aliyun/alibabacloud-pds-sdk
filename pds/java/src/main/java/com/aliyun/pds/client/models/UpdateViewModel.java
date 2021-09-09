// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class UpdateViewModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    public static UpdateViewModel build(java.util.Map<String, ?> map) throws Exception {
        UpdateViewModel self = new UpdateViewModel();
        return TeaModel.build(map, self);
    }

    public UpdateViewModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

}
