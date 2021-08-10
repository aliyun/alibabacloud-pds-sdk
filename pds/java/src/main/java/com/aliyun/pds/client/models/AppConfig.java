// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class AppConfig extends TeaModel {
    @NameInMap("web_version")
    public String webVersion;

    public static AppConfig build(java.util.Map<String, ?> map) throws Exception {
        AppConfig self = new AppConfig();
        return TeaModel.build(map, self);
    }

    public AppConfig setWebVersion(String webVersion) {
        this.webVersion = webVersion;
        return this;
    }
    public String getWebVersion() {
        return this.webVersion;
    }

}
