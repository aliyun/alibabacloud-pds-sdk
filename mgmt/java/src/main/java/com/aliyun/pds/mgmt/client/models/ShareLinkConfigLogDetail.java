// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class ShareLinkConfigLogDetail extends TeaModel {
    // enable
    @NameInMap("enable")
    public Boolean enable;

    public static ShareLinkConfigLogDetail build(java.util.Map<String, ?> map) throws Exception {
        ShareLinkConfigLogDetail self = new ShareLinkConfigLogDetail();
        return TeaModel.build(map, self);
    }

    public ShareLinkConfigLogDetail setEnable(Boolean enable) {
        this.enable = enable;
        return this;
    }
    public Boolean getEnable() {
        return this.enable;
    }

}
