// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 获取文件上传URL
 */
public class BaseGetUploadUrlRequest extends TeaModel {
    // content_md5
    @NameInMap("content_md5")
    @Validation(maxLength = 32)
    public String contentMd5;

    // drive_id
    @NameInMap("drive_id")
    @Validation(pattern = "[0-9]+")
    public String driveId;

    // upload_part_list
    @NameInMap("part_info_list")
    public java.util.List<UploadPartInfo> partInfoList;

    @NameInMap("share_id")
    public String shareId;

    // upload_id
    @NameInMap("upload_id")
    @Validation(required = true)
    public String uploadId;

    public static BaseGetUploadUrlRequest build(java.util.Map<String, ?> map) throws Exception {
        BaseGetUploadUrlRequest self = new BaseGetUploadUrlRequest();
        return TeaModel.build(map, self);
    }

    public BaseGetUploadUrlRequest setContentMd5(String contentMd5) {
        this.contentMd5 = contentMd5;
        return this;
    }
    public String getContentMd5() {
        return this.contentMd5;
    }

    public BaseGetUploadUrlRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public BaseGetUploadUrlRequest setPartInfoList(java.util.List<UploadPartInfo> partInfoList) {
        this.partInfoList = partInfoList;
        return this;
    }
    public java.util.List<UploadPartInfo> getPartInfoList() {
        return this.partInfoList;
    }

    public BaseGetUploadUrlRequest setShareId(String shareId) {
        this.shareId = shareId;
        return this;
    }
    public String getShareId() {
        return this.shareId;
    }

    public BaseGetUploadUrlRequest setUploadId(String uploadId) {
        this.uploadId = uploadId;
        return this;
    }
    public String getUploadId() {
        return this.uploadId;
    }

}
