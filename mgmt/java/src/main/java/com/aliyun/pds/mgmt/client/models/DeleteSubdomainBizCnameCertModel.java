// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

public class DeleteSubdomainBizCnameCertModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    public static DeleteSubdomainBizCnameCertModel build(java.util.Map<String, ?> map) throws Exception {
        DeleteSubdomainBizCnameCertModel self = new DeleteSubdomainBizCnameCertModel();
        return TeaModel.build(map, self);
    }

    public DeleteSubdomainBizCnameCertModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

}
