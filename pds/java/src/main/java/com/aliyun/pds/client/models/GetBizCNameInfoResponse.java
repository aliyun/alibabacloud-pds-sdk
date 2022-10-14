// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class GetBizCNameInfoResponse extends TeaModel {
    // biz cname
    @NameInMap("biz_cname")
    public String bizCname;

    // cert name
    @NameInMap("cert_id")
    public String certId;

    // cert name
    @NameInMap("cert_name")
    public String certName;

    @NameInMap("cname_status")
    public CNameStatus cnameStatus;

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

    public static GetBizCNameInfoResponse build(java.util.Map<String, ?> map) throws Exception {
        GetBizCNameInfoResponse self = new GetBizCNameInfoResponse();
        return TeaModel.build(map, self);
    }

    public GetBizCNameInfoResponse setBizCname(String bizCname) {
        this.bizCname = bizCname;
        return this;
    }
    public String getBizCname() {
        return this.bizCname;
    }

    public GetBizCNameInfoResponse setCertId(String certId) {
        this.certId = certId;
        return this;
    }
    public String getCertId() {
        return this.certId;
    }

    public GetBizCNameInfoResponse setCertName(String certName) {
        this.certName = certName;
        return this;
    }
    public String getCertName() {
        return this.certName;
    }

    public GetBizCNameInfoResponse setCnameStatus(CNameStatus cnameStatus) {
        this.cnameStatus = cnameStatus;
        return this;
    }
    public CNameStatus getCnameStatus() {
        return this.cnameStatus;
    }

    public GetBizCNameInfoResponse setCnameType(String cnameType) {
        this.cnameType = cnameType;
        return this;
    }
    public String getCnameType() {
        return this.cnameType;
    }

    public GetBizCNameInfoResponse setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

    public GetBizCNameInfoResponse setIsVpc(Boolean isVpc) {
        this.isVpc = isVpc;
        return this;
    }
    public Boolean getIsVpc() {
        return this.isVpc;
    }

}
