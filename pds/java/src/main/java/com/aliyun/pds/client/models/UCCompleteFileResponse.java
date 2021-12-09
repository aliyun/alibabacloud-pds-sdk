// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * UCCompleteFileResponse
 */
public class UCCompleteFileResponse extends TeaModel {
    // action_list
    @NameInMap("action_list")
    public java.util.List<String> actionList;

    // auto_delete_left_sec
    @NameInMap("auto_delete_left_sec")
    public Long autoDeleteLeftSec;

    // bucket_name
    @NameInMap("bucket_name")
    public String bucketName;

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

    // creator_id
    @NameInMap("creator_id")
    public String creatorId;

    // creator_name
    @NameInMap("creator_name")
    public String creatorName;

    // creator_type
    @NameInMap("creator_type")
    public String creatorType;

    // custom_field_1
    @NameInMap("custom_field_1")
    public String customField1;

    // custom_field_2
    @NameInMap("custom_field_2")
    public String customField2;

    // custom_type
    @NameInMap("custom_type")
    public String customType;

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

    // endpoint
    @NameInMap("endpoint")
    public String endpoint;

    // ex_fields_info
    @NameInMap("ex_fields_info")
    public java.util.Map<String, ?> exFieldsInfo;

    // file_extension
    @NameInMap("file_extension")
    public String fileExtension;

    // file_id
    @NameInMap("file_id")
    @Validation(pattern = "[a-z0-9]{1,50}", maxLength = 50, minLength = 40)
    public String fileId;

    // TODO 先不在API上透出该字段，file_path_type目前在edm中返回；path type是否在PDS通用逻辑中展示，展示的含义是什么，需要再做分析
    @NameInMap("file_path_type")
    public String filePathType;

    // Hidden
    // type: boolean
    @NameInMap("hidden")
    public Boolean hidden;

    @NameInMap("image_media_metadata")
    public ImageMediaResponse imageMediaMetadata;

    // labels
    @NameInMap("labels")
    public java.util.List<String> labels;

    // last_modifier_id
    @NameInMap("last_modifier_id")
    public String lastModifierId;

    // last_modifier_name
    @NameInMap("last_modifier_name")
    public String lastModifierName;

    // last_modifier_type
    @NameInMap("last_modifier_type")
    public String lastModifierType;

    // local_created_at
    @NameInMap("local_created_at")
    public String localCreatedAt;

    @NameInMap("meta")
    public String meta;

    // mime_extension
    @NameInMap("mime_extension")
    public String mimeExtension;

    // mime_type
    @NameInMap("mime_type")
    public String mimeType;

    // name
    @NameInMap("name")
    @Validation(required = true, pattern = "[a-zA-Z0-9.-]{1,1000}")
    public String name;

    // object_key
    @NameInMap("object_key")
    public String objectKey;

    // parent_file_id
    @NameInMap("parent_file_id")
    @Validation(pattern = "[a-z0-9]{1,50}", maxLength = 50, minLength = 40)
    public String parentFileId;

    // PunishFlag
    @NameInMap("punish_flag")
    public Long punishFlag;

    // revision_id
    @NameInMap("revision_id")
    public String revisionId;

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

    // user_tags
    @NameInMap("user_tags")
    public java.util.Map<String, ?> userTags;

    @NameInMap("video_media_metadata")
    public VideoMediaResponse videoMediaMetadata;

    @NameInMap("video_preview_metadata")
    public VideoPreviewResponse videoPreviewMetadata;

    public static UCCompleteFileResponse build(java.util.Map<String, ?> map) throws Exception {
        UCCompleteFileResponse self = new UCCompleteFileResponse();
        return TeaModel.build(map, self);
    }

    public UCCompleteFileResponse setActionList(java.util.List<String> actionList) {
        this.actionList = actionList;
        return this;
    }
    public java.util.List<String> getActionList() {
        return this.actionList;
    }

    public UCCompleteFileResponse setAutoDeleteLeftSec(Long autoDeleteLeftSec) {
        this.autoDeleteLeftSec = autoDeleteLeftSec;
        return this;
    }
    public Long getAutoDeleteLeftSec() {
        return this.autoDeleteLeftSec;
    }

    public UCCompleteFileResponse setBucketName(String bucketName) {
        this.bucketName = bucketName;
        return this;
    }
    public String getBucketName() {
        return this.bucketName;
    }

    public UCCompleteFileResponse setCategory(String category) {
        this.category = category;
        return this;
    }
    public String getCategory() {
        return this.category;
    }

    public UCCompleteFileResponse setCharacteristicHash(String characteristicHash) {
        this.characteristicHash = characteristicHash;
        return this;
    }
    public String getCharacteristicHash() {
        return this.characteristicHash;
    }

    public UCCompleteFileResponse setContentHash(String contentHash) {
        this.contentHash = contentHash;
        return this;
    }
    public String getContentHash() {
        return this.contentHash;
    }

