// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * Base file response
 */
public class BaseCCPFileResponse extends TeaModel {
    // category
    @NameInMap("category")
    public String category;

    // CharacteristicHash
    @NameInMap("characteristic_hash")
    public String characteristicHash;

    // Content Hash
    @NameInMap("content_hash")
    public String contentHash;

    // content_hash_name
    @NameInMap("content_hash_name")
    public String contentHashName;

    // content_type
    @NameInMap("content_type")
    public String contentType;

    // crc64_hash
    @NameInMap("crc64_hash")
    public String crc64Hash;

    // created_at
    @NameInMap("created_at")
    public String createdAt;

    // description
    @NameInMap("description")
    public String description;

    // DomainID
    @NameInMap("domain_id")
    @Validation(pattern = "[a-z0-9A-Z]+")
    public String domainId;

    // download_url
    @NameInMap("download_url")
    public String downloadUrl;

    // drive_id
    @NameInMap("drive_id")
    @Validation(pattern = "[0-9]+")
    public String driveId;

    // encrypt_mode
    @NameInMap("encrypt_mode")
    public String encryptMode;

    // file_extension
    @NameInMap("file_extension")
    public String fileExtension;

    // file_id
    @NameInMap("file_id")
    @Validation(pattern = "[a-z0-9]{1,50}", maxLength = 50, minLength = 40)
    public String fileId;

    // Hidden
    // type: boolean
    @NameInMap("hidden")
    public Boolean hidden;

    @NameInMap("image_media_metadata")
    public ImageMediaResponse imageMediaMetadata;

    // labels
    @NameInMap("labels")
    public java.util.List<String> labels;

    @NameInMap("meta")
    public String meta;

    // name
    @NameInMap("name")
    @Validation(required = true, pattern = "[a-zA-Z0-9.-]{1,1000}")
    public String name;

    // parent_file_id
    @NameInMap("parent_file_id")
    @Validation(pattern = "[a-z0-9]{1,50}", maxLength = 50, minLength = 40)
    public String parentFileId;

    // PunishFlag
    @NameInMap("punish_flag")
    public Long punishFlag;

    @NameInMap("share_id")
    public String shareId;

    // Size
    @NameInMap("size")
    @Validation(maximum = 53687091200D)
    public Long size;

    // starred
    // type: boolean
    @NameInMap("starred")
    public Boolean starred;

    // status
    @NameInMap("status")
    public String status;

    // @Deprecated streams url info
    @NameInMap("streams_info")
    public java.util.Map<String, ?> streamsInfo;

    // thumbnail
    @NameInMap("thumbnail")
    public String thumbnail;

    // trashed_at
    @NameInMap("trashed_at")
    public String trashedAt;

    // type
    @NameInMap("type")
    public String type;

    // updated_at
    @NameInMap("updated_at")
    public String updatedAt;

    // upload_id
    @NameInMap("upload_id")
    public String uploadId;

    // url
    @NameInMap("url")
    public String url;

    // user_meta
    @NameInMap("user_meta")
    public String userMeta;

    @NameInMap("video_media_metadata")
    public VideoMediaResponse videoMediaMetadata;

    @NameInMap("video_preview_metadata")
    public VideoPreviewResponse videoPreviewMetadata;

    public static BaseCCPFileResponse build(java.util.Map<String, ?> map) throws Exception {
        BaseCCPFileResponse self = new BaseCCPFileResponse();
        return TeaModel.build(map, self);
    }

    public BaseCCPFileResponse setCategory(String category) {
        this.category = category;
        return this;
    }
    public String getCategory() {
        return this.category;
    }

    public BaseCCPFileResponse setCharacteristicHash(String characteristicHash) {
        this.characteristicHash = characteristicHash;
        return this;
    }
    public String getCharacteristicHash() {
        return this.characteristicHash;
    }

    public BaseCCPFileResponse setContentHash(String contentHash) {
        this.contentHash = contentHash;
        return this;
    }
    public String getContentHash() {
        return this.contentHash;
    }

    public BaseCCPFileResponse setContentHashName(String contentHashName) {
        this.contentHashName = contentHashName;
        return this;
    }
    public String getContentHashName() {
        return this.contentHashName;
    }

    public BaseCCPFileResponse setContentType(String contentType) {
        this.contentType = contentType;
        return this;
    }
    public String getContentType() {
        return this.contentType;
    }

    public BaseCCPFileResponse setCrc64Hash(String crc64Hash) {
        this.crc64Hash = crc64Hash;
        return this;
    }
    public String getCrc64Hash() {
        return this.crc64Hash;
    }

    public BaseCCPFileResponse setCreatedAt(String createdAt) {
        this.createdAt = createdAt;
        return this;
    }
    public String getCreatedAt() {
        return this.createdAt;
    }

    public BaseCCPFileResponse setDescription(String description) {
        this.description = description;
        return this;
    }
    public String getDescription() {
        return this.description;
    }

    public BaseCCPFileResponse setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

