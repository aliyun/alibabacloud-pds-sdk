// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 导出审计日志response
 */
public class ExportAuditLogResponse extends TeaModel {
    @NameInMap("async_task_id")
    public String asyncTaskId;

    public static ExportAuditLogResponse build(java.util.Map<String, ?> map) throws Exception {
        ExportAuditLogResponse self = new ExportAuditLogResponse();
        return TeaModel.build(map, self);
    }

    public ExportAuditLogResponse setAsyncTaskId(String asyncTaskId) {
        this.asyncTaskId = asyncTaskId;
        return this;
    }
    public String getAsyncTaskId() {
        return this.asyncTaskId;
    }

}
