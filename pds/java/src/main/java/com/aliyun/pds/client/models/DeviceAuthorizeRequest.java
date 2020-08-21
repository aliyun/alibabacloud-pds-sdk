// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class DeviceAuthorizeRequest extends TeaModel {
    // Client ID, 此处填写创建App时返回的AppID
    @NameInMap("ClientID")
    @Validation(required = true)
    public String ClientID;

    // 设备信息，用于用户识别设备
    @NameInMap("DeviceInfo")
    public String DeviceInfo;

    // 设备名，实现方需保证不同设备的设备名不重复（推荐用硬件名称+硬件型号作为设备名）
    @NameInMap("DeviceName")
    @Validation(required = true)
    public String DeviceName;

    // 鉴权方式，目前支持ding,ram鉴权
    @NameInMap("LoginType")
    public String LoginType;

    // 申请的权限列表, 默认为所有权限
    @NameInMap("Scope")
    public java.util.List<String> Scope;

    public static DeviceAuthorizeRequest build(java.util.Map<String, ?> map) throws Exception {
        DeviceAuthorizeRequest self = new DeviceAuthorizeRequest();
        return TeaModel.build(map, self);
    }

    public DeviceAuthorizeRequest setClientID(String ClientID) {
        this.ClientID = ClientID;
        return this;
    }
    public String getClientID() {
        return this.ClientID;
    }

    public DeviceAuthorizeRequest setDeviceInfo(String DeviceInfo) {
        this.DeviceInfo = DeviceInfo;
        return this;
    }
    public String getDeviceInfo() {
        return this.DeviceInfo;
    }

    public DeviceAuthorizeRequest setDeviceName(String DeviceName) {
        this.DeviceName = DeviceName;
        return this;
    }
    public String getDeviceName() {
        return this.DeviceName;
    }

    public DeviceAuthorizeRequest setLoginType(String LoginType) {
        this.LoginType = LoginType;
        return this;
    }
    public String getLoginType() {
        return this.LoginType;
    }

    public DeviceAuthorizeRequest setScope(java.util.List<String> Scope) {
        this.Scope = Scope;
        return this;
    }
    public java.util.List<String> getScope() {
        return this.Scope;
    }

}
