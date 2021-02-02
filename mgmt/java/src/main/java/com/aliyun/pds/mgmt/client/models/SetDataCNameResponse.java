// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class SetDataCNameResponse extends TeaModel {
    // datacname
    @NameInMap("data_cname")
    @Validation(required = true)
    public String dataCname;

    // domain ID
    @NameInMap("domain_id")
    @Validation(required = true)
    public String domainId;

    // data location
    @NameInMap("location")
    @Validation(required = true)
    public String location;

    public static SetDataCNameResponse build(java.util.Map<String, ?> map) throws Exception {
        SetDataCNameResponse self = new SetDataCNameResponse();
        return TeaModel.build(map, self);
    }

    public SetDataCNameResponse setDataCname(String dataCname) {
        this.dataCname = dataCname;
        return this;
    }
    public String getDataCname() {
        return this.dataCname;
    }

    public SetDataCNameResponse setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

    public SetDataCNameResponse setLocation(String location) {
        this.location = location;
        return this;
    }
    public String getLocation() {
        return this.location;
    }

}
