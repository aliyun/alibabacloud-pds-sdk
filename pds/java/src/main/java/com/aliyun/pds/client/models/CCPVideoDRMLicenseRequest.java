// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 获取视频DRM License
 */
public class CCPVideoDRMLicenseRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    // drmType
    @NameInMap("drmType")
    public String drmType;

    // licenseRequest
    @NameInMap("licenseRequest")
    public String licenseRequest;

    public static CCPVideoDRMLicenseRequest build(java.util.Map<String, ?> map) throws Exception {
        CCPVideoDRMLicenseRequest self = new CCPVideoDRMLicenseRequest();
        return TeaModel.build(map, self);
    }

    public CCPVideoDRMLicenseRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public CCPVideoDRMLicenseRequest setDrmType(String drmType) {
        this.drmType = drmType;
        return this;
    }
    public String getDrmType() {
        return this.drmType;
    }

    public CCPVideoDRMLicenseRequest setLicenseRequest(String licenseRequest) {
        this.licenseRequest = licenseRequest;
        return this;
    }
    public String getLicenseRequest() {
        return this.licenseRequest;
    }

}
