// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * DRM License response
 */
public class HostingVideoDRMLicenseResponse extends TeaModel {
    /**
     * <p>drm_data</p>
     */
    @NameInMap("data")
    @Validation(required = true)
    public String data;

    /**
     * <p>device_info</p>
     */
    @NameInMap("device_info")
    @Validation(required = true)
    public String deviceInfo;

    /**
     * <p>states</p>
     */
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

    public HostingVideoDRMLicenseResponse setDeviceInfo(String deviceInfo) {
        this.deviceInfo = deviceInfo;
        return this;
    }
    public String getDeviceInfo() {
        return this.deviceInfo;
    }

    public HostingVideoDRMLicenseResponse setStates(Long states) {
        this.states = states;
        return this;
    }
    public Long getStates() {
        return this.states;
    }

}
