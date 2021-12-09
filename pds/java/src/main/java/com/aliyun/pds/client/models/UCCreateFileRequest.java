// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * UCCreateFileRequest create file with signature
 */
public class UCCreateFileRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    // addition_data
    @NameInMap("addition_data")
    public java.util.Map<String, ?> additionData;

    @NameInMap("auto_rename")
    public Boolean autoRename;

    @NameInMap("callback")
    public CcpCallback callback;

    // check_name_mode
    @NameInMap("check_name_mode")
    public String checkNameMode;

    // content_hash
    @NameInMap("content_hash")
    public String contentHash;

    // content_hash_mutable
    @NameInMap("content_hash_mutable")
    public Boolean contentHashMutable;

    // content_hash_name
    @NameInMap("content_hash_name")
    public String contentHashName;

    // ContentMd5
    @NameInMap("content_md5")
    public String contentMd5;

    // ContentType
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

    // date
    @NameInMap("date")
    public String date;

    // description
    @NameInMap("description")
    @Validation(maxLength = 1024)
    public String description;

    // drive_id
    @NameInMap("drive_id")
    @Validation(pattern = "[0-9]+")
    public String driveId;

    // encrypt_mode
    @NameInMap("encrypt_mode")
    public String encryptMode;

    // file_id
    @NameInMap("file_id")
    public String fileId;

    // force_upload_to_location
    @NameInMap("force_upload_to_location")
    public Boolean forceUploadToLocation;

    // headers
    @NameInMap("headers")
    public java.util.Map<String, ?> headers;

    // hidden
    @NameInMap("hidden")
    public Boolean hidden;

    @NameInMap("image_media_metadata")
    public ImageMediaMetadata imageMediaMetadata;

    // labels
    @NameInMap("labels")
    public java.util.List<String> labels;

    // last_updated_at
    @NameInMap("last_updated_at")
    public String lastUpdatedAt;

    // local_created_at
    @NameInMap("local_created_at")
    public String localCreatedAt;

    // location
    @NameInMap("location")
    public String location;

    @NameInMap("meta")
    public String meta;

    // Name
    @NameInMap("name")
    @Validation(required = true, maxLength = 1024, minLength = 1)
    public String name;

    // overwrite
    @NameInMap("overwrite")
    public Boolean overwrite;

    @NameInMap("parallel_upload")
    public Boolean parallelUpload;

    // parameters
    @NameInMap("parameters")
    public java.util.Map<String, ?> parameters;

    // parent_file_id
    @NameInMap("parent_file_id")
    @Validation(required = true, pattern = "[a-z0-9]{1,50}", maxLength = 50, minLength = 4)
    public String parentFileId;

    @NameInMap("parent_file_id_path")
    public String parentFileIdPath;

    // part_info_list
    @NameInMap("part_info_list")
    public java.util.List<UploadPartInfo> partInfoList;

    // pre_hash
    @NameInMap("pre_hash")
    public String preHash;

    // proof_code
    @NameInMap("proof_code")
    public String proofCode;

    // proof_version
    @NameInMap("proof_version")
    public String proofVersion;

    // share_id
    // example
    @NameInMap("share_id")
    public String shareId;

    // Size
    @NameInMap("size")
    public Long size;

    // streams_info
    @NameInMap("streams_info")
    public java.util.Map<String, ?> streamsInfo;

    // Type
    @NameInMap("type")
    @Validation(required = true)
    public String type;

    // upload_type
    @NameInMap("upload_type")
    public String uploadType;

    // user_meta
    @NameInMap("user_meta")
    public String userMeta;

    // user_tags
    @NameInMap("user_tags")
    public java.util.List<UserTag> userTags;

    @NameInMap("video_media_metadata")
    public VideoMediaMetadata videoMediaMetadata;

    public static UCCreateFileRequest build(java.util.Map<String, ?> map) throws Exception {
        UCCreateFileRequest self = new UCCreateFileRequest();
        return TeaModel.build(map, self);
    }

    public UCCreateFileRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
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

    public UCCreateFileRequest setCheckNameMode(String checkNameMode) {
        this.checkNameMode = checkNameMode;
        return this;
    }
    public String getCheckNameMode() {
        return this.checkNameMode;
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
