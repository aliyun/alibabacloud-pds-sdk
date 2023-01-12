// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class SetShareStatusRequest extends TeaModel {
    /**
     * <p>domain ID</p>
     */
    @NameInMap("domain_id")
    @Validation(required = true)
    public String domainId;

    /**
     * <p>enabled</p>
     */
    @NameInMap("enabled")
    @Validation(required = true)
    public Boolean enabled;

    public static SetShareStatusRequest build(java.util.Map<String, ?> map) throws Exception {
        SetShareStatusRequest self = new SetShareStatusRequest();
        return TeaModel.build(map, self);
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
