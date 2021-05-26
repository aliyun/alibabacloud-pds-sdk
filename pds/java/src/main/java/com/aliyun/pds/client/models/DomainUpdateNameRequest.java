// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * domain update name request
 */
public class DomainUpdateNameRequest extends TeaModel {
    // Domain ID
    @NameInMap("domain_id")
    @Validation(required = true)
    public String domainId;

    // Domain 名称
    @NameInMap("name")
    @Validation(required = true)
    public String name;

    public static DomainUpdateNameRequest build(java.util.Map<String, ?> map) throws Exception {
        DomainUpdateNameRequest self = new DomainUpdateNameRequest();
        return TeaModel.build(map, self);
    }

    public DomainUpdateNameRequest setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

    public DomainUpdateNameRequest setName(String name) {
        this.name = name;
        return this;
    }
    public String getName() {
        return this.name;
    }

}
