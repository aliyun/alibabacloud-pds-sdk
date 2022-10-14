// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 *
 */
public class ShareConfigLogDetail extends TeaModel {
    // enable
    @NameInMap("enable")
    public Boolean enable;

    public static ShareConfigLogDetail build(java.util.Map<String, ?> map) throws Exception {
        ShareConfigLogDetail self = new ShareConfigLogDetail();
        return TeaModel.build(map, self);
    }

    public ShareConfigLogDetail setEnable(Boolean enable) {
        this.enable = enable;
        return this;
    }
    public Boolean getEnable() {
        return this.enable;
    }

}
