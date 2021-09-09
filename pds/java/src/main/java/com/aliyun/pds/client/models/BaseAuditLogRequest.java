// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class BaseAuditLogRequest extends TeaModel {
    // order_by
    @NameInMap("order_by")
    public String orderBy;

    // query
    @NameInMap("query")
    @Validation(maxLength = 4096)
    public String query;

    public static BaseAuditLogRequest build(java.util.Map<String, ?> map) throws Exception {
        BaseAuditLogRequest self = new BaseAuditLogRequest();
        return TeaModel.build(map, self);
    }

    public BaseAuditLogRequest setOrderBy(String orderBy) {
        this.orderBy = orderBy;
        return this;
    }
    public String getOrderBy() {
        return this.orderBy;
    }

    public BaseAuditLogRequest setQuery(String query) {
        this.query = query;
        return this;
    }
    public String getQuery() {
        return this.query;
    }

}
