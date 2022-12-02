// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 获取版本response
 */
public class GetRevisionResponse extends TeaModel {
    // Content Hash
    @NameInMap("content_hash")
    public String contentHash;

    // content_hash_name
    @NameInMap("content_hash_name")
    public String contentHashName;

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

    // file_extension
    @NameInMap("file_extension")
    public String fileExtension;

    // file_id
    @NameInMap("file_id")
    @Validation(pattern = "[a-z0-9]{1,50}", maxLength = 50, minLength = 40)
    public String fileId;

    // is_latest_version
    // type: boolean
    @NameInMap("is_latest_version")
    public Boolean isLatestVersion;

    // keep_forever
    // type: boolean
    @NameInMap("keep_forever")
    public Boolean keepForever;

    // revision_create_reason
    // type: string
    @NameInMap("revision_create_reason")
    @Validation(maxLength = 1024)
    public String revisionCreateReason;

    // revision_description
    // type: string
    @NameInMap("revision_description")
    @Validation(maxLength = 1024)
    public String revisionDescription;

    // revision_id
    @NameInMap("revision_id")
    @Validation(pattern = "[a-z0-9]{1,50}", maxLength = 50, minLength = 40)
    public String revisionId;

    // revision_name
    // name
    @NameInMap("revision_name")
    @Validation(pattern = "[a-zA-Z0-9.-]{1,1000}")
    public String revisionName;

    // revision_version
    @NameInMap("revision_version")
    public Long revisionVersion;

    // Size
    @NameInMap("size")
    public Long size;

    // @Deprecated streams url info
    @NameInMap("streams_info")
    public java.util.Map<String, ?> streamsInfo;

    // thumbnail
    @NameInMap("thumbnail")
    public String thumbnail;

    // updated_at
    @NameInMap("updated_at")
    public String updatedAt;

    // url
    @NameInMap("url")
    public String url;

    public static GetRevisionResponse build(java.util.Map<String, ?> map) throws Exception {
        GetRevisionResponse self = new GetRevisionResponse();
        return TeaModel.build(map, self);
    }

    public GetRevisionResponse setContentHash(String contentHash) {
        this.contentHash = contentHash;
        return this;
    }
    public String getContentHash() {
        return this.contentHash;
    }

    public GetRevisionResponse setContentHashName(String contentHashName) {
        this.contentHashName = contentHashName;
        return this;
    }
    public String getContentHashName() {
        return this.contentHashName;
    }

    public GetRevisionResponse setCrc64Hash(String crc64Hash) {
        this.crc64Hash = crc64Hash;
        return this;
    }
    public String getCrc64Hash() {
        return this.crc64Hash;
    }

    public GetRevisionResponse setCreatedAt(String createdAt) {
        this.createdAt = createdAt;
        return this;
    }
    public String getCreatedAt() {
        return this.createdAt;
    }

    public GetRevisionResponse setCreatorId(String creatorId) {
        this.creatorId = creatorId;
        return this;
    }
    public String getCreatorId() {
        return this.creatorId;
    }

    public GetRevisionResponse setCreatorName(String creatorName) {
        this.creatorName = creatorName;
        return this;
    }
    public String getCreatorName() {
        return this.creatorName;
    }

    public GetRevisionResponse setCreatorType(String creatorType) {
        this.creatorType = creatorType;
        return this;
    }
    public String getCreatorType() {
        return this.creatorType;
    }

    public GetRevisionResponse setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

    public GetRevisionResponse setDownloadUrl(String downloadUrl) {
        this.downloadUrl = downloadUrl;
        return this;
    }
    public String getDownloadUrl() {
        return this.downloadUrl;
    }

    public GetRevisionResponse setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public GetRevisionResponse setFileExtension(String fileExtension) {
        this.fileExtension = fileExtension;
        return this;
    }
    public String getFileExtension() {
        return this.fileExtension;
    }

    public GetRevisionResponse setFileId(String fileId) {
        this.fileId = fileId;
        return this;
    }
    public String getFileId() {
        return this.fileId;
    }

    public GetRevisionResponse setIsLatestVersion(Boolean isLatestVersion) {
        this.isLatestVersion = isLatestVersion;
        return this;
    }
    public Boolean getIsLatestVersion() {
        return this.isLatestVersion;
    }

    public GetRevisionResponse setKeepForever(Boolean keepForever) {
        this.keepForever = keepForever;
        return this;
    }
    public Boolean getKeepForever() {
        return this.keepForever;
    }

    public GetRevisionResponse setRevisionCreateReason(String revisionCreateReason) {
        this.revisionCreateReason = revisionCreateReason;
        return this;
    }
    public String getRevisionCreateReason() {
        return this.revisionCreateReason;
    }

    public GetRevisionResponse setRevisionDescription(String revisionDescription) {
        this.revisionDescription = revisionDescription;
        return this;
    }
    public String getRevisionDescription() {
        return this.revisionDescription;
    }

    public GetRevisionResponse setRevisionId(String revisionId) {
        this.revisionId = revisionId;
        return this;
    }
    public String getRevisionId() {
        return this.revisionId;
    }

    public GetRevisionResponse setRevisionName(String revisionName) {
        this.revisionName = revisionName;
        return this;
    }
    public String getRevisionName() {
        return this.revisionName;
    }

    public GetRevisionResponse setRevisionVersion(Long revisionVersion) {
        this.revisionVersion = revisionVersion;
        return this;
    }
    public Long getRevisionVersion() {
        return this.revisionVersion;
    }

    public GetRevisionResponse setSize(Long size) {
        this.size = size;
        return this;
    }
    public Long getSize() {
        return this.size;
    }

    public GetRevisionResponse setStreamsInfo(java.util.Map<String, ?> streamsInfo) {
        this.streamsInfo = streamsInfo;
        return this;
    }
    public java.util.Map<String, ?> getStreamsInfo() {
        return this.streamsInfo;
    }

    public GetRevisionResponse setThumbnail(String thumbnail) {
        this.thumbnail = thumbnail;
        return this;
    }
    public String getThumbnail() {
        return this.thumbnail;
    }

    public GetRevisionResponse setUpdatedAt(String updatedAt) {
        this.updatedAt = updatedAt;
        return this;
    }
    public String getUpdatedAt() {
        return this.updatedAt;
    }

    public GetRevisionResponse setUrl(String url) {
        this.url = url;
        return this;
    }
    public String getUrl() {
        return this.url;
    }

}