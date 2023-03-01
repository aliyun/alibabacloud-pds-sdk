// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 获取download url response
 */
public class GetDownloadUrlResponse extends TeaModel {
    /**
     * <p>cdn_url</p>
     */
    @NameInMap("cdn_url")
    public String cdnUrl;

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
     * <p>crc64_hash</p>
     */
    @NameInMap("crc64_hash")
    public String crc64Hash;

    /**
     * <p>DomainID</p>
     */
    @NameInMap("domain_id")
    @Validation(pattern = "[a-z0-9A-Z]+")
    public String domainId;

    /**
     * <p>drive_id</p>
     */
    @NameInMap("drive_id")
    @Validation(pattern = "[0-9]+")
    public String driveId;

    /**
     * <p>expiration</p>
     */
    @NameInMap("expiration")
    public String expiration;

    /**
     * <p>file_id</p>
     */
    @NameInMap("file_id")
    @Validation(pattern = "[a-z0-9]{1,50}", maxLength = 50, minLength = 40)
    public String fileId;

    /**
     * <p>internal_url</p>
     */
    @NameInMap("internal_url")
    public String internalUrl;

    /**
     * <p>method</p>
     */
    @NameInMap("method")
    public String method;

    /**
     * <p>PunishFlag</p>
     */
    @NameInMap("punish_flag")
    public Long punishFlag;

    /**
     * <p>revision_id</p>
     */
    @NameInMap("revision_id")
    public String revisionId;

    /**
     * <p>size</p>
     */
    @NameInMap("size")
    public Long size;

    /**
     * <p>streams info</p>
     */
    @NameInMap("streams_info")
    public java.util.Map<String, ?> streamsInfo;

    /**
     * <p>streams url info</p>
     */
    @NameInMap("streams_url")
    public java.util.Map<String, ?> streamsUrl;

    /**
     * <p>url</p>
     */
    @NameInMap("url")
    public String url;

    public static GetDownloadUrlResponse build(java.util.Map<String, ?> map) throws Exception {
        GetDownloadUrlResponse self = new GetDownloadUrlResponse();
        return TeaModel.build(map, self);
    }

    public GetDownloadUrlResponse setCdnUrl(String cdnUrl) {
        this.cdnUrl = cdnUrl;
        return this;
    }
    public String getCdnUrl() {
        return this.cdnUrl;
    }

    public GetDownloadUrlResponse setContentHash(String contentHash) {
        this.contentHash = contentHash;
        return this;
    }
    public String getContentHash() {
        return this.contentHash;
    }

    public GetDownloadUrlResponse setContentHashName(String contentHashName) {
        this.contentHashName = contentHashName;
        return this;
    }
    public String getContentHashName() {
        return this.contentHashName;
    }

    public GetDownloadUrlResponse setCrc64Hash(String crc64Hash) {
        this.crc64Hash = crc64Hash;
        return this;
    }
    public String getCrc64Hash() {
        return this.crc64Hash;
    }

    public GetDownloadUrlResponse setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

    public GetDownloadUrlResponse setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public GetDownloadUrlResponse setExpiration(String expiration) {
        this.expiration = expiration;
        return this;
    }
    public String getExpiration() {
        return this.expiration;
    }

    public GetDownloadUrlResponse setFileId(String fileId) {
        this.fileId = fileId;
        return this;
    }
    public String getFileId() {
        return this.fileId;
    }

    public GetDownloadUrlResponse setInternalUrl(String internalUrl) {
        this.internalUrl = internalUrl;
        return this;
    }
    public String getInternalUrl() {
        return this.internalUrl;
    }

    public GetDownloadUrlResponse setMethod(String method) {
        this.method = method;
        return this;
    }
    public String getMethod() {
        return this.method;
    }

    public GetDownloadUrlResponse setPunishFlag(Long punishFlag) {
        this.punishFlag = punishFlag;
        return this;
    }
    public Long getPunishFlag() {
        return this.punishFlag;
    }

    public GetDownloadUrlResponse setRevisionId(String revisionId) {
        this.revisionId = revisionId;
        return this;
    }
    public String getRevisionId() {
        return this.revisionId;
    }

    public GetDownloadUrlResponse setSize(Long size) {
        this.size = size;
        return this;
    }
    public Long getSize() {
        return this.size;
    }

    public GetDownloadUrlResponse setStreamsInfo(java.util.Map<String, ?> streamsInfo) {
        this.streamsInfo = streamsInfo;
        return this;
    }
    public java.util.Map<String, ?> getStreamsInfo() {
        return this.streamsInfo;
    }

    public GetDownloadUrlResponse setStreamsUrl(java.util.Map<String, ?> streamsUrl) {
        this.streamsUrl = streamsUrl;
        return this;
    }
    public java.util.Map<String, ?> getStreamsUrl() {
        return this.streamsUrl;
    }

    public GetDownloadUrlResponse setUrl(String url) {
        this.url = url;
        return this;
    }
    public String getUrl() {
        return this.url;
    }

}
