// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class SetBizCNameResponse extends TeaModel {
    // biz cname
    @NameInMap("biz_cname")
    public String bizCname;

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

    public static SetBizCNameResponse build(java.util.Map<String, ?> map) throws Exception {
        SetBizCNameResponse self = new SetBizCNameResponse();
        return TeaModel.build(map, self);
    }

    public SetBizCNameResponse setBizCname(String bizCname) {
        this.bizCname = bizCname;
        return this;
    }
    public String getBizCname() {
        return this.bizCname;
    }

    public SetBizCNameResponse setCnameStatus(CNameStatus cnameStatus) {
        this.cnameStatus = cnameStatus;
        return this;
    }
    public CNameStatus getCnameStatus() {
        return this.cnameStatus;
    }

    public SetBizCNameResponse setCnameType(String cnameType) {
        this.cnameType = cnameType;
        return this;
    }
    public String getCnameType() {
        return this.cnameType;
    }

    public SetBizCNameResponse setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

    public SetBizCNameResponse setIsVpc(Boolean isVpc) {
        this.isVpc = isVpc;
        return this;
    }
    public Boolean getIsVpc() {
        return this.isVpc;
    }

}
