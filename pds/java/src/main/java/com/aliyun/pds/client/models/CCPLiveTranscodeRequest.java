// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 触发实时转码
 */
public class CCPLiveTranscodeRequest extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    // addition_data
    @NameInMap("addition_data")
    public java.util.Map<String, ?> additionData;

    // object_path
    @NameInMap("object_path")
    public String objectPath;

    public static CCPLiveTranscodeRequest build(java.util.Map<String, ?> map) throws Exception {
        CCPLiveTranscodeRequest self = new CCPLiveTranscodeRequest();
        return TeaModel.build(map, self);
    }

    public CCPLiveTranscodeRequest setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public CCPLiveTranscodeRequest setAdditionData(java.util.Map<String, ?> additionData) {
        this.additionData = additionData;
        return this;
    }
    public java.util.Map<String, ?> getAdditionData() {
        return this.additionData;
    }

    public CCPLiveTranscodeRequest setObjectPath(String objectPath) {
        this.objectPath = objectPath;
        return this;
    }
    public String getObjectPath() {
        return this.objectPath;
    }

}
