// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class DeleteBizCNameAndCertRequest extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

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

    public static DeleteBizCNameAndCertRequest build(java.util.Map<String, ?> map) throws Exception {
        DeleteBizCNameAndCertRequest self = new DeleteBizCNameAndCertRequest();
        return TeaModel.build(map, self);
    }

    public DeleteBizCNameAndCertRequest setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public DeleteBizCNameAndCertRequest setBizCname(String bizCname) {
        this.bizCname = bizCname;
        return this;
    }
    public String getBizCname() {
        return this.bizCname;
    }

    public DeleteBizCNameAndCertRequest setCnameType(String cnameType) {
        this.cnameType = cnameType;
        return this;
    }
    public String getCnameType() {
        return this.cnameType;
    }

    public DeleteBizCNameAndCertRequest setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

    public DeleteBizCNameAndCertRequest setIsVpc(Boolean isVpc) {
        this.isVpc = isVpc;
        return this;
    }
    public Boolean getIsVpc() {
        return this.isVpc;
    }

}
