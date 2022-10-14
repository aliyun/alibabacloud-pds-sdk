// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 *
 */
public class RoleConfig extends TeaModel {
    @NameInMap("default_group_drive_role")
    public String defaultGroupDriveRole;

    @NameInMap("disabled_admin_file_permission")
    public Boolean disabledAdminFilePermission;

    @NameInMap("enabled")
    public Boolean enabled;

    @NameInMap("enabled_admin_delete_personal_file_permission")
    public Boolean enabledAdminDeletePersonalFilePermission;

    @NameInMap("enabled_admin_personal_file_permission")
    public Boolean enabledAdminPersonalFilePermission;

    public static RoleConfig build(java.util.Map<String, ?> map) throws Exception {
        RoleConfig self = new RoleConfig();
        return TeaModel.build(map, self);
    }

    public RoleConfig setDefaultGroupDriveRole(String defaultGroupDriveRole) {
        this.defaultGroupDriveRole = defaultGroupDriveRole;
        return this;
    }
    public String getDefaultGroupDriveRole() {
        return this.defaultGroupDriveRole;
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

    public RoleConfig setEnabledAdminDeletePersonalFilePermission(Boolean enabledAdminDeletePersonalFilePermission) {
        this.enabledAdminDeletePersonalFilePermission = enabledAdminDeletePersonalFilePermission;
        return this;
    }
    public Boolean getEnabledAdminDeletePersonalFilePermission() {
        return this.enabledAdminDeletePersonalFilePermission;
    }

    public RoleConfig setEnabledAdminPersonalFilePermission(Boolean enabledAdminPersonalFilePermission) {
        this.enabledAdminPersonalFilePermission = enabledAdminPersonalFilePermission;
        return this;
    }
    public Boolean getEnabledAdminPersonalFilePermission() {
        return this.enabledAdminPersonalFilePermission;
    }

}
