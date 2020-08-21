// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.standard.client.models;

import com.aliyun.tea.*;

/**
 * 获取签名 response
 */
public class OSSListUploadedPartResponse extends TeaModel {
    // file_path
    @NameInMap("file_path")
    public String filePath;

    // next_part_number_marker
    @NameInMap("next_part_number_marker")
    public String nextPartNumberMarker;

    // upload_id
    @NameInMap("upload_id")
    public String uploadId;

    // uploaded_parts
    @NameInMap("uploaded_parts")
    public java.util.List<UploadPartInfo> uploadedParts;

    public static OSSListUploadedPartResponse build(java.util.Map<String, ?> map) throws Exception {
        OSSListUploadedPartResponse self = new OSSListUploadedPartResponse();
        return TeaModel.build(map, self);
    }

    public OSSListUploadedPartResponse setFilePath(String filePath) {
        this.filePath = filePath;
        return this;
    }
    public String getFilePath() {
        return this.filePath;
    }

    public OSSListUploadedPartResponse setNextPartNumberMarker(String nextPartNumberMarker) {
        this.nextPartNumberMarker = nextPartNumberMarker;
        return this;
    }
    public String getNextPartNumberMarker() {
        return this.nextPartNumberMarker;
    }

    public OSSListUploadedPartResponse setUploadId(String uploadId) {
        this.uploadId = uploadId;
        return this;
    }
    public String getUploadId() {
        return this.uploadId;
    }

    public OSSListUploadedPartResponse setUploadedParts(java.util.List<UploadPartInfo> uploadedParts) {
        this.uploadedParts = uploadedParts;
        return this;
    }
    public java.util.List<UploadPartInfo> getUploadedParts() {
        return this.uploadedParts;
    }

}
