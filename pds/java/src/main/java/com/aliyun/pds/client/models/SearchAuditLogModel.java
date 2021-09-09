// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class SearchAuditLogModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public SearchAuditLogResponse body;

    public static SearchAuditLogModel build(java.util.Map<String, ?> map) throws Exception {
        SearchAuditLogModel self = new SearchAuditLogModel();
        return TeaModel.build(map, self);
    }

    public SearchAuditLogModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public SearchAuditLogModel setBody(SearchAuditLogResponse body) {
        this.body = body;
        return this;
    }
    public SearchAuditLogResponse getBody() {
        return this.body;
    }

}
