// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class QueryRequestTimeRange extends TeaModel {
    // end
    @NameInMap("end")
    public String end;

    // start
    @NameInMap("start")
    public String start;

    public static QueryRequestTimeRange build(java.util.Map<String, ?> map) throws Exception {
        QueryRequestTimeRange self = new QueryRequestTimeRange();
        return TeaModel.build(map, self);
    }

    public QueryRequestTimeRange setEnd(String end) {
        this.end = end;
        return this;
    }
    public String getEnd() {
        return this.end;
    }

    public QueryRequestTimeRange setStart(String start) {
        this.start = start;
        return this;
    }
    public String getStart() {
        return this.start;
    }

}
