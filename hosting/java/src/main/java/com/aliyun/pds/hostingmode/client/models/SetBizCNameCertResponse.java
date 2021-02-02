// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.hostingmode.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class SetBizCNameCertResponse extends TeaModel {
    // biz cname
    @NameInMap("biz_cname")
    public String bizCname;

    // cert name
    @NameInMap("cert_name")
    public String certName;

    // cname type
    @NameInMap("cname_type")
    public String cnameType;

    // domain ID
    @NameInMap("domain_id")
    @Validation(required = true)
    public String domainId;

    // is vpc
    @NameInMap("is_vpc")
    public Boolean isVpc;

    public static SetBizCNameCertResponse build(java.util.Map<String, ?> map) throws Exception {
        SetBizCNameCertResponse self = new SetBizCNameCertResponse();
        return TeaModel.build(map, self);
    }

    public SetBizCNameCertResponse setBizCname(String bizCname) {
        this.bizCname = bizCname;
        return this;
    }
    public String getBizCname() {
        return this.bizCname;
    }

    public SetBizCNameCertResponse setCertName(String certName) {
        this.certName = certName;
        return this;
    }
    public String getCertName() {
        return this.certName;
    }

    public SetBizCNameCertResponse setCnameType(String cnameType) {
        this.cnameType = cnameType;
        return this;
    }
    public String getCnameType() {
        return this.cnameType;
    }

    public SetBizCNameCertResponse setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

    public SetBizCNameCertResponse setIsVpc(Boolean isVpc) {
        this.isVpc = isVpc;
        return this;
    }
    public Boolean getIsVpc() {
        return this.isVpc;
    }

}
