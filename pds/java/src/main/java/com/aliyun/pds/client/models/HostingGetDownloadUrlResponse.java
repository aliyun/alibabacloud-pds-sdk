// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 获取download url response
 */
public class HostingGetDownloadUrlResponse extends TeaModel {
    /**
     * <p>expiration</p>
     */
    @NameInMap("expiration")
    public String expiration;

    /**
     * <p>method</p>
     */
    @NameInMap("method")
    public String method;

    /**
     * <p>url</p>
     */
    @NameInMap("url")
    public String url;

    public static HostingGetDownloadUrlResponse build(java.util.Map<String, ?> map) throws Exception {
        HostingGetDownloadUrlResponse self = new HostingGetDownloadUrlResponse();
        return TeaModel.build(map, self);
    }

    public HostingGetDownloadUrlResponse setExpiration(String expiration) {
        this.expiration = expiration;
        return this;
    }
    public String getExpiration() {
        return this.expiration;
    }

    public HostingGetDownloadUrlResponse setMethod(String method) {
        this.method = method;
        return this;
    }
    public String getMethod() {
        return this.method;
    }

    public HostingGetDownloadUrlResponse setUrl(String url) {
        this.url = url;
        return this;
    }
    public String getUrl() {
        return this.url;
    }

}
