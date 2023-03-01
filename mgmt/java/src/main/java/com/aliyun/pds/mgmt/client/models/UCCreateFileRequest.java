// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * UCCreateFileRequest create file with signature
 */
public class UCCreateFileRequest extends TeaModel {
    /**
     * <p>addition_data</p>
     */
    @NameInMap("addition_data")
    public java.util.Map<String, ?> additionData;

    @NameInMap("auto_rename")
    public Boolean autoRename;

    @NameInMap("callback")
    public CcpCallback callback;

    /**
     * <p>category</p>
     */
    @NameInMap("category")
    public String category;

    /**
     * <p>check_name_mode</p>
     */
    @NameInMap("check_name_mode")
    public String checkNameMode;

    @NameInMap("check_parent_file_id_path")
    public String checkParentFileIdPath;

    /**
     * <p>content_hash</p>
     */
    @NameInMap("content_hash")
    public String contentHash;

    /**
     * <p>content_hash_mutable</p>
     */
    @NameInMap("content_hash_mutable")
    public Boolean contentHashMutable;

    /**
     * <p>content_hash_name</p>
     */
    @NameInMap("content_hash_name")
    public String contentHashName;

    /**
     * <p>ContentMd5</p>
     */
    @NameInMap("content_md5")
    public String contentMd5;

    /**
     * <p>ContentType</p>
     */
    @NameInMap("content_type")
    public String contentType;

    @NameInMap("create_reason")
    public String createReason;

    @NameInMap("custom_field_1")
    public String customField1;

    @NameInMap("custom_field_2")
    public String customField2;

    @NameInMap("custom_type")
    public String customType;

    /**
     * <p>date</p>
     */
    @NameInMap("date")
    public String date;

    /**
     * <p>description</p>
     */
    @NameInMap("description")
    @Validation(maxLength = 1024)
    public String description;

    /**
     * <p>drive_id</p>
     */
    @NameInMap("drive_id")
    @Validation(pattern = "[0-9]+")
    public String driveId;

    @NameInMap("encrypt_mode")
    public String encryptMode;

    /**
     * <p>file_id</p>
     */
    @NameInMap("file_id")
    public String fileId;

    /**
     * <p>force_upload_to_location</p>
     */
    @NameInMap("force_upload_to_location")
    public Boolean forceUploadToLocation;

    /**
     * <p>headers</p>
     */
    @NameInMap("headers")
    public java.util.Map<String, ?> headers;

    /**
     * <p>hidden</p>
     */
    @NameInMap("hidden")
    public Boolean hidden;

    @NameInMap("image_media_metadata")
    public ImageMediaMetadata imageMediaMetadata;

    /**
     * <p>labels</p>
     */
    @NameInMap("labels")
    public java.util.List<String> labels;

    @NameInMap("last_revision_id")
    public String lastRevisionId;

    /**
     * <p>last_updated_at</p>
     */
    @NameInMap("last_updated_at")
    public String lastUpdatedAt;

    /**
     * <p>local_created_at</p>
     */
    @NameInMap("local_created_at")
    public String localCreatedAt;

    @NameInMap("local_modified_at")
    public String localModifiedAt;

    /**
     * <p>location</p>
     */
    @NameInMap("location")
    public String location;

    @NameInMap("meta")
    public String meta;

    /**
     * <p>Name</p>
     */
    @NameInMap("name")
    @Validation(required = true, maxLength = 1024, minLength = 1)
    public String name;

    @NameInMap("need_merge_period_revision")
    public Boolean needMergePeriodRevision;

    /**
     * <p>overwrite</p>
     */
    @NameInMap("overwrite")
    public Boolean overwrite;

    @NameInMap("parallel_upload")
    public Boolean parallelUpload;

    /**
     * <p>parameters</p>
     */
    @NameInMap("parameters")
    public java.util.Map<String, ?> parameters;

    /**
     * <p>parent_file_id</p>
     */
    @NameInMap("parent_file_id")
    @Validation(required = true, pattern = "[a-z0-9]{1,50}", maxLength = 50, minLength = 4)
    public String parentFileId;

