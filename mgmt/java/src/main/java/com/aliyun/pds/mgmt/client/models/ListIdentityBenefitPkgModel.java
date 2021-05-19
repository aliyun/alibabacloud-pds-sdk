// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

public class ListIdentityBenefitPkgModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public ListIdentityBenefitPkgResponse body;

    public static ListIdentityBenefitPkgModel build(java.util.Map<String, ?> map) throws Exception {
        ListIdentityBenefitPkgModel self = new ListIdentityBenefitPkgModel();
        return TeaModel.build(map, self);
    }

    public ListIdentityBenefitPkgModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public ListIdentityBenefitPkgModel setBody(ListIdentityBenefitPkgResponse body) {
        this.body = body;
        return this;
    }
    public ListIdentityBenefitPkgResponse getBody() {
        return this.body;
    }

}
