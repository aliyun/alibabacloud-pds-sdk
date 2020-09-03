// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.hosting.mode.models;

import com.aliyun.tea.*;

/**
 * DRM License response
 */
public class HostingVideoDRMLicenseResponse extends TeaModel {
    // drm_data
    @NameInMap("data")
    @Validation(required = true)
    public String data;

    // states
    @NameInMap("states")
    @Validation(required = true)
    public Long states;

    public static HostingVideoDRMLicenseResponse build(java.util.Map<String, ?> map) throws Exception {
        HostingVideoDRMLicenseResponse self = new HostingVideoDRMLicenseResponse();
        return TeaModel.build(map, self);
    }

    public HostingVideoDRMLicenseResponse setData(String data) {
        this.data = data;
        return this;
    }
    public String getData() {
        return this.data;
    }

    public HostingVideoDRMLicenseResponse setStates(Long states) {
        this.states = states;
        return this;
    }
    public Long getStates() {
        return this.states;
    }

}
