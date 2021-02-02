// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.hostingmode.client.models;

import com.aliyun.tea.*;

/**
 * 获取文件上传URL
 */
public class GetUploadUrlRequest extends TeaModel {
    // content_md5
    @NameInMap("content_md5")
    @Validation(maxLength = 32)
    public String contentMd5;

    // drive_id
    @NameInMap("drive_id")
    @Validation(pattern = "[0-9]+")
    public String driveId;

    // file_id
    @NameInMap("file_id")
    @Validation(required = true, pattern = "[a-z0-9]{1,50}", maxLength = 50, minLength = 40)
    public String fileId;

    // upload_part_list
    @NameInMap("part_info_list")
    public java.util.List<UploadPartInfo> partInfoList;

    @NameInMap("share_id")
    public String shareId;

    // upload_id
    @NameInMap("upload_id")
    @Validation(required = true)
    public String uploadId;

    public static GetUploadUrlRequest build(java.util.Map<String, ?> map) throws Exception {
        GetUploadUrlRequest self = new GetUploadUrlRequest();
        return TeaModel.build(map, self);
    }

    public GetUploadUrlRequest setContentMd5(String contentMd5) {
        this.contentMd5 = contentMd5;
        return this;
    }
    public String getContentMd5() {
        return this.contentMd5;
    }

    public GetUploadUrlRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public GetUploadUrlRequest setFileId(String fileId) {
        this.fileId = fileId;
        return this;
    }
    public String getFileId() {
        return this.fileId;
    }

    public GetUploadUrlRequest setPartInfoList(java.util.List<UploadPartInfo> partInfoList) {
        this.partInfoList = partInfoList;
        return this;
    }
    public java.util.List<UploadPartInfo> getPartInfoList() {
        return this.partInfoList;
    }

    public GetUploadUrlRequest setShareId(String shareId) {
        this.shareId = shareId;
        return this;
    }
    public String getShareId() {
        return this.shareId;
    }

    public GetUploadUrlRequest setUploadId(String uploadId) {
        this.uploadId = uploadId;
        return this;
    }
    public String getUploadId() {
        return this.uploadId;
    }

}
