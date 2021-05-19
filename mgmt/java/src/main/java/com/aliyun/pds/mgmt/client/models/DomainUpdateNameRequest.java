// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * domain update name request
 */
public class DomainUpdateNameRequest extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    // Domain ID
    @NameInMap("domain_id")
    @Validation(required = true)
    public String domainId;

    // Name
    @NameInMap("name")
    @Validation(required = true)
    public String name;

    public static DomainUpdateNameRequest build(java.util.Map<String, ?> map) throws Exception {
        DomainUpdateNameRequest self = new DomainUpdateNameRequest();
        return TeaModel.build(map, self);
    }

    public DomainUpdateNameRequest setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
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
