// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.standard.client.models;

import com.aliyun.tea.*;

/**
 * 获取视频DRM License
 */
public class OSSVideoDRMLicenseRequest extends TeaModel {
    // drmType
    @NameInMap("drmType")
    @Validation(required = true)
    public String drmType;

    // licenseRequest
    @NameInMap("licenseRequest")
    @Validation(required = true)
    public String licenseRequest;

    public static OSSVideoDRMLicenseRequest build(java.util.Map<String, ?> map) throws Exception {
        OSSVideoDRMLicenseRequest self = new OSSVideoDRMLicenseRequest();
        return TeaModel.build(map, self);
    }

    public OSSVideoDRMLicenseRequest setDrmType(String drmType) {
        this.drmType = drmType;
        return this;
    }
    public String getDrmType() {
        return this.drmType;
    }

    public OSSVideoDRMLicenseRequest setLicenseRequest(String licenseRequest) {
        this.licenseRequest = licenseRequest;
        return this;
    }
    public String getLicenseRequest() {
        return this.licenseRequest;
    }

}
