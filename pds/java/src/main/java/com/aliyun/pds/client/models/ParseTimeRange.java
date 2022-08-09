// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 *
 */
public class ParseTimeRange extends TeaModel {
    @NameInMap("end")
    public String end;

    @NameInMap("start")
    public String start;

    public static ParseTimeRange build(java.util.Map<String, ?> map) throws Exception {
        ParseTimeRange self = new ParseTimeRange();
        return TeaModel.build(map, self);
    }

    public ParseTimeRange setEnd(String end) {
        this.end = end;
        return this;
    }
    public String getEnd() {
        return this.end;
    }

    public ParseTimeRange setStart(String start) {
        this.start = start;
        return this;
    }
    public String getStart() {
        return this.start;
    }

}
