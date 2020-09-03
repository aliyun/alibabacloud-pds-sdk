// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.hosting.mode.models;

import com.aliyun.tea.*;

/**
 * 获取download url response
 */
public class GetDownloadUrlResponse extends TeaModel {
    // expiration
    @NameInMap("expiration")
    public String expiration;

    // method
    @NameInMap("method")
    public String method;

    @NameInMap("ratelimit")
    public RateLimit ratelimit;

    // size
    @NameInMap("size")
    public Long size;

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

    public GetDownloadUrlResponse setExpiration(String expiration) {
        this.expiration = expiration;
        return this;
    }
    public String getExpiration() {
        return this.expiration;
    }

    public GetDownloadUrlResponse setMethod(String method) {
        this.method = method;
        return this;
    }
    public String getMethod() {
        return this.method;
    }

    public GetDownloadUrlResponse setRatelimit(RateLimit ratelimit) {
        this.ratelimit = ratelimit;
        return this;
    }
    public RateLimit getRatelimit() {
        return this.ratelimit;
    }

    public GetDownloadUrlResponse setSize(Long size) {
        this.size = size;
        return this;
    }
    public Long getSize() {
        return this.size;
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
