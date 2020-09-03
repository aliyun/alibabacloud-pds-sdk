// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.hosting.mode.models;

import com.aliyun.tea.*;

/**
 * DRM License response
 */
public class OSSVideoDRMLicenseResponse extends TeaModel {
    // drm_data
    @NameInMap("data")
    @Validation(required = true)
    public String data;

    // states
    @NameInMap("states")
    @Validation(required = true)
    public Long states;

    public static OSSVideoDRMLicenseResponse build(java.util.Map<String, ?> map) throws Exception {
        OSSVideoDRMLicenseResponse self = new OSSVideoDRMLicenseResponse();
        return TeaModel.build(map, self);
    }

    public OSSVideoDRMLicenseResponse setData(String data) {
        this.data = data;
        return this;
    }
    public String getData() {
        return this.data;
    }

    public OSSVideoDRMLicenseResponse setStates(Long states) {
        this.states = states;
        return this;
    }
    public Long getStates() {
        return this.states;
    }

}
