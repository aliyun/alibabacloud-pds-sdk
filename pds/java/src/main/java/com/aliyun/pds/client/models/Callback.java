// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class Callback extends TeaModel {
    @NameInMap("body")
    public String body;

    @NameInMap("url")
    public String url;

    public static Callback build(java.util.Map<String, ?> map) throws Exception {
        Callback self = new Callback();
        return TeaModel.build(map, self);
    }

    public Callback setBody(String body) {
        this.body = body;
        return this;
    }
    public String getBody() {
        return this.body;
    }

    public Callback setUrl(String url) {
        this.url = url;
        return this;
    }
    public String getUrl() {
        return this.url;
    }

}
