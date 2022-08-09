// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 *
 */
public class SetShareLinkStatusRequest extends TeaModel {
    // domain ID
    @NameInMap("domain_id")
    @Validation(required = true)
    public String domainId;

    // enabled
    @NameInMap("enabled")
    @Validation(required = true)
    public Boolean enabled;

    public static SetShareLinkStatusRequest build(java.util.Map<String, ?> map) throws Exception {
        SetShareLinkStatusRequest self = new SetShareLinkStatusRequest();
        return TeaModel.build(map, self);
    }

    public SetShareLinkStatusRequest setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

    public SetShareLinkStatusRequest setEnabled(Boolean enabled) {
        this.enabled = enabled;
        return this;
    }
    public Boolean getEnabled() {
        return this.enabled;
    }

}
