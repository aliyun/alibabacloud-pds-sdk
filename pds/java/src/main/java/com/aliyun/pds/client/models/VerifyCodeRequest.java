// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class VerifyCodeRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    /**
     * <p>App ID, 当前访问的App</p>
     */
    @NameInMap("app_id")
    @Validation(required = true)
    public String appId;

    /**
     * <p>手机号</p>
     */
    @NameInMap("phone_number")
    @Validation(required = true)
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

    /**
     * <p>需要被校验内容的类型</p>
     */
    @NameInMap("verify_type")
    public String verifyType;

    public static VerifyCodeRequest build(java.util.Map<String, ?> map) throws Exception {
        VerifyCodeRequest self = new VerifyCodeRequest();
        return TeaModel.build(map, self);
    }

    public VerifyCodeRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public VerifyCodeRequest setAppId(String appId) {
        this.appId = appId;
        return this;
    }
    public String getAppId() {
        return this.appId;
    }

    public VerifyCodeRequest setPhoneNumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
        return this;
    }
    public String getPhoneNumber() {
        return this.phoneNumber;
    }

    public VerifyCodeRequest setPhoneRegion(String phoneRegion) {
        this.phoneRegion = phoneRegion;
        return this;
    }
    public String getPhoneRegion() {
        return this.phoneRegion;
    }

    public VerifyCodeRequest setSmsCode(String smsCode) {
        this.smsCode = smsCode;
        return this;
    }
    public String getSmsCode() {
        return this.smsCode;
    }

    public VerifyCodeRequest setSmsCodeId(String smsCodeId) {
        this.smsCodeId = smsCodeId;
        return this;
    }
    public String getSmsCodeId() {
        return this.smsCodeId;
    }

    public VerifyCodeRequest setVerifyType(String verifyType) {
        this.verifyType = verifyType;
        return this;
    }
    public String getVerifyType() {
        return this.verifyType;
    }

}
