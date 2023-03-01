// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class DeleteSubdomainRequest extends TeaModel {
    /**
     * <p>用以唯一标识subdomain</p>
     */
    @NameInMap("subdomain_id")
    @Validation(required = true)
    public String subdomainId;

    public static DeleteSubdomainRequest build(java.util.Map<String, ?> map) throws Exception {
        DeleteSubdomainRequest self = new DeleteSubdomainRequest();
        return TeaModel.build(map, self);
    }

    public DeleteSubdomainRequest setSubdomainId(String subdomainId) {
        this.subdomainId = subdomainId;
        return this;
    }
    public String getSubdomainId() {
        return this.subdomainId;
    }

}
