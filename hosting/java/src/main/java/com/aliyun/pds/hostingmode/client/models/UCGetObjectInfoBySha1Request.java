// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.hostingmode.client.models;

import com.aliyun.tea.*;

/**
 * UCGetObjectInfoBySha1Request
 */
public class UCGetObjectInfoBySha1Request extends TeaModel {
    @NameInMap("sha1")
    public String sha1;

    public static UCGetObjectInfoBySha1Request build(java.util.Map<String, ?> map) throws Exception {
        UCGetObjectInfoBySha1Request self = new UCGetObjectInfoBySha1Request();
        return TeaModel.build(map, self);
    }

    public UCGetObjectInfoBySha1Request setSha1(String sha1) {
        this.sha1 = sha1;
        return this;
    }
    public String getSha1() {
        return this.sha1;
    }

}
