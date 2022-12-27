// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class GetAppPublicKeyRequest extends TeaModel {
    /**
     * <p>App ID</p>
     */
    @NameInMap("app_id")
    @Validation(required = true)
    public String appId;

    public static GetAppPublicKeyRequest build(java.util.Map<String, ?> map) throws Exception {
        GetAppPublicKeyRequest self = new GetAppPublicKeyRequest();
        return TeaModel.build(map, self);
    }

    public GetAppPublicKeyRequest setAppId(String appId) {
        this.appId = appId;
        return this;
    }
    public String getAppId() {
        return this.appId;
    }

}
