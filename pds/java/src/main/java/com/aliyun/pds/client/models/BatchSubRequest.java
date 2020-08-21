// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class BatchSubRequest extends TeaModel {
    // body 子请求的请求参数 json 字符串，可参考对于子请求文档, 当指定了body 必须传headers ： "Content-Type" 对应的类型，目前子请求入参是"application/json"
    @NameInMap("body")
    public java.util.Map<String, ?> body;

    // headers 请求头，表示body传入数据的类型
    @NameInMap("headers")
    public java.util.Map<String, ?> headers;

    // id 用于request 和 response关联， 不允许重复
    @NameInMap("id")
    @Validation(required = true)
    public String id;

    // method
    @NameInMap("method")
    @Validation(required = true)
    public String method;

    // url 子请求的api path路径， 可参考对于子请求文档
    @NameInMap("url")
    @Validation(required = true)
    public String url;

    public static BatchSubRequest build(java.util.Map<String, ?> map) throws Exception {
        BatchSubRequest self = new BatchSubRequest();
        return TeaModel.build(map, self);
    }

    public BatchSubRequest setBody(java.util.Map<String, ?> body) {
        this.body = body;
        return this;
    }
    public java.util.Map<String, ?> getBody() {
        return this.body;
    }

    public BatchSubRequest setHeaders(java.util.Map<String, ?> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, ?> getHeaders() {
        return this.headers;
    }

    public BatchSubRequest setId(String id) {
        this.id = id;
        return this;
    }
    public String getId() {
        return this.id;
    }

    public BatchSubRequest setMethod(String method) {
        this.method = method;
        return this;
    }
    public String getMethod() {
        return this.method;
    }

    public BatchSubRequest setUrl(String url) {
        this.url = url;
        return this;
    }
    public String getUrl() {
        return this.url;
    }

}
