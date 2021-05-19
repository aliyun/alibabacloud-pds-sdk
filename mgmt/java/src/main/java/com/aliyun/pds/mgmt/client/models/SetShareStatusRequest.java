// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class SetShareStatusRequest extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    // domain ID
    @NameInMap("domain_id")
    @Validation(required = true)
    public String domainId;

    // enabled
    @NameInMap("enabled")
    @Validation(required = true)
    public Boolean enabled;

    public static SetShareStatusRequest build(java.util.Map<String, ?> map) throws Exception {
        SetShareStatusRequest self = new SetShareStatusRequest();
        return TeaModel.build(map, self);
    }

    public SetShareStatusRequest setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public SetShareStatusRequest setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

    public SetShareStatusRequest setEnabled(Boolean enabled) {
        this.enabled = enabled;
        return this;
    }
    public Boolean getEnabled() {
        return this.enabled;
    }

}
