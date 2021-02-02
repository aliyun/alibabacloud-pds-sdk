// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.hostingmode.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class RPVerifyTokenResponse extends TeaModel {
    // 是否需要实人认证，如果用户已通过认证，或者未开启实人认证，返回false
    @NameInMap("need_rp_verify")
    @Validation(required = true)
    public Boolean needRpVerify;

    @NameInMap("verify_token")
    @Validation(required = true)
    public VerifyTokenResponse verifyToken;

    public static RPVerifyTokenResponse build(java.util.Map<String, ?> map) throws Exception {
        RPVerifyTokenResponse self = new RPVerifyTokenResponse();
        return TeaModel.build(map, self);
    }

    public RPVerifyTokenResponse setNeedRpVerify(Boolean needRpVerify) {
        this.needRpVerify = needRpVerify;
        return this;
    }
    public Boolean getNeedRpVerify() {
        return this.needRpVerify;
    }

    public RPVerifyTokenResponse setVerifyToken(VerifyTokenResponse verifyToken) {
        this.verifyToken = verifyToken;
        return this;
    }
    public VerifyTokenResponse getVerifyToken() {
        return this.verifyToken;
    }

}
