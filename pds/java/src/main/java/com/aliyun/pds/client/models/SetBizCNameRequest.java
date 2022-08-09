// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 *
 */
public class SetBizCNameRequest extends TeaModel {
    // biz cname
    @NameInMap("biz_cname")
    @Validation(required = true)
    public String bizCname;

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

    public static SetBizCNameRequest build(java.util.Map<String, ?> map) throws Exception {
        SetBizCNameRequest self = new SetBizCNameRequest();
        return TeaModel.build(map, self);
    }

    public SetBizCNameRequest setBizCname(String bizCname) {
        this.bizCname = bizCname;
        return this;
    }
    public String getBizCname() {
        return this.bizCname;
    }

    public SetBizCNameRequest setCnameType(String cnameType) {
        this.cnameType = cnameType;
        return this;
    }
    public String getCnameType() {
        return this.cnameType;
    }

    public SetBizCNameRequest setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

    public SetBizCNameRequest setIsVpc(Boolean isVpc) {
        this.isVpc = isVpc;
        return this;
    }
    public Boolean getIsVpc() {
        return this.isVpc;
    }

}
