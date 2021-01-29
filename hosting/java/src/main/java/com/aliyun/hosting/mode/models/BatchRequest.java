// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.hosting.mode.models;

import com.aliyun.tea.*;

/**
 * 批处理
 */
public class BatchRequest extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    // Requests 请求合集
    @NameInMap("requests")
    @Validation(required = true)
    public java.util.List<BatchSubRequest> requests;

    // 支持的资源类型
    @NameInMap("resource")
    @Validation(required = true)
    public String resource;

    public static BatchRequest build(java.util.Map<String, ?> map) throws Exception {
        BatchRequest self = new BatchRequest();
        return TeaModel.build(map, self);
    }

    public BatchRequest setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public BatchRequest setRequests(java.util.List<BatchSubRequest> requests) {
        this.requests = requests;
        return this;
    }
    public java.util.List<BatchSubRequest> getRequests() {
        return this.requests;
    }

    public BatchRequest setResource(String resource) {
        this.resource = resource;
        return this;
    }
    public String getResource() {
        return this.resource;
    }

}
