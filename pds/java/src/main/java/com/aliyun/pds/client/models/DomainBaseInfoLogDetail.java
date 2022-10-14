// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class DomainBaseInfoLogDetail extends TeaModel {
    // name
    @NameInMap("name")
    public String name;

    public static DomainBaseInfoLogDetail build(java.util.Map<String, ?> map) throws Exception {
        DomainBaseInfoLogDetail self = new DomainBaseInfoLogDetail();
        return TeaModel.build(map, self);
    }

    public DomainBaseInfoLogDetail setName(String name) {
        this.name = name;
        return this;
    }
    public String getName() {
        return this.name;
    }

}
