// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * Create file response
 */
public class CreateFileResponse extends TeaModel {
    /**
     * <p>domain_id</p>
     */
    @NameInMap("domain_id")
    @Validation(pattern = "[a-z0-9]{1,50}", maxLength = 50, minLength = 40)
    public String domainId;

    /**
     * <p>drive_id</p>
     */
    @NameInMap("drive_id")
    @Validation(pattern = "[0-9]+")
    public String driveId;

    /**
     * <p>encrypt_mode</p>
     */
    @NameInMap("encrypt_mode")
    public String encryptMode;

    /**
     * <p>exist</p>
     * <p>type: boolean</p>
     */
    @NameInMap("exist")
    public Boolean exist;

    /**
     * <p>file_id</p>
     */
    @NameInMap("file_id")
    @Validation(pattern = "[a-z0-9]{1,50}", maxLength = 50, minLength = 40)
    public String fileId;

    /**
     * <p>file_name</p>
     */
    @NameInMap("file_name")
    @Validation(maxLength = 255, minLength = 1)
    public String fileName;

    /**
     * <p>location</p>
     */
    @NameInMap("location")
    public String location;

    /**
     * <p>parent_file_id</p>
     */
    @NameInMap("parent_file_id")
    @Validation(pattern = "[a-z0-9]{1,50}", maxLength = 50, minLength = 40)
    public String parentFileId;

    /**
     * <p>part_info_list</p>
     */
    @NameInMap("part_info_list")
    public java.util.List<UploadPartInfo> partInfoList;

    /**
     * <p>rapid_upload</p>
     * <p>type: boolean</p>
     */
    @NameInMap("rapid_upload")
    public Boolean rapidUpload;

    /**
     * <p>revision_id</p>
     */
    @NameInMap("revision_id")
    public String revisionId;

    /**
     * <p>share_id</p>
     */
    @NameInMap("share_id")
    public String shareId;

    /**
     * <p>status</p>
     */
    @NameInMap("status")
    public String status;

    /**
     * <p>streams_upload_info</p>
     */
    @NameInMap("streams_upload_info")
    public java.util.Map<String, ?> streamsUploadInfo;

    /**
     * <p>type</p>
     */
    @NameInMap("type")
    public String type;

    /**
     * <p>upload_id</p>
     */
    @NameInMap("upload_id")
    public String uploadId;

    public static CreateFileResponse build(java.util.Map<String, ?> map) throws Exception {
        CreateFileResponse self = new CreateFileResponse();
        return TeaModel.build(map, self);
    }

    public CreateFileResponse setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

    public CreateFileResponse setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public CreateFileResponse setEncryptMode(String encryptMode) {
        this.encryptMode = encryptMode;
        return this;
    }
    public String getEncryptMode() {
        return this.encryptMode;
    }

    public CreateFileResponse setExist(Boolean exist) {
        this.exist = exist;
        return this;
    }
    public Boolean getExist() {
        return this.exist;
    }

    public CreateFileResponse setFileId(String fileId) {
        this.fileId = fileId;
        return this;
    }
    public String getFileId() {
        return this.fileId;
    }

    public CreateFileResponse setFileName(String fileName) {
        this.fileName = fileName;
        return this;
    }
    public String getFileName() {
        return this.fileName;
    }

    public CreateFileResponse setLocation(String location) {
        this.location = location;
        return this;
    }
    public String getLocation() {
        return this.location;
    }

    public CreateFileResponse setParentFileId(String parentFileId) {
        this.parentFileId = parentFileId;
        return this;
    }
    public String getParentFileId() {
        return this.parentFileId;
    }

    public CreateFileResponse setPartInfoList(java.util.List<UploadPartInfo> partInfoList) {
        this.partInfoList = partInfoList;
        return this;
    }
    public java.util.List<UploadPartInfo> getPartInfoList() {
        return this.partInfoList;
    }

    public CreateFileResponse setRapidUpload(Boolean rapidUpload) {
        this.rapidUpload = rapidUpload;
        return this;
    }
    public Boolean getRapidUpload() {
        return this.rapidUpload;
    }

    public CreateFileResponse setRevisionId(String revisionId) {
        this.revisionId = revisionId;
        return this;
    }
    public String getRevisionId() {
        return this.revisionId;
    }

    public CreateFileResponse setShareId(String shareId) {
        this.shareId = shareId;
        return this;
    }
    public String getShareId() {
        return this.shareId;
    }

    public CreateFileResponse setStatus(String status) {
        this.status = status;
        return this;
    }
    public String getStatus() {
        return this.status;
    }

    public CreateFileResponse setStreamsUploadInfo(java.util.Map<String, ?> streamsUploadInfo) {
        this.streamsUploadInfo = streamsUploadInfo;
        return this;
    }
    public java.util.Map<String, ?> getStreamsUploadInfo() {
        return this.streamsUploadInfo;
    }

    public CreateFileResponse setType(String type) {
        this.type = type;
        return this;
    }
    public String getType() {
        return this.type;
    }

    public CreateFileResponse setUploadId(String uploadId) {
        this.uploadId = uploadId;
        return this;
    }
    public String getUploadId() {
        return this.uploadId;
    }

}
