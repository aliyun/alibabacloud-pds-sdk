// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class DomainBuildClient extends TeaModel {
    @NameInMap("copyright")
    public String copyright;

    @NameInMap("name")
    public String name;

    public static DomainBuildClient build(java.util.Map<String, ?> map) throws Exception {
        DomainBuildClient self = new DomainBuildClient();
        return TeaModel.build(map, self);
    }

    public DomainBuildClient setCopyright(String copyright) {
        this.copyright = copyright;
        return this;
    }
    public String getCopyright() {
        return this.copyright;
    }

    public DomainBuildClient setName(String name) {
        this.name = name;
        return this;
    }
    public String getName() {
        return this.name;
    }

}