    public UCCompleteFileResponse setContentHashName(String contentHashName) {
        this.contentHashName = contentHashName;
        return this;
    }
    public String getContentHashName() {
        return this.contentHashName;
    }

    public UCCompleteFileResponse setContentType(String contentType) {
        this.contentType = contentType;
        return this;
    }
    public String getContentType() {
        return this.contentType;
    }

    public UCCompleteFileResponse setCrc64Hash(String crc64Hash) {
        this.crc64Hash = crc64Hash;
        return this;
    }
    public String getCrc64Hash() {
        return this.crc64Hash;
    }

    public UCCompleteFileResponse setCreatedAt(String createdAt) {
        this.createdAt = createdAt;
        return this;
    }
    public String getCreatedAt() {
        return this.createdAt;
    }

    public UCCompleteFileResponse setCreatorId(String creatorId) {
        this.creatorId = creatorId;
        return this;
    }
    public String getCreatorId() {
        return this.creatorId;
    }

    public UCCompleteFileResponse setCreatorName(String creatorName) {
        this.creatorName = creatorName;
        return this;
    }
    public String getCreatorName() {
        return this.creatorName;
    }

    public UCCompleteFileResponse setCreatorType(String creatorType) {
        this.creatorType = creatorType;
        return this;
    }
    public String getCreatorType() {
        return this.creatorType;
    }

    public UCCompleteFileResponse setCustomField1(String customField1) {
        this.customField1 = customField1;
        return this;
    }
    public String getCustomField1() {
        return this.customField1;
    }

    public UCCompleteFileResponse setCustomField2(String customField2) {
        this.customField2 = customField2;
        return this;
    }
    public String getCustomField2() {
        return this.customField2;
    }

    public UCCompleteFileResponse setCustomType(String customType) {
        this.customType = customType;
        return this;
    }
    public String getCustomType() {
        return this.customType;
    }

    public UCCompleteFileResponse setDescription(String description) {
        this.description = description;
        return this;
    }
    public String getDescription() {
        return this.description;
    }

    public UCCompleteFileResponse setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

    public UCCompleteFileResponse setDownloadUrl(String downloadUrl) {
        this.downloadUrl = downloadUrl;
        return this;
    }
    public String getDownloadUrl() {
        return this.downloadUrl;
    }

    public UCCompleteFileResponse setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public UCCompleteFileResponse setEncryptMode(String encryptMode) {
        this.encryptMode = encryptMode;
        return this;
    }
    public String getEncryptMode() {
        return this.encryptMode;
    }

    public UCCompleteFileResponse setEndpoint(String endpoint) {
        this.endpoint = endpoint;
        return this;
    }
    public String getEndpoint() {
        return this.endpoint;
    }

    public UCCompleteFileResponse setExFieldsInfo(java.util.Map<String, ?> exFieldsInfo) {
        this.exFieldsInfo = exFieldsInfo;
        return this;
    }
    public java.util.Map<String, ?> getExFieldsInfo() {
        return this.exFieldsInfo;
    }

    public UCCompleteFileResponse setFileExtension(String fileExtension) {
        this.fileExtension = fileExtension;
        return this;
    }
    public String getFileExtension() {
        return this.fileExtension;
    }

    public UCCompleteFileResponse setFileId(String fileId) {
        this.fileId = fileId;
        return this;
    }
    public String getFileId() {
        return this.fileId;
    }

    public UCCompleteFileResponse setFilePathType(String filePathType) {
        this.filePathType = filePathType;
        return this;
    }
    public String getFilePathType() {
        return this.filePathType;
    }

    public UCCompleteFileResponse setHidden(Boolean hidden) {
        this.hidden = hidden;
        return this;
    }
    public Boolean getHidden() {
        return this.hidden;
    }

    public UCCompleteFileResponse setImageMediaMetadata(ImageMediaResponse imageMediaMetadata) {
        this.imageMediaMetadata = imageMediaMetadata;
        return this;
    }
    public ImageMediaResponse getImageMediaMetadata() {
        return this.imageMediaMetadata;
    }

    public UCCompleteFileResponse setLabels(java.util.List<String> labels) {
        this.labels = labels;
        return this;
    }
    public java.util.List<String> getLabels() {
        return this.labels;
    }

    public UCCompleteFileResponse setLastModifierId(String lastModifierId) {
        this.lastModifierId = lastModifierId;
        return this;
    }
    public String getLastModifierId() {
        return this.lastModifierId;
    }

    public UCCompleteFileResponse setLastModifierName(String lastModifierName) {
        this.lastModifierName = lastModifierName;
        return this;
    }
    public String getLastModifierName() {
        return this.lastModifierName;
    }

    public UCCompleteFileResponse setLastModifierType(String lastModifierType) {
        this.lastModifierType = lastModifierType;
        return this;
    }
    public String getLastModifierType() {
        return this.lastModifierType;
    }

