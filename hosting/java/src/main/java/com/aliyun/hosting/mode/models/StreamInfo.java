// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.hosting.mode.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class StreamInfo extends TeaModel {
    // crc64_hash
    @NameInMap("crc64_hash")
    public String crc64Hash;

    // download_url
    @NameInMap("download_url")
    public String downloadUrl;

    // thumbnail
    @NameInMap("thumbnail")
    public String thumbnail;

    // url
    @NameInMap("url")
    public String url;

    public static StreamInfo build(java.util.Map<String, ?> map) throws Exception {
        StreamInfo self = new StreamInfo();
        return TeaModel.build(map, self);
    }

    public StreamInfo setCrc64Hash(String crc64Hash) {
        this.crc64Hash = crc64Hash;
        return this;
    }
    public String getCrc64Hash() {
        return this.crc64Hash;
    }

    public StreamInfo setDownloadUrl(String downloadUrl) {
        this.downloadUrl = downloadUrl;
        return this;
    }
    public String getDownloadUrl() {
        return this.downloadUrl;
    }

    public StreamInfo setThumbnail(String thumbnail) {
        this.thumbnail = thumbnail;
        return this;
    }
    public String getThumbnail() {
        return this.thumbnail;
    }

    public StreamInfo setUrl(String url) {
        this.url = url;
        return this;
    }
    public String getUrl() {
        return this.url;
    }

}
