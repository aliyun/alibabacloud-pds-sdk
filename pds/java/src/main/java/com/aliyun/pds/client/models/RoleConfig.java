// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class RoleConfig extends TeaModel {
    @NameInMap("disabled_admin_file_permission")
    public Boolean disabledAdminFilePermission;

    @NameInMap("enabled")
    public Boolean enabled;

    @NameInMap("enabled_admin_personal_file_permission")
    public Boolean enabledAdminPersonalFilePermission;

    public static RoleConfig build(java.util.Map<String, ?> map) throws Exception {
        RoleConfig self = new RoleConfig();
        return TeaModel.build(map, self);
    }

    public RoleConfig setDisabledAdminFilePermission(Boolean disabledAdminFilePermission) {
        this.disabledAdminFilePermission = disabledAdminFilePermission;
        return this;
    }
    public Boolean getDisabledAdminFilePermission() {
        return this.disabledAdminFilePermission;
    }

    public RoleConfig setEnabled(Boolean enabled) {
        this.enabled = enabled;
        return this;
    }
    public Boolean getEnabled() {
        return this.enabled;
    }

    public RoleConfig setEnabledAdminPersonalFilePermission(Boolean enabledAdminPersonalFilePermission) {
        this.enabledAdminPersonalFilePermission = enabledAdminPersonalFilePermission;
        return this;
    }
    public Boolean getEnabledAdminPersonalFilePermission() {
        return this.enabledAdminPersonalFilePermission;
    }

}