    @NameInMap("parent_file_id_path")
    public String parentFileIdPath;

    /**
     * <p>part_info_list</p>
     */
    @NameInMap("part_info_list")
    public java.util.List<UploadPartInfo> partInfoList;

    /**
     * <p>pre_hash</p>
     */
    @NameInMap("pre_hash")
    public String preHash;

    /**
     * <p>proof_code</p>
     */
    @NameInMap("proof_code")
    public String proofCode;

    /**
     * <p>proof_seed</p>
     */
    @NameInMap("proof_seed")
    public String proofSeed;

    /**
     * <p>proof_version</p>
     */
    @NameInMap("proof_version")
    public String proofVersion;

    /**
     * <p>share_id</p>
     * <p>example</p>
     */
    @NameInMap("share_id")
    public String shareId;

    /**
     * <p>Size</p>
     */
    @NameInMap("size")
    public Long size;

    /**
     * <p>streams_info</p>
     */
    @NameInMap("streams_info")
    public java.util.Map<String, ?> streamsInfo;

    /**
     * <p>Type</p>
     */
    @NameInMap("type")
    @Validation(required = true)
    public String type;

    /**
     * <p>upload_type</p>
     */
    @NameInMap("upload_type")
    public String uploadType;

    /**
     * <p>user_meta</p>
     */
    @NameInMap("user_meta")
    public String userMeta;

    /**
     * <p>user_tags</p>
     */
    @NameInMap("user_tags")
    public java.util.List<UserTag> userTags;

    @NameInMap("video_media_metadata")
    public VideoMediaMetadata videoMediaMetadata;

    public static UCCreateFileRequest build(java.util.Map<String, ?> map) throws Exception {
        UCCreateFileRequest self = new UCCreateFileRequest();
        return TeaModel.build(map, self);
    }

    public UCCreateFileRequest setAdditionData(java.util.Map<String, ?> additionData) {
        this.additionData = additionData;
        return this;
    }
    public java.util.Map<String, ?> getAdditionData() {
        return this.additionData;
    }

    public UCCreateFileRequest setAutoRename(Boolean autoRename) {
        this.autoRename = autoRename;
        return this;
    }
    public Boolean getAutoRename() {
        return this.autoRename;
    }

    public UCCreateFileRequest setCallback(CcpCallback callback) {
        this.callback = callback;
        return this;
    }
    public CcpCallback getCallback() {
        return this.callback;
    }

    public UCCreateFileRequest setCategory(String category) {
        this.category = category;
        return this;
    }
    public String getCategory() {
        return this.category;
    }

    public UCCreateFileRequest setCheckNameMode(String checkNameMode) {
        this.checkNameMode = checkNameMode;
        return this;
    }
    public String getCheckNameMode() {
        return this.checkNameMode;
    }

    public UCCreateFileRequest setCheckParentFileIdPath(String checkParentFileIdPath) {
        this.checkParentFileIdPath = checkParentFileIdPath;
        return this;
    }
    public String getCheckParentFileIdPath() {
        return this.checkParentFileIdPath;
    }

    public UCCreateFileRequest setContentHash(String contentHash) {
        this.contentHash = contentHash;
        return this;
    }
    public String getContentHash() {
        return this.contentHash;
    }

    public UCCreateFileRequest setContentHashMutable(Boolean contentHashMutable) {
        this.contentHashMutable = contentHashMutable;
        return this;
    }
    public Boolean getContentHashMutable() {
        return this.contentHashMutable;
    }

    public UCCreateFileRequest setContentHashName(String contentHashName) {
        this.contentHashName = contentHashName;
        return this;
    }
    public String getContentHashName() {
        return this.contentHashName;
    }

    public UCCreateFileRequest setContentMd5(String contentMd5) {
        this.contentMd5 = contentMd5;
        return this;
    }
    public String getContentMd5() {
        return this.contentMd5;
    }

