// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class FindStoryRequestTimeRange extends TeaModel {
    // end
    @NameInMap("end")
    public String end;

    // start
    @NameInMap("start")
    public String start;

    public static FindStoryRequestTimeRange build(java.util.Map<String, ?> map) throws Exception {
        FindStoryRequestTimeRange self = new FindStoryRequestTimeRange();
        return TeaModel.build(map, self);
    }

    public FindStoryRequestTimeRange setEnd(String end) {
        this.end = end;
        return this;
    }
    public String getEnd() {
        return this.end;
    }

    public FindStoryRequestTimeRange setStart(String start) {
        this.start = start;
        return this;
    }
    public String getStart() {
        return this.start;
    }

}
