// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class CancelShareLinkModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    public static CancelShareLinkModel build(java.util.Map<String, ?> map) throws Exception {
        CancelShareLinkModel self = new CancelShareLinkModel();
        return TeaModel.build(map, self);
    }

    public CancelShareLinkModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

}
