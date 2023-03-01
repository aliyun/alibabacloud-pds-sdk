// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class FileCustomRoleInfoLogDetail extends TeaModel {
    @NameInMap("action_list")
    public java.util.List<String> actionList;

    @NameInMap("description")
    public String description;

    @NameInMap("role_name")
    public String roleName;

    @NameInMap("status")
    public String status;

    public static FileCustomRoleInfoLogDetail build(java.util.Map<String, ?> map) throws Exception {
        FileCustomRoleInfoLogDetail self = new FileCustomRoleInfoLogDetail();
        return TeaModel.build(map, self);
    }

    public FileCustomRoleInfoLogDetail setActionList(java.util.List<String> actionList) {
        this.actionList = actionList;
        return this;
    }
    public java.util.List<String> getActionList() {
        return this.actionList;
    }

    public FileCustomRoleInfoLogDetail setDescription(String description) {
        this.description = description;
        return this;
    }
    public String getDescription() {
        return this.description;
    }

    public FileCustomRoleInfoLogDetail setRoleName(String roleName) {
        this.roleName = roleName;
        return this;
    }
    public String getRoleName() {
        return this.roleName;
    }

    public FileCustomRoleInfoLogDetail setStatus(String status) {
        this.status = status;
        return this;
    }
    public String getStatus() {
        return this.status;
    }

}
