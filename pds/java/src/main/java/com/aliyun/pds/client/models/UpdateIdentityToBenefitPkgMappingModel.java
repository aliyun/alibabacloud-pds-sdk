// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class UpdateIdentityToBenefitPkgMappingModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public UpdateIdentityToBenefitPkgMappingResponse body;

    public static UpdateIdentityToBenefitPkgMappingModel build(java.util.Map<String, ?> map) throws Exception {
        UpdateIdentityToBenefitPkgMappingModel self = new UpdateIdentityToBenefitPkgMappingModel();
        return TeaModel.build(map, self);
    }

    public UpdateIdentityToBenefitPkgMappingModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public UpdateIdentityToBenefitPkgMappingModel setBody(UpdateIdentityToBenefitPkgMappingResponse body) {
        this.body = body;
        return this;
    }
    public UpdateIdentityToBenefitPkgMappingResponse getBody() {
        return this.body;
    }

}
