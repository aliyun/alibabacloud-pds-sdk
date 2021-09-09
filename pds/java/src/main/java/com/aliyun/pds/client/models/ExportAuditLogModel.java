// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

public class ExportAuditLogModel extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    @NameInMap("body")
    @Validation(required = true)
    public ExportAuditLogResponse body;

    public static ExportAuditLogModel build(java.util.Map<String, ?> map) throws Exception {
        ExportAuditLogModel self = new ExportAuditLogModel();
        return TeaModel.build(map, self);
    }

    public ExportAuditLogModel setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public ExportAuditLogModel setBody(ExportAuditLogResponse body) {
        this.body = body;
        return this;
    }
    public ExportAuditLogResponse getBody() {
        return this.body;
    }

}
