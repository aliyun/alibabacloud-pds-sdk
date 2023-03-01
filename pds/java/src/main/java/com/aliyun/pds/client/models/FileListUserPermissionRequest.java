// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 查询用户所有的文件共享/授权列表请求
 */
public class FileListUserPermissionRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    @NameInMap("subdomain_id")
    public String subdomainId;

    /**
     * <p>选择查看自己的或团队的或所有的，默认自己的</p>
     */
    @NameInMap("type")
    public String type;

    /**
     * <p>需要查询的用户ID</p>
     */
    @NameInMap("user_id")
    @Validation(required = true)
    public String userId;

    public static FileListUserPermissionRequest build(java.util.Map<String, ?> map) throws Exception {
        FileListUserPermissionRequest self = new FileListUserPermissionRequest();
        return TeaModel.build(map, self);
    }

    public FileListUserPermissionRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
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
