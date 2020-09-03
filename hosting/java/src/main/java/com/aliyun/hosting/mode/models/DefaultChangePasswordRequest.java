// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.hosting.mode.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class DefaultChangePasswordRequest extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    // App ID, 当前访问的App
    @NameInMap("app_id")
    @Validation(required = true)
    public String appId;

    // AES-256对称加密密钥，通过App公钥加密后传输
    @NameInMap("encrypted_key")
    @Validation(required = true)
    public String encryptedKey;

    // 新密码，必须包含数字和字母，长度8-20个字符
    @NameInMap("new_password")
    @Validation(required = true)
    public String newPassword;

    // 手机号
    @NameInMap("phone_number")
    @Validation(required = true)
    public String phoneNumber;

    // 国家编号，默认86，不需要填+号，直接填数字
    @NameInMap("phone_region")
    public String phoneRegion;

    // 修改密码的临时授权码
    @NameInMap("state")
    @Validation(required = true)
    public String state;

    public static DefaultChangePasswordRequest build(java.util.Map<String, ?> map) throws Exception {
        DefaultChangePasswordRequest self = new DefaultChangePasswordRequest();
        return TeaModel.build(map, self);
    }

    public DefaultChangePasswordRequest setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public DefaultChangePasswordRequest setAppId(String appId) {
        this.appId = appId;
        return this;
    }
    public String getAppId() {
        return this.appId;
    }

    public DefaultChangePasswordRequest setEncryptedKey(String encryptedKey) {
        this.encryptedKey = encryptedKey;
        return this;
    }
    public String getEncryptedKey() {
        return this.encryptedKey;
    }

    public DefaultChangePasswordRequest setNewPassword(String newPassword) {
        this.newPassword = newPassword;
        return this;
    }
    public String getNewPassword() {
        return this.newPassword;
    }

    public DefaultChangePasswordRequest setPhoneNumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
        return this;
    }
    public String getPhoneNumber() {
        return this.phoneNumber;
    }

    public DefaultChangePasswordRequest setPhoneRegion(String phoneRegion) {
        this.phoneRegion = phoneRegion;
        return this;
    }
    public String getPhoneRegion() {
        return this.phoneRegion;
    }

    public DefaultChangePasswordRequest setState(String state) {
        this.state = state;
        return this;
    }
    public String getState() {
        return this.state;
    }

}
