// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class DeleteIdentityToBenefitPkgMappingModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public DeleteIdentityToBenefitPkgMappingResponse body;

    public static DeleteIdentityToBenefitPkgMappingModel build(java.util.Map<String, ?> map) throws Exception {
        DeleteIdentityToBenefitPkgMappingModel self = new DeleteIdentityToBenefitPkgMappingModel();
        return TeaModel.build(map, self);
    }

    public DeleteIdentityToBenefitPkgMappingModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public DeleteIdentityToBenefitPkgMappingModel setBody(DeleteIdentityToBenefitPkgMappingResponse body) {
        this.body = body;
        return this;
    }
    public DeleteIdentityToBenefitPkgMappingResponse getBody() {
        return this.body;
    }

}
