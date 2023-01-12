// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class SubdomainDeleteBizCNameCertRequest extends TeaModel {
    /**
     * <p>biz cname</p>
     */
    @NameInMap("biz_cname")
    public String bizCname;

    /**
     * <p>cert id</p>
     */
    @NameInMap("cert_id")
    public String certId;

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
     * <p>is vpc</p>
     */
    @NameInMap("is_vpc")
    public Boolean isVpc;

    /**
     * <p>subdomain ID</p>
     */
    @NameInMap("subdomain_id")
    @Validation(required = true)
    public String subdomainId;

    public static SubdomainDeleteBizCNameCertRequest build(java.util.Map<String, ?> map) throws Exception {
        SubdomainDeleteBizCNameCertRequest self = new SubdomainDeleteBizCNameCertRequest();
        return TeaModel.build(map, self);
    }

    public SubdomainDeleteBizCNameCertRequest setBizCname(String bizCname) {
        this.bizCname = bizCname;
        return this;
    }
    public String getBizCname() {
        return this.bizCname;
    }

    public SubdomainDeleteBizCNameCertRequest setCertId(String certId) {
        this.certId = certId;
        return this;
    }
    public String getCertId() {
        return this.certId;
    }

    public SubdomainDeleteBizCNameCertRequest setCnameType(String cnameType) {
        this.cnameType = cnameType;
        return this;
    }
    public String getCnameType() {
        return this.cnameType;
    }

    public SubdomainDeleteBizCNameCertRequest setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

    public SubdomainDeleteBizCNameCertRequest setIsVpc(Boolean isVpc) {
        this.isVpc = isVpc;
        return this;
    }
    public Boolean getIsVpc() {
        return this.isVpc;
    }

    public SubdomainDeleteBizCNameCertRequest setSubdomainId(String subdomainId) {
        this.subdomainId = subdomainId;
        return this;
    }
    public String getSubdomainId() {
        return this.subdomainId;
    }

}