    public UCCreateFileRequest setContentType(String contentType) {
        this.contentType = contentType;
        return this;
    }
    public String getContentType() {
        return this.contentType;
    }

    public UCCreateFileRequest setCreateReason(String createReason) {
        this.createReason = createReason;
        return this;
    }
    public String getCreateReason() {
        return this.createReason;
    }

    public UCCreateFileRequest setCustomField1(String customField1) {
        this.customField1 = customField1;
        return this;
    }
    public String getCustomField1() {
        return this.customField1;
    }

    public UCCreateFileRequest setCustomField2(String customField2) {
        this.customField2 = customField2;
        return this;
    }
    public String getCustomField2() {
        return this.customField2;
    }

    public UCCreateFileRequest setCustomType(String customType) {
        this.customType = customType;
        return this;
    }
    public String getCustomType() {
        return this.customType;
    }

    public UCCreateFileRequest setDate(String date) {
        this.date = date;
        return this;
    }
    public String getDate() {
        return this.date;
    }

    public UCCreateFileRequest setDescription(String description) {
        this.description = description;
        return this;
    }
    public String getDescription() {
        return this.description;
    }

    public UCCreateFileRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public UCCreateFileRequest setEncryptMode(String encryptMode) {
        this.encryptMode = encryptMode;
        return this;
    }
    public String getEncryptMode() {
        return this.encryptMode;
    }

    public UCCreateFileRequest setFileId(String fileId) {
        this.fileId = fileId;
        return this;
    }
    public String getFileId() {
        return this.fileId;
    }

    public UCCreateFileRequest setForceUploadToLocation(Boolean forceUploadToLocation) {
        this.forceUploadToLocation = forceUploadToLocation;
        return this;
    }
    public Boolean getForceUploadToLocation() {
        return this.forceUploadToLocation;
    }

