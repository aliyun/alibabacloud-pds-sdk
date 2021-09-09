// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 导出审计日志request
 */
public class ExportAuditLogRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    // file_name
    @NameInMap("file_name")
    public String fileName;

    // language
    @NameInMap("language")
    public String language;

    // order_by
    @NameInMap("order_by")
    public String orderBy;

    // query
    @NameInMap("query")
    @Validation(maxLength = 4096)
    public String query;

    public static ExportAuditLogRequest build(java.util.Map<String, ?> map) throws Exception {
        ExportAuditLogRequest self = new ExportAuditLogRequest();
        return TeaModel.build(map, self);
    }

    public ExportAuditLogRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public ExportAuditLogRequest setFileName(String fileName) {
        this.fileName = fileName;
        return this;
    }
    public String getFileName() {
        return this.fileName;
    }

    public ExportAuditLogRequest setLanguage(String language) {
        this.language = language;
        return this;
    }
    public String getLanguage() {
        return this.language;
    }

    public ExportAuditLogRequest setOrderBy(String orderBy) {
        this.orderBy = orderBy;
        return this;
    }
    public String getOrderBy() {
        return this.orderBy;
    }

    public ExportAuditLogRequest setQuery(String query) {
        this.query = query;
        return this;
    }
    public String getQuery() {
        return this.query;
    }

}
