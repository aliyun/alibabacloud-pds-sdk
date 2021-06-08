// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class LiveTranscodeModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public CCPLiveTranscodeResponse body;

    public static LiveTranscodeModel build(java.util.Map<String, ?> map) throws Exception {
        LiveTranscodeModel self = new LiveTranscodeModel();
        return TeaModel.build(map, self);
    }

    public LiveTranscodeModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public LiveTranscodeModel setBody(CCPLiveTranscodeResponse body) {
        this.body = body;
        return this;
    }
    public CCPLiveTranscodeResponse getBody() {
        return this.body;
    }

}
