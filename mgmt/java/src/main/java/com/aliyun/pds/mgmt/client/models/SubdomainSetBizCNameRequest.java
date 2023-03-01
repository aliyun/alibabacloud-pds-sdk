// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class SubdomainSetBizCNameRequest extends TeaModel {
    /**
     * <p>biz cname</p>
     */
    @NameInMap("biz_cname")
    @Validation(required = true)
    public String bizCname;

    /**
     * <p>cname type</p>
     */
    @NameInMap("cname_type")
    @Validation(required = true)
    public String cnameType;

    /**
     * <p>domain ID</p>
     */
    @NameInMap("domain_id")
    @Validation(required = true)
    public String domainId;

    /**
     * <p>biz cname</p>
     */
    @NameInMap("is_vpc")
    public Boolean isVpc;

    /**
     * <p>domain ID</p>
     */
    @NameInMap("subdomain_id")
    @Validation(required = true)
    public String subdomainId;

    public static SubdomainSetBizCNameRequest build(java.util.Map<String, ?> map) throws Exception {
        SubdomainSetBizCNameRequest self = new SubdomainSetBizCNameRequest();
        return TeaModel.build(map, self);
    }

    public SubdomainSetBizCNameRequest setBizCname(String bizCname) {
        this.bizCname = bizCname;
        return this;
    }
    public String getBizCname() {
        return this.bizCname;
    }

    public SubdomainSetBizCNameRequest setCnameType(String cnameType) {
        this.cnameType = cnameType;
        return this;
    }
    public String getCnameType() {
        return this.cnameType;
    }

    public SubdomainSetBizCNameRequest setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

    public SubdomainSetBizCNameRequest setIsVpc(Boolean isVpc) {
        this.isVpc = isVpc;
        return this;
    }
    public Boolean getIsVpc() {
        return this.isVpc;
    }

    public SubdomainSetBizCNameRequest setSubdomainId(String subdomainId) {
        this.subdomainId = subdomainId;
        return this;
    }
    public String getSubdomainId() {
        return this.subdomainId;
    }

}
