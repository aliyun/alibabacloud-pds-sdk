// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class SubdomainDeleteBizCNameAndCertRequest extends TeaModel {
    // api cname
    @NameInMap("biz_cname")
    public String bizCname;

    // cname type
    @NameInMap("cname_type")
    @Validation(required = true)
    public String cnameType;

    // domain ID
    @NameInMap("domain_id")
    @Validation(required = true)
    public String domainId;

    // vpc
    @NameInMap("is_vpc")
    public Boolean isVpc;

    // subdomain ID
    @NameInMap("subdomain_id")
    @Validation(required = true)
    public String subdomainId;

    public static SubdomainDeleteBizCNameAndCertRequest build(java.util.Map<String, ?> map) throws Exception {
        SubdomainDeleteBizCNameAndCertRequest self = new SubdomainDeleteBizCNameAndCertRequest();
        return TeaModel.build(map, self);
    }

    public SubdomainDeleteBizCNameAndCertRequest setBizCname(String bizCname) {
        this.bizCname = bizCname;
        return this;
    }
    public String getBizCname() {
        return this.bizCname;
    }

    public SubdomainDeleteBizCNameAndCertRequest setCnameType(String cnameType) {
        this.cnameType = cnameType;
        return this;
    }
    public String getCnameType() {
        return this.cnameType;
    }

    public SubdomainDeleteBizCNameAndCertRequest setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

    public SubdomainDeleteBizCNameAndCertRequest setIsVpc(Boolean isVpc) {
        this.isVpc = isVpc;
        return this;
    }
    public Boolean getIsVpc() {
        return this.isVpc;
    }

    public SubdomainDeleteBizCNameAndCertRequest setSubdomainId(String subdomainId) {
        this.subdomainId = subdomainId;
        return this;
    }
    public String getSubdomainId() {
        return this.subdomainId;
    }

}
