// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class DefaultSetPasswordRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    // App ID, 当前访问的App
    @NameInMap("app_id")
    @Validation(required = true)
    public String appId;

    // AES-256对称加密密钥，通过App公钥加密后传输
    @NameInMap("encrypted_key")
    @Validation(required = true)
    public String encryptedKey;

    // 新密码，必须包含数字和字母，长度8-20个字符，使用AES-256对称加密后传输（CBC模式, 填充算法为PKCS7Padding，生成base64字符串）
    @NameInMap("new_password")
    @Validation(required = true)
    public String newPassword;

    // 修改密码的临时授权码
    @NameInMap("state")
    @Validation(required = true)
    public String state;

    public static DefaultSetPasswordRequest build(java.util.Map<String, ?> map) throws Exception {
        DefaultSetPasswordRequest self = new DefaultSetPasswordRequest();
        return TeaModel.build(map, self);
    }

    public DefaultSetPasswordRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public DefaultSetPasswordRequest setAppId(String appId) {
        this.appId = appId;
        return this;
    }
    public String getAppId() {
        return this.appId;
    }

    public DefaultSetPasswordRequest setEncryptedKey(String encryptedKey) {
        this.encryptedKey = encryptedKey;
        return this;
    }
    public String getEncryptedKey() {
        return this.encryptedKey;
    }

    public DefaultSetPasswordRequest setNewPassword(String newPassword) {
        this.newPassword = newPassword;
        return this;
    }
    public String getNewPassword() {
        return this.newPassword;
    }

    public DefaultSetPasswordRequest setState(String state) {
        this.state = state;
        return this;
    }
    public String getState() {
        return this.state;
    }

}
