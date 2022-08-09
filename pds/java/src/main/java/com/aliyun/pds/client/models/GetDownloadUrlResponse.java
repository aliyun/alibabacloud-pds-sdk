// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 获取download url response
 */
public class GetDownloadUrlResponse extends TeaModel {
    // cdn_url
    @NameInMap("cdn_url")
    public String cdnUrl;

    // Content Hash
    @NameInMap("content_hash")
    public String contentHash;

    // content_hash_name
    @NameInMap("content_hash_name")
    public String contentHashName;

    // crc64_hash
    @NameInMap("crc64_hash")
    public String crc64Hash;

    // expiration
    @NameInMap("expiration")
    public String expiration;

    // internal_url
    @NameInMap("internal_url")
    public String internalUrl;

    // method
    @NameInMap("method")
    public String method;

    // PunishFlag
    @NameInMap("punish_flag")
    public Long punishFlag;

    // size
    @NameInMap("size")
    public Long size;

    // streams info
    @NameInMap("streams_info")
    public java.util.Map<String, ?> streamsInfo;

    // streams url info
    @NameInMap("streams_url")
    public java.util.Map<String, ?> streamsUrl;

    // url
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

    public GetDownloadUrlResponse setExpiration(String expiration) {
        this.expiration = expiration;
        return this;
    }
    public String getExpiration() {
        return this.expiration;
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
