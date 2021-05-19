// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * get_media_play_url response
 */
public class GetMediaPlayURLResponse extends TeaModel {
    // url
    @NameInMap("url")
    public String url;

    public static GetMediaPlayURLResponse build(java.util.Map<String, ?> map) throws Exception {
        GetMediaPlayURLResponse self = new GetMediaPlayURLResponse();
        return TeaModel.build(map, self);
    }

    public GetMediaPlayURLResponse setUrl(String url) {
        this.url = url;
        return this;
    }
    public String getUrl() {
        return this.url;
    }

}
