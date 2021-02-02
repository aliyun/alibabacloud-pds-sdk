// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.hostingmode.client.models;

import com.aliyun.tea.*;

public class VideoLicenseModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public HostingVideoDRMLicenseResponse body;

    public static VideoLicenseModel build(java.util.Map<String, ?> map) throws Exception {
        VideoLicenseModel self = new VideoLicenseModel();
        return TeaModel.build(map, self);
    }

    public VideoLicenseModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public VideoLicenseModel setBody(HostingVideoDRMLicenseResponse body) {
        this.body = body;
        return this;
    }
    public HostingVideoDRMLicenseResponse getBody() {
        return this.body;
    }

}
