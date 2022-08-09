// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 *
 */
public class CcpCallback extends TeaModel {
    @NameInMap("body")
    public java.util.Map<String, ?> body;

    @NameInMap("url")
    public String url;

    public static CcpCallback build(java.util.Map<String, ?> map) throws Exception {
        CcpCallback self = new CcpCallback();
        return TeaModel.build(map, self);
    }

    public CcpCallback setBody(java.util.Map<String, ?> body) {
        this.body = body;
        return this;
    }
    public java.util.Map<String, ?> getBody() {
        return this.body;
    }

    public CcpCallback setUrl(String url) {
        this.url = url;
        return this;
    }
    public String getUrl() {
        return this.url;
    }

}