    public BaseCCPFileResponse setDownloadUrl(String downloadUrl) {
        this.downloadUrl = downloadUrl;
        return this;
    }
    public String getDownloadUrl() {
        return this.downloadUrl;
    }

    public BaseCCPFileResponse setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public BaseCCPFileResponse setEncryptMode(String encryptMode) {
        this.encryptMode = encryptMode;
        return this;
    }
    public String getEncryptMode() {
        return this.encryptMode;
    }

    public BaseCCPFileResponse setFileExtension(String fileExtension) {
        this.fileExtension = fileExtension;
        return this;
    }
    public String getFileExtension() {
        return this.fileExtension;
    }

    public BaseCCPFileResponse setFileId(String fileId) {
        this.fileId = fileId;
        return this;
    }
    public String getFileId() {
        return this.fileId;
    }

    public BaseCCPFileResponse setHidden(Boolean hidden) {
        this.hidden = hidden;
        return this;
    }
    public Boolean getHidden() {
        return this.hidden;
    }

    public BaseCCPFileResponse setImageMediaMetadata(ImageMediaResponse imageMediaMetadata) {
        this.imageMediaMetadata = imageMediaMetadata;
        return this;
    }
    public ImageMediaResponse getImageMediaMetadata() {
        return this.imageMediaMetadata;
    }

    public BaseCCPFileResponse setLabels(java.util.List<String> labels) {
        this.labels = labels;
        return this;
    }
    public java.util.List<String> getLabels() {
        return this.labels;
    }

    public BaseCCPFileResponse setMeta(String meta) {
        this.meta = meta;
        return this;
    }
    public String getMeta() {
        return this.meta;
    }

    public BaseCCPFileResponse setName(String name) {
        this.name = name;
        return this;
    }
    public String getName() {
        return this.name;
    }

    public BaseCCPFileResponse setParentFileId(String parentFileId) {
        this.parentFileId = parentFileId;
        return this;
    }
    public String getParentFileId() {
        return this.parentFileId;
    }

    public BaseCCPFileResponse setPunishFlag(Long punishFlag) {
        this.punishFlag = punishFlag;
        return this;
    }
    public Long getPunishFlag() {
        return this.punishFlag;
    }

    public BaseCCPFileResponse setShareId(String shareId) {
        this.shareId = shareId;
        return this;
    }
    public String getShareId() {
        return this.shareId;
    }

    public BaseCCPFileResponse setSize(Long size) {
        this.size = size;
        return this;
    }
    public Long getSize() {
        return this.size;
    }

    public BaseCCPFileResponse setStarred(Boolean starred) {
        this.starred = starred;
        return this;
    }
    public Boolean getStarred() {
        return this.starred;
    }

    public BaseCCPFileResponse setStatus(String status) {
        this.status = status;
        return this;
    }
    public String getStatus() {
        return this.status;
    }

    public BaseCCPFileResponse setStreamsInfo(java.util.Map<String, ?> streamsInfo) {
        this.streamsInfo = streamsInfo;
        return this;
    }
    public java.util.Map<String, ?> getStreamsInfo() {
        return this.streamsInfo;
    }

    public BaseCCPFileResponse setThumbnail(String thumbnail) {
        this.thumbnail = thumbnail;
        return this;
    }
    public String getThumbnail() {
        return this.thumbnail;
    }

    public BaseCCPFileResponse setTrashedAt(String trashedAt) {
        this.trashedAt = trashedAt;
        return this;
    }
    public String getTrashedAt() {
        return this.trashedAt;
    }

    public BaseCCPFileResponse setType(String type) {
        this.type = type;
        return this;
    }
    public String getType() {
        return this.type;
    }

    public BaseCCPFileResponse setUpdatedAt(String updatedAt) {
        this.updatedAt = updatedAt;
        return this;
    }
    public String getUpdatedAt() {
        return this.updatedAt;
    }

    public BaseCCPFileResponse setUploadId(String uploadId) {
        this.uploadId = uploadId;
        return this;
    }
    public String getUploadId() {
        return this.uploadId;
    }

    public BaseCCPFileResponse setUrl(String url) {
        this.url = url;
        return this;
    }
    public String getUrl() {
        return this.url;
    }

    public BaseCCPFileResponse setUserMeta(String userMeta) {
        this.userMeta = userMeta;
        return this;
    }
    public String getUserMeta() {
        return this.userMeta;
    }

    public BaseCCPFileResponse setVideoMediaMetadata(VideoMediaResponse videoMediaMetadata) {
        this.videoMediaMetadata = videoMediaMetadata;
        return this;
    }
    public VideoMediaResponse getVideoMediaMetadata() {
        return this.videoMediaMetadata;
    }

    public BaseCCPFileResponse setVideoPreviewMetadata(VideoPreviewResponse videoPreviewMetadata) {
        this.videoPreviewMetadata = videoPreviewMetadata;
        return this;
    }
    public VideoPreviewResponse getVideoPreviewMetadata() {
        return this.videoPreviewMetadata;
    }

}
