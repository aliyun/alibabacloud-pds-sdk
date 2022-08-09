// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 *
 */
public class GetAppPublicKeyResponse extends TeaModel {
    // App ID
    @NameInMap("app_id")
    @Validation(required = true)
    public String appId;

    // RSA加密算法的公钥, PEM格式
    @NameInMap("public_key")
    @Validation(required = true)
    public String publicKey;

    public static GetAppPublicKeyResponse build(java.util.Map<String, ?> map) throws Exception {
        GetAppPublicKeyResponse self = new GetAppPublicKeyResponse();
        return TeaModel.build(map, self);
    }

    public GetAppPublicKeyResponse setAppId(String appId) {
        this.appId = appId;
        return this;
    }
    public String getAppId() {
        return this.appId;
    }

    public GetAppPublicKeyResponse setPublicKey(String publicKey) {
        this.publicKey = publicKey;
        return this;
    }
    public String getPublicKey() {
        return this.publicKey;
    }

}
