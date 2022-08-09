// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 *
 */
public class DeviceItem extends TeaModel {
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

    public static DeviceItem build(java.util.Map<String, ?> map) throws Exception {
        DeviceItem self = new DeviceItem();
        return TeaModel.build(map, self);
    }

    public DeviceItem setCreatedAt(String createdAt) {
        this.createdAt = createdAt;
        return this;
    }
    public String getCreatedAt() {
        return this.createdAt;
    }

    public DeviceItem setDeviceId(String deviceId) {
        this.deviceId = deviceId;
        return this;
    }
    public String getDeviceId() {
        return this.deviceId;
    }

    public DeviceItem setDeviceInfo(String deviceInfo) {
        this.deviceInfo = deviceInfo;
        return this;
    }
    public String getDeviceInfo() {
        return this.deviceInfo;
    }

    public DeviceItem setDeviceName(String deviceName) {
        this.deviceName = deviceName;
        return this;
    }
    public String getDeviceName() {
        return this.deviceName;
    }

    public DeviceItem setDeviceType(String deviceType) {
        this.deviceType = deviceType;
        return this;
    }
    public String getDeviceType() {
        return this.deviceType;
    }

    public DeviceItem setUpdatedAt(String updatedAt) {
        this.updatedAt = updatedAt;
        return this;
    }
    public String getUpdatedAt() {
        return this.updatedAt;
    }

}
