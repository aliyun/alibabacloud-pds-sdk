// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 获取文件元数据response
 */
public class GetFileResponse extends TeaModel {
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

    // Trashed
    // type: boolean
    @NameInMap("trashed")
    public Boolean trashed;

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

    public static GetFileResponse build(java.util.Map<String, ?> map) throws Exception {
        GetFileResponse self = new GetFileResponse();
        return TeaModel.build(map, self);
    }

    public GetFileResponse setCategory(String category) {
        this.category = category;
        return this;
    }
    public String getCategory() {
        return this.category;
    }

    public GetFileResponse setCharacteristicHash(String characteristicHash) {
        this.characteristicHash = characteristicHash;
        return this;
    }
    public String getCharacteristicHash() {
        return this.characteristicHash;
    }

    public GetFileResponse setContentHash(String contentHash) {
        this.contentHash = contentHash;
        return this;
    }
    public String getContentHash() {
        return this.contentHash;
    }

    public GetFileResponse setContentHashName(String contentHashName) {
        this.contentHashName = contentHashName;
        return this;
    }
    public String getContentHashName() {
        return this.contentHashName;
    }

    public GetFileResponse setContentType(String contentType) {
        this.contentType = contentType;
        return this;
    }
    public String getContentType() {
        return this.contentType;
    }

    public GetFileResponse setCrc64Hash(String crc64Hash) {
        this.crc64Hash = crc64Hash;
        return this;
    }
    public String getCrc64Hash() {
        return this.crc64Hash;
    }

    public GetFileResponse setCreatedAt(String createdAt) {
        this.createdAt = createdAt;
        return this;
    }
    public String getCreatedAt() {
        return this.createdAt;
    }

    public GetFileResponse setDescription(String description) {
        this.description = description;
        return this;
    }
    public String getDescription() {
        return this.description;
    }

    public GetFileResponse setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

    public GetFileResponse setDownloadUrl(String downloadUrl) {
        this.downloadUrl = downloadUrl;
        return this;
    }
    public String getDownloadUrl() {
        return this.downloadUrl;
    }

    public GetFileResponse setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public GetFileResponse setEncryptMode(String encryptMode) {
        this.encryptMode = encryptMode;
        return this;
    }
    public String getEncryptMode() {
        return this.encryptMode;
    }

    public GetFileResponse setFileExtension(String fileExtension) {
        this.fileExtension = fileExtension;
        return this;
    }
    public String getFileExtension() {
        return this.fileExtension;
    }

    public GetFileResponse setFileId(String fileId) {
        this.fileId = fileId;
        return this;
    }
    public String getFileId() {
        return this.fileId;
    }

    public GetFileResponse setHidden(Boolean hidden) {
        this.hidden = hidden;
        return this;
    }
    public Boolean getHidden() {
        return this.hidden;
    }

    public GetFileResponse setImageMediaMetadata(ImageMediaResponse imageMediaMetadata) {
        this.imageMediaMetadata = imageMediaMetadata;
        return this;
    }
    public ImageMediaResponse getImageMediaMetadata() {
        return this.imageMediaMetadata;
    }

    public GetFileResponse setLabels(java.util.List<String> labels) {
        this.labels = labels;
        return this;
    }
    public java.util.List<String> getLabels() {
        return this.labels;
    }

    public GetFileResponse setMeta(String meta) {
        this.meta = meta;
        return this;
    }
    public String getMeta() {
        return this.meta;
    }

    public GetFileResponse setName(String name) {
        this.name = name;
        return this;
    }
    public String getName() {
        return this.name;
    }

    public GetFileResponse setParentFileId(String parentFileId) {
        this.parentFileId = parentFileId;
        return this;
    }
    public String getParentFileId() {
        return this.parentFileId;
    }

    public GetFileResponse setPunishFlag(Long punishFlag) {
        this.punishFlag = punishFlag;
        return this;
    }
    public Long getPunishFlag() {
        return this.punishFlag;
    }

    public GetFileResponse setShareId(String shareId) {
        this.shareId = shareId;
        return this;
    }
    public String getShareId() {
        return this.shareId;
    }

    public GetFileResponse setSize(Long size) {
        this.size = size;
        return this;
    }
    public Long getSize() {
        return this.size;
    }

    public GetFileResponse setStarred(Boolean starred) {
        this.starred = starred;
        return this;
    }
    public Boolean getStarred() {
        return this.starred;
    }

    public GetFileResponse setStatus(String status) {
        this.status = status;
        return this;
    }
    public String getStatus() {
        return this.status;
    }

    public GetFileResponse setStreamsInfo(java.util.Map<String, ?> streamsInfo) {
        this.streamsInfo = streamsInfo;
        return this;
    }
    public java.util.Map<String, ?> getStreamsInfo() {
        return this.streamsInfo;
    }

    public GetFileResponse setThumbnail(String thumbnail) {
        this.thumbnail = thumbnail;
        return this;
    }
    public String getThumbnail() {
        return this.thumbnail;
    }

    public GetFileResponse setTrashed(Boolean trashed) {
        this.trashed = trashed;
        return this;
    }
    public Boolean getTrashed() {
        return this.trashed;
    }

    public GetFileResponse setTrashedAt(String trashedAt) {
        this.trashedAt = trashedAt;
        return this;
    }
    public String getTrashedAt() {
        return this.trashedAt;
    }

    public GetFileResponse setType(String type) {
        this.type = type;
        return this;
    }
    public String getType() {
        return this.type;
    }

    public GetFileResponse setUpdatedAt(String updatedAt) {
        this.updatedAt = updatedAt;
        return this;
    }
    public String getUpdatedAt() {
        return this.updatedAt;
    }

    public GetFileResponse setUploadId(String uploadId) {
        this.uploadId = uploadId;
        return this;
    }
    public String getUploadId() {
        return this.uploadId;
    }

    public GetFileResponse setUrl(String url) {
        this.url = url;
        return this;
    }
    public String getUrl() {
        return this.url;
    }

    public GetFileResponse setUserMeta(String userMeta) {
        this.userMeta = userMeta;
        return this;
    }
    public String getUserMeta() {
        return this.userMeta;
    }

    public GetFileResponse setVideoMediaMetadata(VideoMediaResponse videoMediaMetadata) {
        this.videoMediaMetadata = videoMediaMetadata;
        return this;
    }
    public VideoMediaResponse getVideoMediaMetadata() {
        return this.videoMediaMetadata;
    }

    public GetFileResponse setVideoPreviewMetadata(VideoPreviewResponse videoPreviewMetadata) {
        this.videoPreviewMetadata = videoPreviewMetadata;
        return this;
    }
    public VideoPreviewResponse getVideoPreviewMetadata() {
        return this.videoPreviewMetadata;
    }

}
