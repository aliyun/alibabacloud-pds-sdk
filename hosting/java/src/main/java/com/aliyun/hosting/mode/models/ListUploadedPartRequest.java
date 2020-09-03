// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.hosting.mode.models;

import com.aliyun.tea.*;

/**
 * 列举uploadID对应的已上传分片
 */
public class ListUploadedPartRequest extends TeaModel {
    // drive_id
    @NameInMap("drive_id")
    @Validation(required = true, pattern = "[0-9]+")
    public String driveId;

    // file_id
    @NameInMap("file_id")
    @Validation(required = true, pattern = "[a-z0-9.-_]{1,50}", maxLength = 50, minLength = 40)
    public String fileId;

    // limit
    @NameInMap("limit")
    @Validation(pattern = "[0-9]+")
    public Long limit;

    // part_number_marker
    @NameInMap("part_number_marker")
    @Validation(pattern = "[0-9]+")
    public Long partNumberMarker;

    // upload_id
    @NameInMap("upload_id")
    public String uploadId;

    public static ListUploadedPartRequest build(java.util.Map<String, ?> map) throws Exception {
        ListUploadedPartRequest self = new ListUploadedPartRequest();
        return TeaModel.build(map, self);
    }

    public ListUploadedPartRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public ListUploadedPartRequest setFileId(String fileId) {
        this.fileId = fileId;
        return this;
    }
    public String getFileId() {
        return this.fileId;
    }

    public ListUploadedPartRequest setLimit(Long limit) {
        this.limit = limit;
        return this;
    }
    public Long getLimit() {
        return this.limit;
    }

    public ListUploadedPartRequest setPartNumberMarker(Long partNumberMarker) {
        this.partNumberMarker = partNumberMarker;
        return this;
    }
    public Long getPartNumberMarker() {
        return this.partNumberMarker;
    }

    public ListUploadedPartRequest setUploadId(String uploadId) {
        this.uploadId = uploadId;
        return this;
    }
    public String getUploadId() {
        return this.uploadId;
    }

}
