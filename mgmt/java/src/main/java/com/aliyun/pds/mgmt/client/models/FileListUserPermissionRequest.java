// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 查询用户所有的文件共享/授权列表请求
 */
public class FileListUserPermissionRequest extends TeaModel {
    @NameInMap("subdomain_id")
    public String subdomainId;

    // 选择查看自己的或团队的或所有的，默认自己的
    @NameInMap("type")
    public String type;

    // 需要查询的用户ID
    @NameInMap("user_id")
    @Validation(required = true)
    public String userId;

    public static FileListUserPermissionRequest build(java.util.Map<String, ?> map) throws Exception {
        FileListUserPermissionRequest self = new FileListUserPermissionRequest();
        return TeaModel.build(map, self);
    }

    public FileListUserPermissionRequest setSubdomainId(String subdomainId) {
        this.subdomainId = subdomainId;
        return this;
    }
    public String getSubdomainId() {
        return this.subdomainId;
    }

    public FileListUserPermissionRequest setType(String type) {
        this.type = type;
        return this;
    }
    public String getType() {
        return this.type;
    }

    public FileListUserPermissionRequest setUserId(String userId) {
        this.userId = userId;
        return this;
    }
    public String getUserId() {
        return this.userId;
    }

}
