// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 获取视频DRM License
 */
public class HostingVideoDRMLicenseRequest extends TeaModel {
    // drmType
    @NameInMap("drmType")
    @Validation(required = true)
    public String drmType;

    // licenseRequest
    @NameInMap("licenseRequest")
    @Validation(required = true)
    public String licenseRequest;

    public static HostingVideoDRMLicenseRequest build(java.util.Map<String, ?> map) throws Exception {
        HostingVideoDRMLicenseRequest self = new HostingVideoDRMLicenseRequest();
        return TeaModel.build(map, self);
    }

    public HostingVideoDRMLicenseRequest setDrmType(String drmType) {
        this.drmType = drmType;
        return this;
    }
    public String getDrmType() {
        return this.drmType;
    }

    public HostingVideoDRMLicenseRequest setLicenseRequest(String licenseRequest) {
        this.licenseRequest = licenseRequest;
        return this;
    }
    public String getLicenseRequest() {
        return this.licenseRequest;
    }

}
