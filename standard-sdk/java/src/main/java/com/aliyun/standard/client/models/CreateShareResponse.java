// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.standard.client.models;

import com.aliyun.tea.*;

/**
 * Create share response
 */
public class CreateShareResponse extends TeaModel {
    // domain_id
    @NameInMap("domain_id")
    public String domainId;

    // share_id
    @NameInMap("share_id")
    public String shareId;

    public static CreateShareResponse build(java.util.Map<String, ?> map) throws Exception {
        CreateShareResponse self = new CreateShareResponse();
        return TeaModel.build(map, self);
    }

    public CreateShareResponse setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

    public CreateShareResponse setShareId(String shareId) {
        this.shareId = shareId;
        return this;
    }
    public String getShareId() {
        return this.shareId;
    }

}
