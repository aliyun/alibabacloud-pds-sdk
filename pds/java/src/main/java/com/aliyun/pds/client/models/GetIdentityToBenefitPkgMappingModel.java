// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class GetIdentityToBenefitPkgMappingModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public BaseIdentityToBenefitPkgMappingResponse body;

    public static GetIdentityToBenefitPkgMappingModel build(java.util.Map<String, ?> map) throws Exception {
        GetIdentityToBenefitPkgMappingModel self = new GetIdentityToBenefitPkgMappingModel();
        return TeaModel.build(map, self);
    }

    public GetIdentityToBenefitPkgMappingModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public GetIdentityToBenefitPkgMappingModel setBody(BaseIdentityToBenefitPkgMappingResponse body) {
        this.body = body;
        return this;
    }
    public BaseIdentityToBenefitPkgMappingResponse getBody() {
        return this.body;
    }

}
