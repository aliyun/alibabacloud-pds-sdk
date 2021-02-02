// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.hostingmode.client.models;

import com.aliyun.tea.*;

public class VideoDefinitionModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public HostingVideoDefinitionResponse body;

    public static VideoDefinitionModel build(java.util.Map<String, ?> map) throws Exception {
        VideoDefinitionModel self = new VideoDefinitionModel();
        return TeaModel.build(map, self);
    }

    public VideoDefinitionModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public VideoDefinitionModel setBody(HostingVideoDefinitionResponse body) {
        this.body = body;
        return this;
    }
    public HostingVideoDefinitionResponse getBody() {
        return this.body;
    }

}
