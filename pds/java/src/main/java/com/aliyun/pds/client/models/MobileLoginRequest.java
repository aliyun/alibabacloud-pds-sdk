// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class MobileLoginRequest extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    // App ID, 当前访问的App
    @NameInMap("app_id")
    @Validation(required = true)
    public String appId;

    // 是否自动注册用户，使用密码登录此参数不生效
    @NameInMap("auto_register")
    public Boolean autoRegister;

    // 图片验证码ID, 密码登录需要此参数
    @NameInMap("captcha_id")
    public String captchaId;

    // 用户输入的验证码值, 密码登录需要此参数
    @NameInMap("captcha_text")
    public String captchaText;

    // AES-256对称加密密钥，通过App公钥加密后传输
    @NameInMap("encrypted_key")
    public String encryptedKey;

    // 环境参数
    @NameInMap("nvc_param")
    @Validation(required = true)
    public String nvcParam;

    // 登录密码, 传入此参数则忽略短信验证码，不传此参数则默认使用短信登录。
    @NameInMap("password")
    public String password;

    // 待查询的手机号
    @NameInMap("phone_number")
    @Validation(required = true)
    public String phoneNumber;

    // 国家编号，默认86，不需要填+号，直接填数字
    @NameInMap("phone_region")
    public String phoneRegion;

    // 短信验证码内容，使用密码登录此参数不生效
    @NameInMap("sms_code")
    public String smsCode;

    // 短信验证码ID，使用密码登录此参数不生效
    @NameInMap("sms_code_id")
    public String smsCodeId;

    public static MobileLoginRequest build(java.util.Map<String, ?> map) throws Exception {
        MobileLoginRequest self = new MobileLoginRequest();
        return TeaModel.build(map, self);
    }

    public MobileLoginRequest setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public MobileLoginRequest setAppId(String appId) {
        this.appId = appId;
        return this;
    }
    public String getAppId() {
        return this.appId;
    }

    public MobileLoginRequest setAutoRegister(Boolean autoRegister) {
        this.autoRegister = autoRegister;
        return this;
    }
    public Boolean getAutoRegister() {
        return this.autoRegister;
    }

    public MobileLoginRequest setCaptchaId(String captchaId) {
        this.captchaId = captchaId;
        return this;
    }
    public String getCaptchaId() {
        return this.captchaId;
    }

    public MobileLoginRequest setCaptchaText(String captchaText) {
        this.captchaText = captchaText;
        return this;
    }
    public String getCaptchaText() {
        return this.captchaText;
    }

    public MobileLoginRequest setEncryptedKey(String encryptedKey) {
        this.encryptedKey = encryptedKey;
        return this;
    }
    public String getEncryptedKey() {
        return this.encryptedKey;
    }

    public MobileLoginRequest setNvcParam(String nvcParam) {
        this.nvcParam = nvcParam;
        return this;
    }
    public String getNvcParam() {
        return this.nvcParam;
    }

    public MobileLoginRequest setPassword(String password) {
        this.password = password;
        return this;
    }
    public String getPassword() {
        return this.password;
    }

    public MobileLoginRequest setPhoneNumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
        return this;
    }
    public String getPhoneNumber() {
        return this.phoneNumber;
    }

    public MobileLoginRequest setPhoneRegion(String phoneRegion) {
        this.phoneRegion = phoneRegion;
        return this;
    }
    public String getPhoneRegion() {
        return this.phoneRegion;
    }

    public MobileLoginRequest setSmsCode(String smsCode) {
        this.smsCode = smsCode;
        return this;
    }
    public String getSmsCode() {
        return this.smsCode;
    }

    public MobileLoginRequest setSmsCodeId(String smsCodeId) {
        this.smsCodeId = smsCodeId;
        return this;
    }
    public String getSmsCodeId() {
        return this.smsCodeId;
    }

}
