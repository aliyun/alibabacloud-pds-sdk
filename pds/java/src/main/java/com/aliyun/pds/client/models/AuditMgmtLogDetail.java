// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class AuditMgmtLogDetail extends TeaModel {
    // file_name
    @NameInMap("file_name")
    public String fileName;

    // query
    @NameInMap("query")
    public String query;

    public static AuditMgmtLogDetail build(java.util.Map<String, ?> map) throws Exception {
        AuditMgmtLogDetail self = new AuditMgmtLogDetail();
        return TeaModel.build(map, self);
    }

    public AuditMgmtLogDetail setFileName(String fileName) {
        this.fileName = fileName;
        return this;
    }
    public String getFileName() {
        return this.fileName;
    }

    public AuditMgmtLogDetail setQuery(String query) {
        this.query = query;
        return this;
    }
    public String getQuery() {
        return this.query;
    }

}
