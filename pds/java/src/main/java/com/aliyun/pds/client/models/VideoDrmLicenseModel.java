// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class VideoDrmLicenseModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public CCPVideoDRMLicenseResponse body;

    public static VideoDrmLicenseModel build(java.util.Map<String, ?> map) throws Exception {
        VideoDrmLicenseModel self = new VideoDrmLicenseModel();
        return TeaModel.build(map, self);
    }

    public VideoDrmLicenseModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public VideoDrmLicenseModel setBody(CCPVideoDRMLicenseResponse body) {
        this.body = body;
        return this;
    }
    public CCPVideoDRMLicenseResponse getBody() {
        return this.body;
    }

}
