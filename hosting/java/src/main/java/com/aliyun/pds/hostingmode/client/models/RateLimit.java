// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.hostingmode.client.models;

import com.aliyun.tea.*;

/**
 * 下载限速配置
 */
public class RateLimit extends TeaModel {
    @NameInMap("part_size")
    public Long partSize;

    @NameInMap("part_speed")
    public Long partSpeed;

    public static RateLimit build(java.util.Map<String, ?> map) throws Exception {
        RateLimit self = new RateLimit();
        return TeaModel.build(map, self);
    }

    public RateLimit setPartSize(Long partSize) {
        this.partSize = partSize;
        return this;
    }
    public Long getPartSize() {
        return this.partSize;
    }

    public RateLimit setPartSpeed(Long partSpeed) {
        this.partSpeed = partSpeed;
        return this;
    }
    public Long getPartSpeed() {
        return this.partSpeed;
    }

}
