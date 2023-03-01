// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class SendSmsCodeRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    /**
     * <p>App ID, 当前访问的App</p>
     */
    @NameInMap("app_id")
    @Validation(required = true)
    public String appId;

    /**
     * <p>图片验证码ID</p>
     */
    @NameInMap("captcha_id")
    public String captchaId;

    /**
     * <p>用户输入的验证码值</p>
     */
    @NameInMap("captcha_text")
    public String captchaText;

    /**
     * <p>邮箱</p>
     */
    @NameInMap("email")
    public String email;

    /**
     * <p>发短信的语言</p>
     */
    @NameInMap("language")
    public String language;

    /**
     * <p>环境参数</p>
     */
    @NameInMap("nvc_param")
    @Validation(required = true)
    public String nvcParam;

    /**
     * <p>待发送验证短信的手机号</p>
     */
    @NameInMap("phone_number")
    public String phoneNumber;

    /**
     * <p>国家编号，默认86，不需要填+号，直接填数字</p>
     */
    @NameInMap("phone_region")
    public String phoneRegion;

    /**
     * <p>验证码用途, 可下发: login、register、change_password</p>
     */
    @NameInMap("type")
    @Validation(required = true)
    public String type;

    public static SendSmsCodeRequest build(java.util.Map<String, ?> map) throws Exception {
        SendSmsCodeRequest self = new SendSmsCodeRequest();
        return TeaModel.build(map, self);
    }

    public SendSmsCodeRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public SendSmsCodeRequest setAppId(String appId) {
        this.appId = appId;
        return this;
    }
    public String getAppId() {
        return this.appId;
    }

    public SendSmsCodeRequest setCaptchaId(String captchaId) {
        this.captchaId = captchaId;
        return this;
    }
    public String getCaptchaId() {
        return this.captchaId;
    }

    public SendSmsCodeRequest setCaptchaText(String captchaText) {
        this.captchaText = captchaText;
        return this;
    }
    public String getCaptchaText() {
        return this.captchaText;
    }

    public SendSmsCodeRequest setEmail(String email) {
        this.email = email;
        return this;
    }
    public String getEmail() {
        return this.email;
    }

    public SendSmsCodeRequest setLanguage(String language) {
        this.language = language;
        return this;
    }
    public String getLanguage() {
        return this.language;
    }

    public SendSmsCodeRequest setNvcParam(String nvcParam) {
        this.nvcParam = nvcParam;
        return this;
    }
    public String getNvcParam() {
        return this.nvcParam;
    }

    public SendSmsCodeRequest setPhoneNumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
        return this;
    }
    public String getPhoneNumber() {
        return this.phoneNumber;
    }

    public SendSmsCodeRequest setPhoneRegion(String phoneRegion) {
        this.phoneRegion = phoneRegion;
        return this;
    }
    public String getPhoneRegion() {
        return this.phoneRegion;
    }

    public SendSmsCodeRequest setType(String type) {
        this.type = type;
        return this;
    }
    public String getType() {
        return this.type;
    }

}
