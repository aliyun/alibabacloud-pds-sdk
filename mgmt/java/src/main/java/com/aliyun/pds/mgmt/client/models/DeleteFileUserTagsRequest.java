// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 删除文件 user_tags 字段
 */
public class DeleteFileUserTagsRequest extends TeaModel {
    // drive_id
    @NameInMap("drive_id")
    @Validation(required = true, pattern = "[0-9]+")
    public String driveId;

    // file_id
    @NameInMap("file_id")
    @Validation(required = true, pattern = "[a-z0-9.-_]{1,50}", maxLength = 50, minLength = 40)
    public String fileId;

    // key_list
    @NameInMap("key_list")
    public java.util.List<String> keyList;

    public static DeleteFileUserTagsRequest build(java.util.Map<String, ?> map) throws Exception {
        DeleteFileUserTagsRequest self = new DeleteFileUserTagsRequest();
        return TeaModel.build(map, self);
    }

    public DeleteFileUserTagsRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public DeleteFileUserTagsRequest setFileId(String fileId) {
        this.fileId = fileId;
        return this;
    }
    public String getFileId() {
        return this.fileId;
    }

    public DeleteFileUserTagsRequest setKeyList(java.util.List<String> keyList) {
        this.keyList = keyList;
        return this;
    }
    public java.util.List<String> getKeyList() {
        return this.keyList;
    }

}
