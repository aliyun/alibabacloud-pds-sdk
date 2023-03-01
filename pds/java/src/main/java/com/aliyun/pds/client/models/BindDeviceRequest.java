// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class BindDeviceRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    /**
     * <p>device_info</p>
     */
    @NameInMap("device_info")
    public String deviceInfo;

    /**
     * <p>device_name</p>
     */
    @NameInMap("device_name")
    public String deviceName;

    /**
     * <p>device_type</p>
     */
    @NameInMap("device_type")
    public String deviceType;

    /**
     * <p>fs_type</p>
     */
    @NameInMap("fs_type")
    public String fsType;

    /**
     * <p>manufacturer</p>
     */
    @NameInMap("manufacturer")
    public String manufacturer;

    /**
     * <p>total_size</p>
     */
    @NameInMap("total_size")
    public Long totalSize;

    /**
     * <p>used_size</p>
     */
    @NameInMap("used_size")
    public Long usedSize;

    public static BindDeviceRequest build(java.util.Map<String, ?> map) throws Exception {
        BindDeviceRequest self = new BindDeviceRequest();
        return TeaModel.build(map, self);
    }

    public BindDeviceRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public BindDeviceRequest setDeviceInfo(String deviceInfo) {
        this.deviceInfo = deviceInfo;
        return this;
    }
    public String getDeviceInfo() {
        return this.deviceInfo;
    }

    public BindDeviceRequest setDeviceName(String deviceName) {
        this.deviceName = deviceName;
        return this;
    }
    public String getDeviceName() {
        return this.deviceName;
    }

    public BindDeviceRequest setDeviceType(String deviceType) {
        this.deviceType = deviceType;
        return this;
    }
    public String getDeviceType() {
        return this.deviceType;
    }

    public BindDeviceRequest setFsType(String fsType) {
        this.fsType = fsType;
        return this;
    }
    public String getFsType() {
        return this.fsType;
    }

    public BindDeviceRequest setManufacturer(String manufacturer) {
        this.manufacturer = manufacturer;
        return this;
    }
    public String getManufacturer() {
        return this.manufacturer;
    }

    public BindDeviceRequest setTotalSize(Long totalSize) {
        this.totalSize = totalSize;
        return this;
    }
    public Long getTotalSize() {
        return this.totalSize;
    }

    public BindDeviceRequest setUsedSize(Long usedSize) {
        this.usedSize = usedSize;
        return this;
    }
    public Long getUsedSize() {
        return this.usedSize;
    }

}
