// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class SendSmsCodeResponse extends TeaModel {
    /**
     * <p>验证码ID</p>
     */
    @NameInMap("sms_code_id")
    @Validation(required = true)
    public String smsCodeId;

    public static SendSmsCodeResponse build(java.util.Map<String, ?> map) throws Exception {
        SendSmsCodeResponse self = new SendSmsCodeResponse();
        return TeaModel.build(map, self);
    }

    public SendSmsCodeResponse setSmsCodeId(String smsCodeId) {
        this.smsCodeId = smsCodeId;
        return this;
    }
    public String getSmsCodeId() {
        return this.smsCodeId;
    }

}
