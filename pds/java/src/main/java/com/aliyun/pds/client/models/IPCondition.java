// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class IPCondition extends TeaModel {
    @NameInMap("client_ip")
    public java.util.List<String> clientIp;

    public static IPCondition build(java.util.Map<String, ?> map) throws Exception {
        IPCondition self = new IPCondition();
        return TeaModel.build(map, self);
    }

    public IPCondition setClientIp(java.util.List<String> clientIp) {
        this.clientIp = clientIp;
        return this;
    }
    public java.util.List<String> getClientIp() {
        return this.clientIp;
    }

}
