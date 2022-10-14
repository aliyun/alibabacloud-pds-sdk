// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class BatchSubResponse extends TeaModel {
    // body 子请求的返回结果，可参考对于子请求文档 json 字符串
    @NameInMap("body")
    public java.util.Map<String, ?> body;

    // id 请求带过来的id, 可以跟 request 进行关联
    @NameInMap("id")
    public String id;

    // status 子请求的返回状态码，可参考对于子请求文档
    @NameInMap("status")
    public Long status;

    public static BatchSubResponse build(java.util.Map<String, ?> map) throws Exception {
        BatchSubResponse self = new BatchSubResponse();
        return TeaModel.build(map, self);
    }

    public BatchSubResponse setBody(java.util.Map<String, ?> body) {
        this.body = body;
        return this;
    }
    public java.util.Map<String, ?> getBody() {
        return this.body;
    }

    public BatchSubResponse setId(String id) {
        this.id = id;
        return this;
    }
    public String getId() {
        return this.id;
    }

    public BatchSubResponse setStatus(Long status) {
        this.status = status;
        return this;
    }
    public Long getStatus() {
        return this.status;
    }

}
