// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 获取文件下载地址的请求body
 */
public class GetDownloadUrlRequest extends TeaModel {
    // addition_data
    @NameInMap("addition_data")
    public java.util.Map<String, ?> additionData;

    // drive_id
    @NameInMap("drive_id")
    @Validation(pattern = "[0-9]+")
    public String driveId;

    // expire_sec
    @NameInMap("expire_sec")
    @Validation(maximum = 115200, minimum = 1)
    public Long expireSec;

    // file_id
    @NameInMap("file_id")
    @Validation(required = true, pattern = "[a-z0-9.-_]{1,50}", maxLength = 50, minLength = 40)
    public String fileId;

    @NameInMap("file_id_path")
    public String fileIdPath;

    // file_name
    @NameInMap("file_name")
    @Validation(maxLength = 1024, minLength = 1)
    public String fileName;

    // location
    @NameInMap("location")
    public String location;

    @NameInMap("referer")
    public String referer;

    // share_id, either share_id or drive_id is required
    @NameInMap("share_id")
    public String shareId;

    @NameInMap("sign_token")
    public String signToken;

    public static GetDownloadUrlRequest build(java.util.Map<String, ?> map) throws Exception {
        GetDownloadUrlRequest self = new GetDownloadUrlRequest();
        return TeaModel.build(map, self);
    }

    public GetDownloadUrlRequest setAdditionData(java.util.Map<String, ?> additionData) {
        this.additionData = additionData;
        return this;
    }
    public java.util.Map<String, ?> getAdditionData() {
        return this.additionData;
    }

    public GetDownloadUrlRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public GetDownloadUrlRequest setExpireSec(Long expireSec) {
        this.expireSec = expireSec;
        return this;
    }
    public Long getExpireSec() {
        return this.expireSec;
    }

    public GetDownloadUrlRequest setFileId(String fileId) {
        this.fileId = fileId;
        return this;
    }
    public String getFileId() {
        return this.fileId;
    }

    public GetDownloadUrlRequest setFileIdPath(String fileIdPath) {
        this.fileIdPath = fileIdPath;
        return this;
    }
    public String getFileIdPath() {
        return this.fileIdPath;
    }

    public GetDownloadUrlRequest setFileName(String fileName) {
        this.fileName = fileName;
        return this;
    }
    public String getFileName() {
        return this.fileName;
    }

    public GetDownloadUrlRequest setLocation(String location) {
        this.location = location;
        return this;
    }
    public String getLocation() {
        return this.location;
    }

    public GetDownloadUrlRequest setReferer(String referer) {
        this.referer = referer;
        return this;
    }
    public String getReferer() {
        return this.referer;
    }

    public GetDownloadUrlRequest setShareId(String shareId) {
        this.shareId = shareId;
        return this;
    }
    public String getShareId() {
        return this.shareId;
    }

    public GetDownloadUrlRequest setSignToken(String signToken) {
        this.signToken = signToken;
        return this;
    }
    public String getSignToken() {
        return this.signToken;
    }

}
