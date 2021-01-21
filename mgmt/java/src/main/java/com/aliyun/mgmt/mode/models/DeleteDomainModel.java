// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.mgmt.mode.models;

import com.aliyun.tea.*;

public class DeleteDomainModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    public static DeleteDomainModel build(java.util.Map<String, ?> map) throws Exception {
        DeleteDomainModel self = new DeleteDomainModel();
        return TeaModel.build(map, self);
    }

    public DeleteDomainModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

}
