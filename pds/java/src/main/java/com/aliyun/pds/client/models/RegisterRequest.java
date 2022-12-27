// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class RegisterRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    /**
     * <p>App ID, 当前访问的App</p>
     */
    @NameInMap("app_id")
    @Validation(required = true)
    public String appId;

    /**
     * <p>邮箱</p>
     */
    @NameInMap("email")
    public String email;

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
     * <p>短信验证码内容</p>
     */
    @NameInMap("sms_code")
    @Validation(required = true)
    public String smsCode;

    /**
     * <p>短信验证码ID</p>
     */
    @NameInMap("sms_code_id")
    @Validation(required = true)
    public String smsCodeId;

    public static RegisterRequest build(java.util.Map<String, ?> map) throws Exception {
        RegisterRequest self = new RegisterRequest();
        return TeaModel.build(map, self);
    }

    public RegisterRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public RegisterRequest setAppId(String appId) {
        this.appId = appId;
        return this;
    }
    public String getAppId() {
        return this.appId;
    }

    public RegisterRequest setEmail(String email) {
        this.email = email;
        return this;
    }
    public String getEmail() {
        return this.email;
    }

    public RegisterRequest setNvcParam(String nvcParam) {
        this.nvcParam = nvcParam;
        return this;
    }
    public String getNvcParam() {
        return this.nvcParam;
    }

    public RegisterRequest setPhoneNumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
        return this;
    }
    public String getPhoneNumber() {
        return this.phoneNumber;
    }

    public RegisterRequest setPhoneRegion(String phoneRegion) {
        this.phoneRegion = phoneRegion;
        return this;
    }
    public String getPhoneRegion() {
        return this.phoneRegion;
    }

    public RegisterRequest setSmsCode(String smsCode) {
        this.smsCode = smsCode;
        return this;
    }
    public String getSmsCode() {
        return this.smsCode;
    }

    public RegisterRequest setSmsCodeId(String smsCodeId) {
        this.smsCodeId = smsCodeId;
        return this;
    }
    public String getSmsCodeId() {
        return this.smsCodeId;
    }

}
