// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 获取签名 response
 */
public class ListUploadedPartResponse extends TeaModel {
    // file_id
    @NameInMap("file_id")
    @Validation(pattern = "[a-z0-9]{1,50}", maxLength = 50, minLength = 40)
    public String fileId;

    // next_part_number_marker
    @NameInMap("next_part_number_marker")
    public String nextPartNumberMarker;

    @NameInMap("parallel_upload")
    public Boolean parallelUpload;

    // upload_id
    @NameInMap("upload_id")
    public String uploadId;

    // uploaded_parts
    @NameInMap("uploaded_parts")
    public java.util.List<UploadPartInfo> uploadedParts;

    public static ListUploadedPartResponse build(java.util.Map<String, ?> map) throws Exception {
        ListUploadedPartResponse self = new ListUploadedPartResponse();
        return TeaModel.build(map, self);
    }

    public ListUploadedPartResponse setFileId(String fileId) {
        this.fileId = fileId;
        return this;
    }
    public String getFileId() {
        return this.fileId;
    }

    public ListUploadedPartResponse setNextPartNumberMarker(String nextPartNumberMarker) {
        this.nextPartNumberMarker = nextPartNumberMarker;
        return this;
    }
    public String getNextPartNumberMarker() {
        return this.nextPartNumberMarker;
    }

    public ListUploadedPartResponse setParallelUpload(Boolean parallelUpload) {
        this.parallelUpload = parallelUpload;
        return this;
    }
    public Boolean getParallelUpload() {
        return this.parallelUpload;
    }

    public ListUploadedPartResponse setUploadId(String uploadId) {
        this.uploadId = uploadId;
        return this;
    }
    public String getUploadId() {
        return this.uploadId;
    }

    public ListUploadedPartResponse setUploadedParts(java.util.List<UploadPartInfo> uploadedParts) {
        this.uploadedParts = uploadedParts;
        return this;
    }
    public java.util.List<UploadPartInfo> getUploadedParts() {
        return this.uploadedParts;
    }

}
