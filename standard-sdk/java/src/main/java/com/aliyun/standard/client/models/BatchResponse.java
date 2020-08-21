// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.standard.client.models;

import com.aliyun.tea.*;

/**
 * batch operation response
 */
public class BatchResponse extends TeaModel {
    // responses 返回结果合集
    @NameInMap("responses")
    public java.util.List<BatchSubResponse> responses;

    public static BatchResponse build(java.util.Map<String, ?> map) throws Exception {
        BatchResponse self = new BatchResponse();
        return TeaModel.build(map, self);
    }

    public BatchResponse setResponses(java.util.List<BatchSubResponse> responses) {
        this.responses = responses;
        return this;
    }
    public java.util.List<BatchSubResponse> getResponses() {
        return this.responses;
    }

}
