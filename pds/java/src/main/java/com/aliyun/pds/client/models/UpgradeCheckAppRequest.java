// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class UpgradeCheckAppRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    /**
     * <p>app_id</p>
     */
    @NameInMap("app_id")
    public String appId;

    /**
     * <p>arch</p>
     */
    @NameInMap("arch")
    public String arch;

    /**
     * <p>version</p>
     */
    @NameInMap("version")
    public String version;

    public static UpgradeCheckAppRequest build(java.util.Map<String, ?> map) throws Exception {
        UpgradeCheckAppRequest self = new UpgradeCheckAppRequest();
        return TeaModel.build(map, self);
    }

    public UpgradeCheckAppRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public UpgradeCheckAppRequest setAppId(String appId) {
        this.appId = appId;
        return this;
    }
    public String getAppId() {
        return this.appId;
    }

    public UpgradeCheckAppRequest setArch(String arch) {
        this.arch = arch;
        return this;
    }
    public String getArch() {
        return this.arch;
    }

    public UpgradeCheckAppRequest setVersion(String version) {
        this.version = version;
        return this;
    }
    public String getVersion() {
        return this.version;
    }

}
