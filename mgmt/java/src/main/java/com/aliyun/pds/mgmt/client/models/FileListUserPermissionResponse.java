// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 用户所有的文件共享/授权列表请求
 */
public class FileListUserPermissionResponse extends TeaModel {
    @NameInMap("items")
    public java.util.List<BaseFileUserPermissionResponse> items;

    public static FileListUserPermissionResponse build(java.util.Map<String, ?> map) throws Exception {
        FileListUserPermissionResponse self = new FileListUserPermissionResponse();
        return TeaModel.build(map, self);
    }

    public FileListUserPermissionResponse setItems(java.util.List<BaseFileUserPermissionResponse> items) {
        this.items = items;
        return this;
    }
    public java.util.List<BaseFileUserPermissionResponse> getItems() {
        return this.items;
    }

}
