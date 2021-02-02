// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.hostingmode.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class MobileSendSmsCodeResponse extends TeaModel {
    // 短信验证码ID
    @NameInMap("sms_code_id")
    @Validation(required = true)
    public String smsCodeId;

    public static MobileSendSmsCodeResponse build(java.util.Map<String, ?> map) throws Exception {
        MobileSendSmsCodeResponse self = new MobileSendSmsCodeResponse();
        return TeaModel.build(map, self);
    }

    public MobileSendSmsCodeResponse setSmsCodeId(String smsCodeId) {
        this.smsCodeId = smsCodeId;
        return this;
    }
    public String getSmsCodeId() {
        return this.smsCodeId;
    }

}
