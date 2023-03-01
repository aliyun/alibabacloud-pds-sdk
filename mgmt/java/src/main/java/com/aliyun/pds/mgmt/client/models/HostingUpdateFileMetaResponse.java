// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 更新文件元数据 response
 */
public class HostingUpdateFileMetaResponse extends TeaModel {
    /**
     * <p>Content Hash</p>
     */
    @NameInMap("content_hash")
    public String contentHash;

    /**
     * <p>content_hash_name</p>
     */
    @NameInMap("content_hash_name")
    public String contentHashName;

    /**
     * <p>content_type</p>
     */
    @NameInMap("content_type")
    public String contentType;

    /**
     * <p>crc64_hash</p>
     */
    @NameInMap("crc64_hash")
    public String crc64Hash;

    /**
     * <p>created_at</p>
     */
    @NameInMap("created_at")
    public String createdAt;

    /**
     * <p>description</p>
     */
    @NameInMap("description")
    public String description;

    /**
     * <p>domain_id</p>
     */
    @NameInMap("domain_id")
    @Validation(pattern = "[a-z0-9A-Z]+")
    public String domainId;

    /**
     * <p>download_url</p>
     */
    @NameInMap("download_url")
    public String downloadUrl;

    /**
     * <p>drive_id</p>
     */
    @NameInMap("drive_id")
    @Validation(pattern = "[0-9]+")
    public String driveId;

    /**
     * <p>file_extension</p>
     */
    @NameInMap("file_extension")
    public String fileExtension;

    /**
     * <p>file_path</p>
     */
    @NameInMap("file_path")
    public String filePath;

    /**
     * <p>name</p>
     */
    @NameInMap("name")
    @Validation(required = true, pattern = "[a-zA-Z0-9.-]{1,1000}")
    public String name;

    /**
     * <p>parent_file_id</p>
     */
    @NameInMap("parent_file_path")
    @Validation(pattern = "[a-z0-9]{1,50}", maxLength = 50, minLength = 40)
    public String parentFilePath;

    /**
     * <p>share_id</p>
     */
    @NameInMap("share_id")
    @Validation(pattern = "[0-9]+")
    public String shareId;

    /**
     * <p>Size</p>
     */
    @NameInMap("size")
    public Long size;

    /**
     * <p>status</p>
     */
    @NameInMap("status")
    public String status;

    /**
     * <p>thumbnail</p>
     */
    @NameInMap("thumbnail")
    public String thumbnail;

    /**
     * <p>trashed_at</p>
     */
    @NameInMap("trashed_at")
    public String trashedAt;

    /**
     * <p>type</p>
     */
    @NameInMap("type")
    public String type;

    /**
     * <p>updated_at</p>
     */
    @NameInMap("updated_at")
    public String updatedAt;

    /**
     * <p>upload_id</p>
     */
    @NameInMap("upload_id")
    public String uploadId;

    /**
     * <p>url</p>
     */
    @NameInMap("url")
    public String url;

    public static HostingUpdateFileMetaResponse build(java.util.Map<String, ?> map) throws Exception {
        HostingUpdateFileMetaResponse self = new HostingUpdateFileMetaResponse();
        return TeaModel.build(map, self);
    }

    public HostingUpdateFileMetaResponse setContentHash(String contentHash) {
        this.contentHash = contentHash;
        return this;
    }
    public String getContentHash() {
        return this.contentHash;
    }

    public HostingUpdateFileMetaResponse setContentHashName(String contentHashName) {
        this.contentHashName = contentHashName;
        return this;
    }
    public String getContentHashName() {
        return this.contentHashName;
    }

    public HostingUpdateFileMetaResponse setContentType(String contentType) {
        this.contentType = contentType;
        return this;
    }
    public String getContentType() {
        return this.contentType;
    }

    public HostingUpdateFileMetaResponse setCrc64Hash(String crc64Hash) {
        this.crc64Hash = crc64Hash;
        return this;
    }
    public String getCrc64Hash() {
        return this.crc64Hash;
    }

    public HostingUpdateFileMetaResponse setCreatedAt(String createdAt) {
        this.createdAt = createdAt;
        return this;
    }
    public String getCreatedAt() {
        return this.createdAt;
    }

    public HostingUpdateFileMetaResponse setDescription(String description) {
        this.description = description;
        return this;
    }
    public String getDescription() {
        return this.description;
    }

    public HostingUpdateFileMetaResponse setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

    public HostingUpdateFileMetaResponse setDownloadUrl(String downloadUrl) {
        this.downloadUrl = downloadUrl;
        return this;
    }
    public String getDownloadUrl() {
        return this.downloadUrl;
    }

    public HostingUpdateFileMetaResponse setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public HostingUpdateFileMetaResponse setFileExtension(String fileExtension) {
        this.fileExtension = fileExtension;
        return this;
    }
    public String getFileExtension() {
        return this.fileExtension;
    }

    public HostingUpdateFileMetaResponse setFilePath(String filePath) {
        this.filePath = filePath;
        return this;
    }
    public String getFilePath() {
        return this.filePath;
    }

    public HostingUpdateFileMetaResponse setName(String name) {
        this.name = name;
        return this;
    }
    public String getName() {
        return this.name;
    }

    public HostingUpdateFileMetaResponse setParentFilePath(String parentFilePath) {
        this.parentFilePath = parentFilePath;
        return this;
    }
    public String getParentFilePath() {
        return this.parentFilePath;
    }

    public HostingUpdateFileMetaResponse setShareId(String shareId) {
        this.shareId = shareId;
        return this;
    }
    public String getShareId() {
        return this.shareId;
    }

    public HostingUpdateFileMetaResponse setSize(Long size) {
        this.size = size;
        return this;
    }
    public Long getSize() {
        return this.size;
    }

    public HostingUpdateFileMetaResponse setStatus(String status) {
        this.status = status;
        return this;
    }
    public String getStatus() {
        return this.status;
    }

    public HostingUpdateFileMetaResponse setThumbnail(String thumbnail) {
        this.thumbnail = thumbnail;
        return this;
    }
    public String getThumbnail() {
        return this.thumbnail;
    }

    public HostingUpdateFileMetaResponse setTrashedAt(String trashedAt) {
        this.trashedAt = trashedAt;
        return this;
    }
    public String getTrashedAt() {
        return this.trashedAt;
    }

    public HostingUpdateFileMetaResponse setType(String type) {
        this.type = type;
        return this;
    }
    public String getType() {
        return this.type;
    }

    public HostingUpdateFileMetaResponse setUpdatedAt(String updatedAt) {
        this.updatedAt = updatedAt;
        return this;
    }
    public String getUpdatedAt() {
        return this.updatedAt;
    }

    public HostingUpdateFileMetaResponse setUploadId(String uploadId) {
        this.uploadId = uploadId;
        return this;
    }
    public String getUploadId() {
        return this.uploadId;
    }

    public HostingUpdateFileMetaResponse setUrl(String url) {
        this.url = url;
        return this;
    }
    public String getUrl() {
        return this.url;
    }

}
