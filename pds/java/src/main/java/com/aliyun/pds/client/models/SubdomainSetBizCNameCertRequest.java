// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class SubdomainSetBizCNameCertRequest extends TeaModel {
    @NameInMap("CertID")
    public String CertID;

    // biz cname
    @NameInMap("biz_cname")
    public String bizCname;

    // cert body
    @NameInMap("cert_body")
    @Validation(required = true)
    public String certBody;

    // cert name
    @NameInMap("cert_name")
    @Validation(required = true)
    public String certName;

    // cert privatekey
    @NameInMap("cert_privatekey")
    @Validation(required = true)
    public String certPrivatekey;

    // cname type
    @NameInMap("cname_type")
    @Validation(required = true)
    public String cnameType;

    // domain ID
    @NameInMap("domain_id")
    @Validation(required = true)
    public String domainId;

    // biz cname
    @NameInMap("is_vpc")
    public Boolean isVpc;

    // subdomain ID
    @NameInMap("subdomain_id")
    @Validation(required = true)
    public String subdomainId;

    public static SubdomainSetBizCNameCertRequest build(java.util.Map<String, ?> map) throws Exception {
        SubdomainSetBizCNameCertRequest self = new SubdomainSetBizCNameCertRequest();
        return TeaModel.build(map, self);
    }

    public SubdomainSetBizCNameCertRequest setCertID(String CertID) {
        this.CertID = CertID;
        return this;
    }
    public String getCertID() {
        return this.CertID;
    }

    public SubdomainSetBizCNameCertRequest setBizCname(String bizCname) {
        this.bizCname = bizCname;
        return this;
    }
    public String getBizCname() {
        return this.bizCname;
    }

    public SubdomainSetBizCNameCertRequest setCertBody(String certBody) {
        this.certBody = certBody;
        return this;
    }
    public String getCertBody() {
        return this.certBody;
    }

    public SubdomainSetBizCNameCertRequest setCertName(String certName) {
        this.certName = certName;
        return this;
    }
    public String getCertName() {
        return this.certName;
    }

    public SubdomainSetBizCNameCertRequest setCertPrivatekey(String certPrivatekey) {
        this.certPrivatekey = certPrivatekey;
        return this;
    }
    public String getCertPrivatekey() {
        return this.certPrivatekey;
    }

    public SubdomainSetBizCNameCertRequest setCnameType(String cnameType) {
        this.cnameType = cnameType;
        return this;
    }
    public String getCnameType() {
        return this.cnameType;
    }

    public SubdomainSetBizCNameCertRequest setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

    public SubdomainSetBizCNameCertRequest setIsVpc(Boolean isVpc) {
        this.isVpc = isVpc;
        return this;
    }
    public Boolean getIsVpc() {
        return this.isVpc;
    }

    public SubdomainSetBizCNameCertRequest setSubdomainId(String subdomainId) {
        this.subdomainId = subdomainId;
        return this;
    }
    public String getSubdomainId() {
        return this.subdomainId;
    }

}