    public UCCompleteFileResponse setLocalCreatedAt(String localCreatedAt) {
        this.localCreatedAt = localCreatedAt;
        return this;
    }
    public String getLocalCreatedAt() {
        return this.localCreatedAt;
    }

    public UCCompleteFileResponse setMeta(String meta) {
        this.meta = meta;
        return this;
    }
    public String getMeta() {
        return this.meta;
    }

    public UCCompleteFileResponse setMimeExtension(String mimeExtension) {
        this.mimeExtension = mimeExtension;
        return this;
    }
    public String getMimeExtension() {
        return this.mimeExtension;
    }

    public UCCompleteFileResponse setMimeType(String mimeType) {
        this.mimeType = mimeType;
        return this;
    }
    public String getMimeType() {
        return this.mimeType;
    }

    public UCCompleteFileResponse setName(String name) {
        this.name = name;
        return this;
    }
    public String getName() {
        return this.name;
    }

    public UCCompleteFileResponse setObjectKey(String objectKey) {
        this.objectKey = objectKey;
        return this;
    }
    public String getObjectKey() {
        return this.objectKey;
    }

    public UCCompleteFileResponse setParentFileId(String parentFileId) {
        this.parentFileId = parentFileId;
        return this;
    }
    public String getParentFileId() {
        return this.parentFileId;
    }

    public UCCompleteFileResponse setPunishFlag(Long punishFlag) {
        this.punishFlag = punishFlag;
        return this;
    }
    public Long getPunishFlag() {
        return this.punishFlag;
    }

    public UCCompleteFileResponse setRevisionId(String revisionId) {
        this.revisionId = revisionId;
        return this;
    }
    public String getRevisionId() {
        return this.revisionId;
    }

    public UCCompleteFileResponse setShareId(String shareId) {
        this.shareId = shareId;
        return this;
    }
    public String getShareId() {
        return this.shareId;
    }

    public UCCompleteFileResponse setSize(Long size) {
        this.size = size;
        return this;
    }
    public Long getSize() {
        return this.size;
    }

    public UCCompleteFileResponse setStarred(Boolean starred) {
        this.starred = starred;
        return this;
    }
    public Boolean getStarred() {
        return this.starred;
    }

    public UCCompleteFileResponse setStatus(String status) {
        this.status = status;
        return this;
    }
    public String getStatus() {
        return this.status;
    }

    public UCCompleteFileResponse setStreamsInfo(java.util.Map<String, ?> streamsInfo) {
        this.streamsInfo = streamsInfo;
        return this;
    }
    public java.util.Map<String, ?> getStreamsInfo() {
        return this.streamsInfo;
    }

    public UCCompleteFileResponse setThumbnail(String thumbnail) {
        this.thumbnail = thumbnail;
        return this;
    }
    public String getThumbnail() {
        return this.thumbnail;
    }

    public UCCompleteFileResponse setTrashedAt(String trashedAt) {
        this.trashedAt = trashedAt;
        return this;
    }
    public String getTrashedAt() {
        return this.trashedAt;
    }

    public UCCompleteFileResponse setType(String type) {
        this.type = type;
        return this;
    }
    public String getType() {
        return this.type;
    }

    public UCCompleteFileResponse setUpdatedAt(String updatedAt) {
        this.updatedAt = updatedAt;
        return this;
    }
    public String getUpdatedAt() {
        return this.updatedAt;
    }

    public UCCompleteFileResponse setUploadId(String uploadId) {
        this.uploadId = uploadId;
        return this;
    }
    public String getUploadId() {
        return this.uploadId;
    }

    public UCCompleteFileResponse setUrl(String url) {
        this.url = url;
        return this;
    }
    public String getUrl() {
        return this.url;
    }

    public UCCompleteFileResponse setUserMeta(String userMeta) {
        this.userMeta = userMeta;
        return this;
    }
    public String getUserMeta() {
        return this.userMeta;
    }

    public UCCompleteFileResponse setUserTags(java.util.Map<String, ?> userTags) {
        this.userTags = userTags;
        return this;
    }
    public java.util.Map<String, ?> getUserTags() {
        return this.userTags;
    }

    public UCCompleteFileResponse setVideoMediaMetadata(VideoMediaResponse videoMediaMetadata) {
        this.videoMediaMetadata = videoMediaMetadata;
        return this;
    }
    public VideoMediaResponse getVideoMediaMetadata() {
        return this.videoMediaMetadata;
    }

    public UCCompleteFileResponse setVideoPreviewMetadata(VideoPreviewResponse videoPreviewMetadata) {
        this.videoPreviewMetadata = videoPreviewMetadata;
        return this;
    }
    public VideoPreviewResponse getVideoPreviewMetadata() {
        return this.videoPreviewMetadata;
    }

}
