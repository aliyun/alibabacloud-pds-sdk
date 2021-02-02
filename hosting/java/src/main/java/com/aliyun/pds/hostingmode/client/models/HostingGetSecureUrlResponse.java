// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.hostingmode.client.models;

import com.aliyun.tea.*;

/**
 * 获取secure url response
 */
public class HostingGetSecureUrlResponse extends TeaModel {
    // expiration
    @NameInMap("expiration")
    public String expiration;

    // url
    @NameInMap("url")
    public String url;

    public static HostingGetSecureUrlResponse build(java.util.Map<String, ?> map) throws Exception {
        HostingGetSecureUrlResponse self = new HostingGetSecureUrlResponse();
        return TeaModel.build(map, self);
    }

    public HostingGetSecureUrlResponse setExpiration(String expiration) {
        this.expiration = expiration;
        return this;
    }
    public String getExpiration() {
        return this.expiration;
    }

    public HostingGetSecureUrlResponse setUrl(String url) {
        this.url = url;
        return this;
    }
    public String getUrl() {
        return this.url;
    }

}
