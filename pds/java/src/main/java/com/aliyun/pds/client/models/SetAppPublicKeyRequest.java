// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class SetAppPublicKeyRequest extends TeaModel {
    // App ID
    @NameInMap("app_id")
    @Validation(required = true)
    public String appId;

    // RSA加密算法的公钥, PEM格式
    @NameInMap("public_key")
    @Validation(required = true)
    public String publicKey;

    public static SetAppPublicKeyRequest build(java.util.Map<String, ?> map) throws Exception {
        SetAppPublicKeyRequest self = new SetAppPublicKeyRequest();
        return TeaModel.build(map, self);
    }

    public SetAppPublicKeyRequest setAppId(String appId) {
        this.appId = appId;
        return this;
    }
    public String getAppId() {
        return this.appId;
    }

    public SetAppPublicKeyRequest setPublicKey(String publicKey) {
        this.publicKey = publicKey;
        return this;
    }
    public String getPublicKey() {
        return this.publicKey;
    }

}
