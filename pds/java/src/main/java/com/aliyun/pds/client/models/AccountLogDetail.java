// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class AccountLogDetail extends TeaModel {
    /**
     * <p>authentication_type</p>
     */
    @NameInMap("authentication_type")
    public String authenticationType;

    /**
     * <p>login_type</p>
     */
    @NameInMap("login_type")
    public String loginType;

    public static AccountLogDetail build(java.util.Map<String, ?> map) throws Exception {
        AccountLogDetail self = new AccountLogDetail();
        return TeaModel.build(map, self);
    }

    public AccountLogDetail setAuthenticationType(String authenticationType) {
        this.authenticationType = authenticationType;
        return this;
    }
    public String getAuthenticationType() {
        return this.authenticationType;
    }

    public AccountLogDetail setLoginType(String loginType) {
        this.loginType = loginType;
        return this;
    }
    public String getLoginType() {
        return this.loginType;
    }

}
