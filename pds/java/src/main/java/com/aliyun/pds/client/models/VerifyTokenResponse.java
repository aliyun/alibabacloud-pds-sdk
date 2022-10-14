// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class VerifyTokenResponse extends TeaModel {
    // 实人认证的Token
    @NameInMap("token")
    @Validation(required = true)
    public String token;

    // 实人认证token有效秒数，如1800
    @NameInMap("ttl")
    @Validation(required = true)
    public Long ttl;

    // 实人认证的URL，包含Token
    @NameInMap("url")
    @Validation(required = true)
    public String url;

    public static VerifyTokenResponse build(java.util.Map<String, ?> map) throws Exception {
        VerifyTokenResponse self = new VerifyTokenResponse();
        return TeaModel.build(map, self);
    }

    public VerifyTokenResponse setToken(String token) {
        this.token = token;
        return this;
    }
    public String getToken() {
        return this.token;
    }

    public VerifyTokenResponse setTtl(Long ttl) {
        this.ttl = ttl;
        return this;
    }
    public Long getTtl() {
        return this.ttl;
    }

    public VerifyTokenResponse setUrl(String url) {
        this.url = url;
        return this;
    }
    public String getUrl() {
        return this.url;
    }

}
