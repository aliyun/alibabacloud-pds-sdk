// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * UCCreateFileResponse
 */
public class UCCreateFileResponse extends TeaModel {
    @NameInMap("callback")
    public Callback callback;

    // domain_id
    @NameInMap("domain_id")
    @Validation(pattern = "[a-z0-9]{1,50}", maxLength = 50, minLength = 40)
    public String domainId;

    // drive_id
    @NameInMap("drive_id")
    @Validation(pattern = "[0-9]+")
    public String driveId;

    // encrypt_mode
    @NameInMap("encrypt_mode")
    public String encryptMode;

    // exist
    // type: boolean
    @NameInMap("exist")
    public Boolean exist;

    // file_id
    @NameInMap("file_id")
    @Validation(pattern = "[a-z0-9]{1,50}", maxLength = 50, minLength = 40)
    public String fileId;

    // file_name
    @NameInMap("file_name")
    @Validation(maxLength = 255, minLength = 1)
    public String fileName;

    // location
    @NameInMap("location")
    public String location;

    // parent_file_id
    @NameInMap("parent_file_id")
    @Validation(pattern = "[a-z0-9]{1,50}", maxLength = 50, minLength = 40)
    public String parentFileId;

    // part_info_list
    @NameInMap("part_info_list")
    public java.util.List<UploadPartInfo> partInfoList;

    // rapid_upload
    // type: boolean
    @NameInMap("rapid_upload")
    public Boolean rapidUpload;

    // share_id
    @NameInMap("share_id")
    public String shareId;

    @NameInMap("signature")
    public SignatureInfo signature;

    // status
    @NameInMap("status")
    public String status;

    // streams_upload_info
    @NameInMap("streams_upload_info")
    public java.util.Map<String, ?> streamsUploadInfo;

    // type
    @NameInMap("type")
    public String type;

    // upload_id
    @NameInMap("upload_id")
    public String uploadId;

    // upload_type
    @NameInMap("upload_type")
    public String uploadType;

    public static UCCreateFileResponse build(java.util.Map<String, ?> map) throws Exception {
        UCCreateFileResponse self = new UCCreateFileResponse();
        return TeaModel.build(map, self);
    }

    public UCCreateFileResponse setCallback(Callback callback) {
        this.callback = callback;
        return this;
    }
    public Callback getCallback() {
        return this.callback;
    }

    public UCCreateFileResponse setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

    public UCCreateFileResponse setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public UCCreateFileResponse setEncryptMode(String encryptMode) {
        this.encryptMode = encryptMode;
        return this;
    }
    public String getEncryptMode() {
        return this.encryptMode;
    }

    public UCCreateFileResponse setExist(Boolean exist) {
        this.exist = exist;
        return this;
    }
    public Boolean getExist() {
        return this.exist;
    }

    public UCCreateFileResponse setFileId(String fileId) {
        this.fileId = fileId;
        return this;
    }
    public String getFileId() {
        return this.fileId;
    }

    public UCCreateFileResponse setFileName(String fileName) {
        this.fileName = fileName;
        return this;
    }
    public String getFileName() {
        return this.fileName;
    }

    public UCCreateFileResponse setLocation(String location) {
        this.location = location;
        return this;
    }
    public String getLocation() {
        return this.location;
    }

    public UCCreateFileResponse setParentFileId(String parentFileId) {
        this.parentFileId = parentFileId;
        return this;
    }
    public String getParentFileId() {
        return this.parentFileId;
    }

    public UCCreateFileResponse setPartInfoList(java.util.List<UploadPartInfo> partInfoList) {
        this.partInfoList = partInfoList;
        return this;
    }
    public java.util.List<UploadPartInfo> getPartInfoList() {
        return this.partInfoList;
    }

    public UCCreateFileResponse setRapidUpload(Boolean rapidUpload) {
        this.rapidUpload = rapidUpload;
        return this;
    }
    public Boolean getRapidUpload() {
        return this.rapidUpload;
    }

    public UCCreateFileResponse setShareId(String shareId) {
        this.shareId = shareId;
        return this;
    }
    public String getShareId() {
        return this.shareId;
    }

    public UCCreateFileResponse setSignature(SignatureInfo signature) {
        this.signature = signature;
        return this;
    }
    public SignatureInfo getSignature() {
        return this.signature;
    }

    public UCCreateFileResponse setStatus(String status) {
        this.status = status;
        return this;
    }
    public String getStatus() {
        return this.status;
    }

    public UCCreateFileResponse setStreamsUploadInfo(java.util.Map<String, ?> streamsUploadInfo) {
        this.streamsUploadInfo = streamsUploadInfo;
        return this;
    }
    public java.util.Map<String, ?> getStreamsUploadInfo() {
        return this.streamsUploadInfo;
    }

    public UCCreateFileResponse setType(String type) {
        this.type = type;
        return this;
    }
    public String getType() {
        return this.type;
    }

    public UCCreateFileResponse setUploadId(String uploadId) {
        this.uploadId = uploadId;
        return this;
    }
    public String getUploadId() {
        return this.uploadId;
    }

    public UCCreateFileResponse setUploadType(String uploadType) {
        this.uploadType = uploadType;
        return this;
    }
    public String getUploadType() {
        return this.uploadType;
    }

}
