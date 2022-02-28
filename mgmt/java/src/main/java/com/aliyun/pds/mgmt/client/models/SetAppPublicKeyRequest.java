// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class SetAppPublicKeyRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

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

    public SetAppPublicKeyRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
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
