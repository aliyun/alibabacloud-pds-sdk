// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * List identity benefit package response
 */
public class ListIdentityBenefitPkgResponse extends TeaModel {
    @NameInMap("items")
    public java.util.List<IdentityBenefitPkgResponse> items;

    public static ListIdentityBenefitPkgResponse build(java.util.Map<String, ?> map) throws Exception {
        ListIdentityBenefitPkgResponse self = new ListIdentityBenefitPkgResponse();
        return TeaModel.build(map, self);
    }

    public ListIdentityBenefitPkgResponse setItems(java.util.List<IdentityBenefitPkgResponse> items) {
        this.items = items;
        return this;
    }
    public java.util.List<IdentityBenefitPkgResponse> getItems() {
        return this.items;
    }

}
