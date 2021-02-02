// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.hostingmode.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class VerifyCodeRequest extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    // App ID, 当前访问的App
    @NameInMap("app_id")
    @Validation(required = true)
    public String appId;

    // 手机号
    @NameInMap("phone_number")
    @Validation(required = true)
    public String phoneNumber;

    // 国家编号，默认86，不需要填+号，直接填数字
    @NameInMap("phone_region")
    public String phoneRegion;

    // 短信验证码内容
    @NameInMap("sms_code")
    @Validation(required = true)
    public String smsCode;

    // 短信验证码ID
    @NameInMap("sms_code_id")
    @Validation(required = true)
    public String smsCodeId;

    // 需要被校验内容的类型
    @NameInMap("verify_type")
    public String verifyType;

    public static VerifyCodeRequest build(java.util.Map<String, ?> map) throws Exception {
        VerifyCodeRequest self = new VerifyCodeRequest();
        return TeaModel.build(map, self);
    }

    public VerifyCodeRequest setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
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
