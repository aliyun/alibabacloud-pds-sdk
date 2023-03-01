// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * DRM License response
 */
public class CCPVideoDRMLicenseResponse extends TeaModel {
    /**
     * <p>drm_data</p>
     */
    @NameInMap("data")
    public String data;

    /**
     * <p>device_info</p>
     */
    @NameInMap("device_info")
    public String deviceInfo;

    /**
     * <p>states</p>
     */
    @NameInMap("states")
    public Long states;

    public static CCPVideoDRMLicenseResponse build(java.util.Map<String, ?> map) throws Exception {
        CCPVideoDRMLicenseResponse self = new CCPVideoDRMLicenseResponse();
        return TeaModel.build(map, self);
    }

    public CCPVideoDRMLicenseResponse setData(String data) {
        this.data = data;
        return this;
    }
    public String getData() {
        return this.data;
    }

    public CCPVideoDRMLicenseResponse setDeviceInfo(String deviceInfo) {
        this.deviceInfo = deviceInfo;
        return this;
    }
    public String getDeviceInfo() {
        return this.deviceInfo;
    }

    public CCPVideoDRMLicenseResponse setStates(Long states) {
        this.states = states;
        return this;
    }
    public Long getStates() {
        return this.states;
    }

}
