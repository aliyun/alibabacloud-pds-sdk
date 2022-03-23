// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

public class DeleteSubdomainBizCnameAndCertModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    public static DeleteSubdomainBizCnameAndCertModel build(java.util.Map<String, ?> map) throws Exception {
        DeleteSubdomainBizCnameAndCertModel self = new DeleteSubdomainBizCnameAndCertModel();
        return TeaModel.build(map, self);
    }

    public DeleteSubdomainBizCnameAndCertModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

}
