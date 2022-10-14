// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class BindDeviceResponse extends TeaModel {
    // created_at
    @NameInMap("created_at")
    public String createdAt;

    // device_id
    @NameInMap("device_id")
    public String deviceId;

    // device_info
    @NameInMap("device_info")
    public String deviceInfo;

    // device_name
    @NameInMap("device_name")
    public String deviceName;

    // device_type
    @NameInMap("device_type")
    public String deviceType;

    // updated_at
    @NameInMap("updated_at")
    public String updatedAt;

    public static BindDeviceResponse build(java.util.Map<String, ?> map) throws Exception {
        BindDeviceResponse self = new BindDeviceResponse();
        return TeaModel.build(map, self);
    }

    public BindDeviceResponse setCreatedAt(String createdAt) {
        this.createdAt = createdAt;
        return this;
    }
    public String getCreatedAt() {
        return this.createdAt;
    }

    public BindDeviceResponse setDeviceId(String deviceId) {
        this.deviceId = deviceId;
        return this;
    }
    public String getDeviceId() {
        return this.deviceId;
    }

    public BindDeviceResponse setDeviceInfo(String deviceInfo) {
        this.deviceInfo = deviceInfo;
        return this;
    }
    public String getDeviceInfo() {
        return this.deviceInfo;
    }

    public BindDeviceResponse setDeviceName(String deviceName) {
        this.deviceName = deviceName;
        return this;
    }
    public String getDeviceName() {
        return this.deviceName;
    }

    public BindDeviceResponse setDeviceType(String deviceType) {
        this.deviceType = deviceType;
        return this;
    }
    public String getDeviceType() {
        return this.deviceType;
    }

    public BindDeviceResponse setUpdatedAt(String updatedAt) {
        this.updatedAt = updatedAt;
        return this;
    }
    public String getUpdatedAt() {
        return this.updatedAt;
    }

}
