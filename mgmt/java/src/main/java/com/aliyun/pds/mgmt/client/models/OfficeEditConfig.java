// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * OfficeEditConfig 文档编辑配置
 */
public class OfficeEditConfig extends TeaModel {
    @NameInMap("enabled")
    public Boolean enabled;

    @NameInMap("role")
    public String role;

    public static OfficeEditConfig build(java.util.Map<String, ?> map) throws Exception {
        OfficeEditConfig self = new OfficeEditConfig();
        return TeaModel.build(map, self);
    }

    public OfficeEditConfig setEnabled(Boolean enabled) {
        this.enabled = enabled;
        return this;
    }
    public Boolean getEnabled() {
        return this.enabled;
    }

    public OfficeEditConfig setRole(String role) {
        this.role = role;
        return this;
    }
    public String getRole() {
        return this.role;
    }

}
