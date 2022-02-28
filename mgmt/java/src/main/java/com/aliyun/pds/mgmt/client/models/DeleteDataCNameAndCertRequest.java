// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class DeleteDataCNameAndCertRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

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

    public DeleteDataCNameAndCertRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
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
