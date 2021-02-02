// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.hostingmode.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class SetBizCNameCertRequest extends TeaModel {
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

    public static SetBizCNameCertRequest build(java.util.Map<String, ?> map) throws Exception {
        SetBizCNameCertRequest self = new SetBizCNameCertRequest();
        return TeaModel.build(map, self);
    }

    public SetBizCNameCertRequest setCertID(String CertID) {
        this.CertID = CertID;
        return this;
    }
    public String getCertID() {
        return this.CertID;
    }

    public SetBizCNameCertRequest setBizCname(String bizCname) {
        this.bizCname = bizCname;
        return this;
    }
    public String getBizCname() {
        return this.bizCname;
    }

    public SetBizCNameCertRequest setCertBody(String certBody) {
        this.certBody = certBody;
        return this;
    }
    public String getCertBody() {
        return this.certBody;
    }

    public SetBizCNameCertRequest setCertName(String certName) {
        this.certName = certName;
        return this;
    }
    public String getCertName() {
        return this.certName;
    }

    public SetBizCNameCertRequest setCertPrivatekey(String certPrivatekey) {
        this.certPrivatekey = certPrivatekey;
        return this;
    }
    public String getCertPrivatekey() {
        return this.certPrivatekey;
    }

    public SetBizCNameCertRequest setCnameType(String cnameType) {
        this.cnameType = cnameType;
        return this;
    }
    public String getCnameType() {
        return this.cnameType;
    }

    public SetBizCNameCertRequest setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

    public SetBizCNameCertRequest setIsVpc(Boolean isVpc) {
        this.isVpc = isVpc;
        return this;
    }
    public Boolean getIsVpc() {
        return this.isVpc;
    }

}
