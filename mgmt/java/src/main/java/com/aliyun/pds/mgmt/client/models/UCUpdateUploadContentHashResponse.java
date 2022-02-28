// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * UCUpdateUploadContentHashResponse
 */
public class UCUpdateUploadContentHashResponse extends TeaModel {
    @NameInMap("content_hash")
    public String contentHash;

    @NameInMap("content_hash_name")
    public String contentHashName;

    @NameInMap("content_md5")
    public String contentMd5;

    @NameInMap("drive_id")
    public String driveId;

    @NameInMap("file_id")
    public String fileId;

    @NameInMap("is_rapid_upload")
    public Boolean isRapidUpload;

    @NameInMap("size")
    public Long size;

    @NameInMap("update_time")
    public String updateTime;

    @NameInMap("upload_id")
    public String uploadId;

    public static UCUpdateUploadContentHashResponse build(java.util.Map<String, ?> map) throws Exception {
        UCUpdateUploadContentHashResponse self = new UCUpdateUploadContentHashResponse();
        return TeaModel.build(map, self);
    }

    public UCUpdateUploadContentHashResponse setContentHash(String contentHash) {
        this.contentHash = contentHash;
        return this;
    }
    public String getContentHash() {
        return this.contentHash;
    }

    public UCUpdateUploadContentHashResponse setContentHashName(String contentHashName) {
        this.contentHashName = contentHashName;
        return this;
    }
    public String getContentHashName() {
        return this.contentHashName;
    }

    public UCUpdateUploadContentHashResponse setContentMd5(String contentMd5) {
        this.contentMd5 = contentMd5;
        return this;
    }
    public String getContentMd5() {
        return this.contentMd5;
    }

    public UCUpdateUploadContentHashResponse setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public UCUpdateUploadContentHashResponse setFileId(String fileId) {
        this.fileId = fileId;
        return this;
    }
    public String getFileId() {
        return this.fileId;
    }

    public UCUpdateUploadContentHashResponse setIsRapidUpload(Boolean isRapidUpload) {
        this.isRapidUpload = isRapidUpload;
        return this;
    }
    public Boolean getIsRapidUpload() {
        return this.isRapidUpload;
    }

    public UCUpdateUploadContentHashResponse setSize(Long size) {
        this.size = size;
        return this;
    }
    public Long getSize() {
        return this.size;
    }

    public UCUpdateUploadContentHashResponse setUpdateTime(String updateTime) {
        this.updateTime = updateTime;
        return this;
    }
    public String getUpdateTime() {
        return this.updateTime;
    }

    public UCUpdateUploadContentHashResponse setUploadId(String uploadId) {
        this.uploadId = uploadId;
        return this;
    }
    public String getUploadId() {
        return this.uploadId;
    }

}
