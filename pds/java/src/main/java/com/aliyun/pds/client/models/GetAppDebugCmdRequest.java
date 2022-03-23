// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class GetAppDebugCmdRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    // app_id
    @NameInMap("app_id")
    public String appId;

    public static GetAppDebugCmdRequest build(java.util.Map<String, ?> map) throws Exception {
        GetAppDebugCmdRequest self = new GetAppDebugCmdRequest();
        return TeaModel.build(map, self);
    }

    public GetAppDebugCmdRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public GetAppDebugCmdRequest setAppId(String appId) {
        this.appId = appId;
        return this;
    }
    public String getAppId() {
        return this.appId;
    }

}
