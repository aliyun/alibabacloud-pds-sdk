// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class BaseFileListInheritPermissionResponse extends TeaModel {
    /**
     * <p>被授权的文件ID</p>
     */
    @NameInMap("file_id")
    @Validation(required = true)
    public String fileId;

    @NameInMap("member")
    public FilePermissionMember member;

    public static BaseFileListInheritPermissionResponse build(java.util.Map<String, ?> map) throws Exception {
        BaseFileListInheritPermissionResponse self = new BaseFileListInheritPermissionResponse();
        return TeaModel.build(map, self);
    }

    public BaseFileListInheritPermissionResponse setFileId(String fileId) {
        this.fileId = fileId;
        return this;
    }
    public String getFileId() {
        return this.fileId;
    }

    public BaseFileListInheritPermissionResponse setMember(FilePermissionMember member) {
        this.member = member;
        return this;
    }
    public FilePermissionMember getMember() {
        return this.member;
    }

}
