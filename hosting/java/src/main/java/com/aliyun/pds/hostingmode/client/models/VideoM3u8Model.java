// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.hostingmode.client.models;

import com.aliyun.tea.*;

public class VideoM3u8Model extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public byte[] body;

    public static VideoM3u8Model build(java.util.Map<String, ?> map) throws Exception {
        VideoM3u8Model self = new VideoM3u8Model();
        return TeaModel.build(map, self);
    }

    public VideoM3u8Model setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public VideoM3u8Model setBody(byte[] body) {
        this.body = body;
        return this;
    }
    public byte[] getBody() {
        return this.body;
    }

}