    public UCCreateFileRequest setHeaders(java.util.Map<String, ?> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, ?> getHeaders() {
        return this.headers;
    }

    public UCCreateFileRequest setHidden(Boolean hidden) {
        this.hidden = hidden;
        return this;
    }
    public Boolean getHidden() {
        return this.hidden;
    }

    public UCCreateFileRequest setImageMediaMetadata(ImageMediaMetadata imageMediaMetadata) {
        this.imageMediaMetadata = imageMediaMetadata;
        return this;
    }
    public ImageMediaMetadata getImageMediaMetadata() {
        return this.imageMediaMetadata;
    }

    public UCCreateFileRequest setLabels(java.util.List<String> labels) {
        this.labels = labels;
        return this;
    }
    public java.util.List<String> getLabels() {
        return this.labels;
    }

    public UCCreateFileRequest setLastRevisionId(String lastRevisionId) {
        this.lastRevisionId = lastRevisionId;
        return this;
    }
    public String getLastRevisionId() {
        return this.lastRevisionId;
    }

    public UCCreateFileRequest setLastUpdatedAt(String lastUpdatedAt) {
        this.lastUpdatedAt = lastUpdatedAt;
        return this;
    }
    public String getLastUpdatedAt() {
        return this.lastUpdatedAt;
    }

    public UCCreateFileRequest setLocalCreatedAt(String localCreatedAt) {
        this.localCreatedAt = localCreatedAt;
        return this;
    }
    public String getLocalCreatedAt() {
        return this.localCreatedAt;
    }

    public UCCreateFileRequest setLocalModifiedAt(String localModifiedAt) {
        this.localModifiedAt = localModifiedAt;
        return this;
    }
    public String getLocalModifiedAt() {
        return this.localModifiedAt;
    }

    public UCCreateFileRequest setLocation(String location) {
        this.location = location;
        return this;
    }
    public String getLocation() {
        return this.location;
    }

    public UCCreateFileRequest setMeta(String meta) {
        this.meta = meta;
        return this;
    }
    public String getMeta() {
        return this.meta;
    }

    public UCCreateFileRequest setName(String name) {
        this.name = name;
        return this;
    }
    public String getName() {
        return this.name;
    }

    public UCCreateFileRequest setNeedMergePeriodRevision(Boolean needMergePeriodRevision) {
        this.needMergePeriodRevision = needMergePeriodRevision;
        return this;
    }
    public Boolean getNeedMergePeriodRevision() {
        return this.needMergePeriodRevision;
    }

    public UCCreateFileRequest setOverwrite(Boolean overwrite) {
        this.overwrite = overwrite;
        return this;
    }
    public Boolean getOverwrite() {
        return this.overwrite;
    }

    public UCCreateFileRequest setParallelUpload(Boolean parallelUpload) {
        this.parallelUpload = parallelUpload;
        return this;
    }
    public Boolean getParallelUpload() {
        return this.parallelUpload;
    }

    public UCCreateFileRequest setParameters(java.util.Map<String, ?> parameters) {
        this.parameters = parameters;
        return this;
    }
    public java.util.Map<String, ?> getParameters() {
        return this.parameters;
    }

    public UCCreateFileRequest setParentFileId(String parentFileId) {
        this.parentFileId = parentFileId;
        return this;
    }
    public String getParentFileId() {
        return this.parentFileId;
    }

    public UCCreateFileRequest setParentFileIdPath(String parentFileIdPath) {
        this.parentFileIdPath = parentFileIdPath;
        return this;
    }
    public String getParentFileIdPath() {
        return this.parentFileIdPath;
    }

    public UCCreateFileRequest setPartInfoList(java.util.List<UploadPartInfo> partInfoList) {
        this.partInfoList = partInfoList;
        return this;
    }
    public java.util.List<UploadPartInfo> getPartInfoList() {
        return this.partInfoList;
    }

    public UCCreateFileRequest setPreHash(String preHash) {
        this.preHash = preHash;
        return this;
    }
    public String getPreHash() {
        return this.preHash;
    }

    public UCCreateFileRequest setProofCode(String proofCode) {
        this.proofCode = proofCode;
        return this;
    }
    public String getProofCode() {
        return this.proofCode;
    }

    public UCCreateFileRequest setProofSeed(String proofSeed) {
        this.proofSeed = proofSeed;
        return this;
    }
    public String getProofSeed() {
        return this.proofSeed;
    }

    public UCCreateFileRequest setProofVersion(String proofVersion) {
        this.proofVersion = proofVersion;
        return this;
    }
    public String getProofVersion() {
        return this.proofVersion;
    }

    public UCCreateFileRequest setShareId(String shareId) {
        this.shareId = shareId;
        return this;
    }
    public String getShareId() {
        return this.shareId;
    }

    public UCCreateFileRequest setSize(Long size) {
        this.size = size;
        return this;
    }
    public Long getSize() {
        return this.size;
    }

    public UCCreateFileRequest setStreamsInfo(java.util.Map<String, ?> streamsInfo) {
        this.streamsInfo = streamsInfo;
        return this;
    }
    public java.util.Map<String, ?> getStreamsInfo() {
        return this.streamsInfo;
    }

    public UCCreateFileRequest setType(String type) {
        this.type = type;
        return this;
    }
    public String getType() {
        return this.type;
    }

    public UCCreateFileRequest setUploadType(String uploadType) {
        this.uploadType = uploadType;
        return this;
    }
    public String getUploadType() {
        return this.uploadType;
    }

    public UCCreateFileRequest setUserMeta(String userMeta) {
        this.userMeta = userMeta;
        return this;
    }
    public String getUserMeta() {
        return this.userMeta;
    }

    public UCCreateFileRequest setUserTags(java.util.List<UserTag> userTags) {
        this.userTags = userTags;
        return this;
    }
    public java.util.List<UserTag> getUserTags() {
        return this.userTags;
    }

    public UCCreateFileRequest setVideoMediaMetadata(VideoMediaMetadata videoMediaMetadata) {
        this.videoMediaMetadata = videoMediaMetadata;
        return this;
    }
    public VideoMediaMetadata getVideoMediaMetadata() {
        return this.videoMediaMetadata;
    }

}
