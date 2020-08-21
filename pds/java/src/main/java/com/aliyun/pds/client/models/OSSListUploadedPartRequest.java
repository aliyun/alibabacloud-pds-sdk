// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 列举uploadID对应的已上传分片
 */
public class OSSListUploadedPartRequest extends TeaModel {
    // drive_id
    @NameInMap("drive_id")
    @Validation(pattern = "[0-9]+")
    public String driveId;

    // file_path
    @NameInMap("file_path")
    @Validation(required = true)
    public String filePath;

    // limit
    @NameInMap("limit")
    @Validation(pattern = "[0-9]+")
    public Long limit;

    // part_number_marker
    @NameInMap("part_number_marker")
    @Validation(pattern = "[0-9]+")
    public Long partNumberMarker;

    // share_id
    @NameInMap("share_id")
    @Validation(pattern = "[0-9a-zA-Z-]+")
    public String shareId;

    // upload_id
    @NameInMap("upload_id")
    public String uploadId;

    public static OSSListUploadedPartRequest build(java.util.Map<String, ?> map) throws Exception {
        OSSListUploadedPartRequest self = new OSSListUploadedPartRequest();
        return TeaModel.build(map, self);
    }

    public OSSListUploadedPartRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public OSSListUploadedPartRequest setFilePath(String filePath) {
        this.filePath = filePath;
        return this;
    }
    public String getFilePath() {
        return this.filePath;
    }

    public OSSListUploadedPartRequest setLimit(Long limit) {
        this.limit = limit;
        return this;
    }
    public Long getLimit() {
        return this.limit;
    }

    public OSSListUploadedPartRequest setPartNumberMarker(Long partNumberMarker) {
        this.partNumberMarker = partNumberMarker;
        return this;
    }
    public Long getPartNumberMarker() {
        return this.partNumberMarker;
    }

    public OSSListUploadedPartRequest setShareId(String shareId) {
        this.shareId = shareId;
        return this;
    }
    public String getShareId() {
        return this.shareId;
    }

    public OSSListUploadedPartRequest setUploadId(String uploadId) {
        this.uploadId = uploadId;
        return this;
    }
    public String getUploadId() {
        return this.uploadId;
    }

}
