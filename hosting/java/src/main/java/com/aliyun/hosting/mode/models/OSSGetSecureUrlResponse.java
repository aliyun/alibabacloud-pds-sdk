// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.hosting.mode.models;

import com.aliyun.tea.*;

/**
 * 获取secure url response
 */
public class OSSGetSecureUrlResponse extends TeaModel {
    // expiration
    @NameInMap("expiration")
    public String expiration;

    // url
    @NameInMap("url")
    public String url;

    public static OSSGetSecureUrlResponse build(java.util.Map<String, ?> map) throws Exception {
        OSSGetSecureUrlResponse self = new OSSGetSecureUrlResponse();
        return TeaModel.build(map, self);
    }

    public OSSGetSecureUrlResponse setExpiration(String expiration) {
        this.expiration = expiration;
        return this;
    }
    public String getExpiration() {
        return this.expiration;
    }

    public OSSGetSecureUrlResponse setUrl(String url) {
        this.url = url;
        return this;
    }
    public String getUrl() {
        return this.url;
    }

}
