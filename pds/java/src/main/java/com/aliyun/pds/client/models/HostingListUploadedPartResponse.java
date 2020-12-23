// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 获取签名 response
 */
public class HostingListUploadedPartResponse extends TeaModel {
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

    public static HostingListUploadedPartResponse build(java.util.Map<String, ?> map) throws Exception {
        HostingListUploadedPartResponse self = new HostingListUploadedPartResponse();
        return TeaModel.build(map, self);
    }

    public HostingListUploadedPartResponse setFilePath(String filePath) {
        this.filePath = filePath;
        return this;
    }
    public String getFilePath() {
        return this.filePath;
    }

    public HostingListUploadedPartResponse setNextPartNumberMarker(String nextPartNumberMarker) {
        this.nextPartNumberMarker = nextPartNumberMarker;
        return this;
    }
    public String getNextPartNumberMarker() {
        return this.nextPartNumberMarker;
    }

    public HostingListUploadedPartResponse setUploadId(String uploadId) {
        this.uploadId = uploadId;
        return this;
    }
    public String getUploadId() {
        return this.uploadId;
    }

    public HostingListUploadedPartResponse setUploadedParts(java.util.List<UploadPartInfo> uploadedParts) {
        this.uploadedParts = uploadedParts;
        return this;
    }
    public java.util.List<UploadPartInfo> getUploadedParts() {
        return this.uploadedParts;
    }

}
