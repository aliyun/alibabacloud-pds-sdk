// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class ListIdentityToBenefitPkgMappingModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public ListIdentityToBenefitPkgMappingResponse body;

    public static ListIdentityToBenefitPkgMappingModel build(java.util.Map<String, ?> map) throws Exception {
        ListIdentityToBenefitPkgMappingModel self = new ListIdentityToBenefitPkgMappingModel();
        return TeaModel.build(map, self);
    }

    public ListIdentityToBenefitPkgMappingModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public ListIdentityToBenefitPkgMappingModel setBody(ListIdentityToBenefitPkgMappingResponse body) {
        this.body = body;
        return this;
    }
    public ListIdentityToBenefitPkgMappingResponse getBody() {
        return this.body;
    }

}
