// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.hosting.mode.models;

import com.aliyun.tea.*;

/**
 * 批量删除文件请求
 */
public class DeleteFilesRequest extends TeaModel {
    // drive_id
    @NameInMap("drive_id")
    @Validation(pattern = "[0-9]+")
    public String driveId;

    // file_id_list
    @NameInMap("file_id_list")
    @Validation(required = true)
    public java.util.List<String> fileIdList;

    // share_id
    @NameInMap("share_id")
    public String shareId;

    public static DeleteFilesRequest build(java.util.Map<String, ?> map) throws Exception {
        DeleteFilesRequest self = new DeleteFilesRequest();
        return TeaModel.build(map, self);
    }

    public DeleteFilesRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public DeleteFilesRequest setFileIdList(java.util.List<String> fileIdList) {
        this.fileIdList = fileIdList;
        return this;
    }
    public java.util.List<String> getFileIdList() {
        return this.fileIdList;
    }

    public DeleteFilesRequest setShareId(String shareId) {
        this.shareId = shareId;
        return this;
    }
    public String getShareId() {
        return this.shareId;
    }

}
