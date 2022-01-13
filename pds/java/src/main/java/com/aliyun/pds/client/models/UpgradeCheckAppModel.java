// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class UpgradeCheckAppModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public UpgradeCheckAppResponse body;

    public static UpgradeCheckAppModel build(java.util.Map<String, ?> map) throws Exception {
        UpgradeCheckAppModel self = new UpgradeCheckAppModel();
        return TeaModel.build(map, self);
    }

    public UpgradeCheckAppModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public UpgradeCheckAppModel setBody(UpgradeCheckAppResponse body) {
        this.body = body;
        return this;
    }
    public UpgradeCheckAppResponse getBody() {
        return this.body;
    }

}
