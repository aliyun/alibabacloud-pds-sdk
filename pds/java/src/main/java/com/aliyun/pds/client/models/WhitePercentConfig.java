// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class WhitePercentConfig extends TeaModel {
    @NameInMap("percent")
    public Long percent;

    @NameInMap("total")
    public Long total;

    public static WhitePercentConfig build(java.util.Map<String, ?> map) throws Exception {
        WhitePercentConfig self = new WhitePercentConfig();
        return TeaModel.build(map, self);
    }

    public WhitePercentConfig setPercent(Long percent) {
        this.percent = percent;
        return this;
    }
    public Long getPercent() {
        return this.percent;
    }

    public WhitePercentConfig setTotal(Long total) {
        this.total = total;
        return this;
    }
    public Long getTotal() {
        return this.total;
    }

}
