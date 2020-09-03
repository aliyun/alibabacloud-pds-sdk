// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.hosting.mode.models;

import com.aliyun.tea.*;

public class VideoTranscodeModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public HostingVideoTranscodeResponse body;

    public static VideoTranscodeModel build(java.util.Map<String, ?> map) throws Exception {
        VideoTranscodeModel self = new VideoTranscodeModel();
        return TeaModel.build(map, self);
    }

    public VideoTranscodeModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public VideoTranscodeModel setBody(HostingVideoTranscodeResponse body) {
        this.body = body;
        return this;
    }
    public HostingVideoTranscodeResponse getBody() {
        return this.body;
    }

}
