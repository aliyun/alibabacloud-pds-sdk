// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class CreateIdentityToBenefitPkgMappingModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public CreateIdentityToBenefitPkgMappingResponse body;

    public static CreateIdentityToBenefitPkgMappingModel build(java.util.Map<String, ?> map) throws Exception {
        CreateIdentityToBenefitPkgMappingModel self = new CreateIdentityToBenefitPkgMappingModel();
        return TeaModel.build(map, self);
    }

    public CreateIdentityToBenefitPkgMappingModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public CreateIdentityToBenefitPkgMappingModel setBody(CreateIdentityToBenefitPkgMappingResponse body) {
        this.body = body;
        return this;
    }
    public CreateIdentityToBenefitPkgMappingResponse getBody() {
        return this.body;
    }

}
