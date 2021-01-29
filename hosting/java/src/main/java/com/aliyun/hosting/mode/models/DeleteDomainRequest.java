// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.hosting.mode.models;

import com.aliyun.tea.*;

/**
 * delete domain request
 */
public class DeleteDomainRequest extends TeaModel {
    // Domain ID
    @NameInMap("domain_id")
    @Validation(required = true)
    public String domainId;

    public static DeleteDomainRequest build(java.util.Map<String, ?> map) throws Exception {
        DeleteDomainRequest self = new DeleteDomainRequest();
        return TeaModel.build(map, self);
    }

    public DeleteDomainRequest setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

}
