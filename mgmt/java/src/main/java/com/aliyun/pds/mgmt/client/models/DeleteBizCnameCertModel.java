// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

public class DeleteBizCnameCertModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    public static DeleteBizCnameCertModel build(java.util.Map<String, ?> map) throws Exception {
        DeleteBizCnameCertModel self = new DeleteBizCnameCertModel();
        return TeaModel.build(map, self);
    }

    public DeleteBizCnameCertModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

}
