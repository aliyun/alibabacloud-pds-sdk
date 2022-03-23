// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class GetAppPublicKeyRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    // App ID
    @NameInMap("app_id")
    @Validation(required = true)
    public String appId;

    public static GetAppPublicKeyRequest build(java.util.Map<String, ?> map) throws Exception {
        GetAppPublicKeyRequest self = new GetAppPublicKeyRequest();
        return TeaModel.build(map, self);
    }

    public GetAppPublicKeyRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public GetAppPublicKeyRequest setAppId(String appId) {
        this.appId = appId;
        return this;
    }
    public String getAppId() {
        return this.appId;
    }

}
