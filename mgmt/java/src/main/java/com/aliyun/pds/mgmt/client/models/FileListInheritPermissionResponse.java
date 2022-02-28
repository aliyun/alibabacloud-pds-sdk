// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 文件继承共享/授权的列表
 */
public class FileListInheritPermissionResponse extends TeaModel {
    @NameInMap("items")
    public java.util.List<BaseFileListInheritPermissionResponse> items;

    public static FileListInheritPermissionResponse build(java.util.Map<String, ?> map) throws Exception {
        FileListInheritPermissionResponse self = new FileListInheritPermissionResponse();
        return TeaModel.build(map, self);
    }

    public FileListInheritPermissionResponse setItems(java.util.List<BaseFileListInheritPermissionResponse> items) {
        this.items = items;
        return this;
    }
    public java.util.List<BaseFileListInheritPermissionResponse> getItems() {
        return this.items;
    }

}
