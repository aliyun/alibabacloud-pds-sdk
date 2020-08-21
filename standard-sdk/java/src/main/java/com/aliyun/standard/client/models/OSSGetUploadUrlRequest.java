// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.standard.client.models;

import com.aliyun.tea.*;

/**
 * 获取文件上传URL
 */
public class OSSGetUploadUrlRequest extends TeaModel {
    // content_md5
    @NameInMap("content_md5")
    @Validation(maxLength = 32)
    public String contentMd5;

    // drive_id
    @NameInMap("drive_id")
    @Validation(pattern = "[0-9]+")
    public String driveId;

    // file_path
    @NameInMap("file_path")
    @Validation(required = true)
    public String filePath;

    // upload_part_list
    @NameInMap("part_info_list")
    public java.util.List<UploadPartInfo> partInfoList;

    // share_id
    @NameInMap("share_id")
    @Validation(pattern = "[0-9a-zA-Z-]+")
    public String shareId;

    // upload_id
    @NameInMap("upload_id")
    @Validation(required = true)
    public String uploadId;

    public static OSSGetUploadUrlRequest build(java.util.Map<String, ?> map) throws Exception {
        OSSGetUploadUrlRequest self = new OSSGetUploadUrlRequest();
        return TeaModel.build(map, self);
    }

    public OSSGetUploadUrlRequest setContentMd5(String contentMd5) {
        this.contentMd5 = contentMd5;
        return this;
    }
    public String getContentMd5() {
        return this.contentMd5;
    }

    public OSSGetUploadUrlRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public OSSGetUploadUrlRequest setFilePath(String filePath) {
        this.filePath = filePath;
        return this;
    }
    public String getFilePath() {
        return this.filePath;
    }

    public OSSGetUploadUrlRequest setPartInfoList(java.util.List<UploadPartInfo> partInfoList) {
        this.partInfoList = partInfoList;
        return this;
    }
    public java.util.List<UploadPartInfo> getPartInfoList() {
        return this.partInfoList;
    }

    public OSSGetUploadUrlRequest setShareId(String shareId) {
        this.shareId = shareId;
        return this;
    }
    public String getShareId() {
        return this.shareId;
    }

    public OSSGetUploadUrlRequest setUploadId(String uploadId) {
        this.uploadId = uploadId;
        return this;
    }
    public String getUploadId() {
        return this.uploadId;
    }

}
