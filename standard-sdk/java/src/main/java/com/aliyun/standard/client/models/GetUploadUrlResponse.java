// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.standard.client.models;

import com.aliyun.tea.*;

/**
 * Get UploadUrl Response
 */
public class GetUploadUrlResponse extends TeaModel {
    // created_at
    @NameInMap("create_at")
    public String createAt;

    // domain_id
    @NameInMap("domain_id")
    @Validation(pattern = "[a-z0-9A-Z]+")
    public String domainId;

    // drive_id
    @NameInMap("drive_id")
    @Validation(pattern = "[0-9]+")
    public String driveId;

    // file_id
    @NameInMap("file_id")
    @Validation(pattern = "[a-z0-9]{1,50}", maxLength = 50, minLength = 40)
    public String fileId;

    // part_info_list
    @NameInMap("part_info_list")
    public java.util.List<UploadPartInfo> partInfoList;

    // upload_id
    @NameInMap("upload_id")
    public String uploadId;

    public static GetUploadUrlResponse build(java.util.Map<String, ?> map) throws Exception {
        GetUploadUrlResponse self = new GetUploadUrlResponse();
        return TeaModel.build(map, self);
    }

    public GetUploadUrlResponse setCreateAt(String createAt) {
        this.createAt = createAt;
        return this;
    }
    public String getCreateAt() {
        return this.createAt;
    }

    public GetUploadUrlResponse setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

    public GetUploadUrlResponse setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public GetUploadUrlResponse setFileId(String fileId) {
        this.fileId = fileId;
        return this;
    }
    public String getFileId() {
        return this.fileId;
    }

    public GetUploadUrlResponse setPartInfoList(java.util.List<UploadPartInfo> partInfoList) {
        this.partInfoList = partInfoList;
        return this;
    }
    public java.util.List<UploadPartInfo> getPartInfoList() {
        return this.partInfoList;
    }

    public GetUploadUrlResponse setUploadId(String uploadId) {
        this.uploadId = uploadId;
        return this;
    }
    public String getUploadId() {
        return this.uploadId;
    }

}
