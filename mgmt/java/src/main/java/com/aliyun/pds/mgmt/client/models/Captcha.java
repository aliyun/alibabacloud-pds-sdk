// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class Captcha extends TeaModel {
    /**
     * <p>图片验证码，base64格式</p>
     */
    @NameInMap("captcha")
    @Validation(required = true)
    public String captcha;

    /**
     * <p>图片格式</p>
     */
    @NameInMap("captcha_format")
    @Validation(required = true)
    public String captchaFormat;

    /**
     * <p>图片验证码ID</p>
     */
    @NameInMap("captcha_id")
    @Validation(required = true)
    public String captchaId;

    public static Captcha build(java.util.Map<String, ?> map) throws Exception {
        Captcha self = new Captcha();
        return TeaModel.build(map, self);
    }

    public Captcha setCaptcha(String captcha) {
        this.captcha = captcha;
        return this;
    }
    public String getCaptcha() {
        return this.captcha;
    }

    public Captcha setCaptchaFormat(String captchaFormat) {
        this.captchaFormat = captchaFormat;
        return this;
    }
    public String getCaptchaFormat() {
        return this.captchaFormat;
    }

    public Captcha setCaptchaId(String captchaId) {
        this.captchaId = captchaId;
        return this;
    }
    public String getCaptchaId() {
        return this.captchaId;
    }

}
