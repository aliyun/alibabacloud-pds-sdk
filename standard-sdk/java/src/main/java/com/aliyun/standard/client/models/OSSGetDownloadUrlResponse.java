// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.standard.client.models;

import com.aliyun.tea.*;

/**
 * 获取download url response
 */
public class OSSGetDownloadUrlResponse extends TeaModel {
    // expiration
    @NameInMap("expiration")
    public String expiration;

    // method
    @NameInMap("method")
    public String method;

    // url
    @NameInMap("url")
    public String url;

    public static OSSGetDownloadUrlResponse build(java.util.Map<String, ?> map) throws Exception {
        OSSGetDownloadUrlResponse self = new OSSGetDownloadUrlResponse();
        return TeaModel.build(map, self);
    }

    public OSSGetDownloadUrlResponse setExpiration(String expiration) {
        this.expiration = expiration;
        return this;
    }
    public String getExpiration() {
        return this.expiration;
    }

    public OSSGetDownloadUrlResponse setMethod(String method) {
        this.method = method;
        return this;
    }
    public String getMethod() {
        return this.method;
    }

    public OSSGetDownloadUrlResponse setUrl(String url) {
        this.url = url;
        return this;
    }
    public String getUrl() {
        return this.url;
    }

}
