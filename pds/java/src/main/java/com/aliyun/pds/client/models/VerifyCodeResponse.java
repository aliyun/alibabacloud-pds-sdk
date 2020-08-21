// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class VerifyCodeResponse extends TeaModel {
    // 修改密码的临时授权码
    @NameInMap("state")
    @Validation(required = true)
    public String state;

    public static VerifyCodeResponse build(java.util.Map<String, ?> map) throws Exception {
        VerifyCodeResponse self = new VerifyCodeResponse();
        return TeaModel.build(map, self);
    }

    public VerifyCodeResponse setState(String state) {
        this.state = state;
        return this;
    }
    public String getState() {
        return this.state;
    }

}
