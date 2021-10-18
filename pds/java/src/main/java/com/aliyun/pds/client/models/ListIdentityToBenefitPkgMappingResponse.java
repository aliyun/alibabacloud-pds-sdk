// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * List identity to benefit pkg mapping info
 */
public class ListIdentityToBenefitPkgMappingResponse extends TeaModel {
    @NameInMap("items")
    public java.util.List<BaseIdentityToBenefitPkgMappingResponse> items;

    public static ListIdentityToBenefitPkgMappingResponse build(java.util.Map<String, ?> map) throws Exception {
        ListIdentityToBenefitPkgMappingResponse self = new ListIdentityToBenefitPkgMappingResponse();
        return TeaModel.build(map, self);
    }

    public ListIdentityToBenefitPkgMappingResponse setItems(java.util.List<BaseIdentityToBenefitPkgMappingResponse> items) {
        this.items = items;
        return this;
    }
    public java.util.List<BaseIdentityToBenefitPkgMappingResponse> getItems() {
        return this.items;
    }

}
