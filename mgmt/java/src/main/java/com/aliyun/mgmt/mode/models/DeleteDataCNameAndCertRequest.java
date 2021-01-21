// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.mgmt.mode.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class DeleteDataCNameAndCertRequest extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    // cn-shanghai data cname
    @NameInMap("data_cname")
    @Validation(required = true)
    public String dataCname;

    // domain ID
    @NameInMap("domain_id")
    @Validation(required = true)
    public String domainId;

    // location
    @NameInMap("location")
    @Validation(required = true)
    public String location;

    public static DeleteDataCNameAndCertRequest build(java.util.Map<String, ?> map) throws Exception {
        DeleteDataCNameAndCertRequest self = new DeleteDataCNameAndCertRequest();
        return TeaModel.build(map, self);
    }

    public DeleteDataCNameAndCertRequest setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
    }

    public DeleteDataCNameAndCertRequest setDataCname(String dataCname) {
        this.dataCname = dataCname;
        return this;
    }
    public String getDataCname() {
        return this.dataCname;
    }

    public DeleteDataCNameAndCertRequest setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

    public DeleteDataCNameAndCertRequest setLocation(String location) {
        this.location = location;
        return this;
    }
    public String getLocation() {
        return this.location;
    }

}
