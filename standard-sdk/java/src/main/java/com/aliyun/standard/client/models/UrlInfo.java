// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.standard.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class UrlInfo extends TeaModel {
    // download_url
    @NameInMap("download_url")
    public String downloadUrl;

    // thumbnail
    @NameInMap("thumbnail")
    public String thumbnail;

    // url
    @NameInMap("url")
    public String url;

    public static UrlInfo build(java.util.Map<String, ?> map) throws Exception {
        UrlInfo self = new UrlInfo();
        return TeaModel.build(map, self);
    }

    public UrlInfo setDownloadUrl(String downloadUrl) {
        this.downloadUrl = downloadUrl;
        return this;
    }
    public String getDownloadUrl() {
        return this.downloadUrl;
    }

    public UrlInfo setThumbnail(String thumbnail) {
        this.thumbnail = thumbnail;
        return this;
    }
    public String getThumbnail() {
        return this.thumbnail;
    }

    public UrlInfo setUrl(String url) {
        this.url = url;
        return this;
    }
    public String getUrl() {
        return this.url;
    }

}
