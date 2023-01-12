// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class GetDataCNameInfoRequest extends TeaModel {
    /**
     * <p>domain ID</p>
     */
    @NameInMap("domain_id")
    @Validation(required = true)
    public String domainId;

    public static GetDataCNameInfoRequest build(java.util.Map<String, ?> map) throws Exception {
        GetDataCNameInfoRequest self = new GetDataCNameInfoRequest();
        return TeaModel.build(map, self);
    }

    public GetDataCNameInfoRequest setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

}
