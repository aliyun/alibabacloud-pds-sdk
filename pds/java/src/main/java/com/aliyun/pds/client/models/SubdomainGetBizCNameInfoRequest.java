// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class SubdomainGetBizCNameInfoRequest extends TeaModel {
    // cname type
    @NameInMap("cname_type")
    @Validation(required = true)
    public String cnameType;

    // domain ID
    @NameInMap("domain_id")
    @Validation(required = true)
    public String domainId;

    // is vpc
    @NameInMap("is_vpc")
    public Boolean isVpc;

    // subdomain ID
    @NameInMap("subdomain_id")
    @Validation(required = true)
    public String subdomainId;

    public static SubdomainGetBizCNameInfoRequest build(java.util.Map<String, ?> map) throws Exception {
        SubdomainGetBizCNameInfoRequest self = new SubdomainGetBizCNameInfoRequest();
        return TeaModel.build(map, self);
    }

    public SubdomainGetBizCNameInfoRequest setCnameType(String cnameType) {
        this.cnameType = cnameType;
        return this;
    }
    public String getCnameType() {
        return this.cnameType;
    }

    public SubdomainGetBizCNameInfoRequest setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

    public SubdomainGetBizCNameInfoRequest setIsVpc(Boolean isVpc) {
        this.isVpc = isVpc;
        return this;
    }
    public Boolean getIsVpc() {
        return this.isVpc;
    }

    public SubdomainGetBizCNameInfoRequest setSubdomainId(String subdomainId) {
        this.subdomainId = subdomainId;
        return this;
    }
    public String getSubdomainId() {
        return this.subdomainId;
    }

}
