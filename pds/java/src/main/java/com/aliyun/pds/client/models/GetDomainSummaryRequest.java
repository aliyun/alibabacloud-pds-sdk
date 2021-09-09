// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 查询 domain 概况
 */
public class GetDomainSummaryRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    public static GetDomainSummaryRequest build(java.util.Map<String, ?> map) throws Exception {
        GetDomainSummaryRequest self = new GetDomainSummaryRequest();
        return TeaModel.build(map, self);
    }

    public GetDomainSummaryRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

}
