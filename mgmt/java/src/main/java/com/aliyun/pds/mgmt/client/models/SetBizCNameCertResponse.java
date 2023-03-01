// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class SetBizCNameCertResponse extends TeaModel {
    /**
     * <p>biz cname</p>
     */
    @NameInMap("biz_cname")
    public String bizCname;

    /**
     * <p>cert name</p>
     */
    @NameInMap("cert_name")
    public String certName;

    /**
     * <p>cname type</p>
     */
    @NameInMap("cname_type")
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
