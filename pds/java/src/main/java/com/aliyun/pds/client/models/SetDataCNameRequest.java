// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class SetDataCNameRequest extends TeaModel {
    /**
     * <p>cn-shanghai data cname</p>
     */
    @NameInMap("data_cname")
    @Validation(required = true)
    public String dataCname;

    /**
     * <p>domain ID</p>
     */
    @NameInMap("domain_id")
    @Validation(required = true)
    public String domainId;

    /**
     * <p>location</p>
     */
    @NameInMap("location")
    @Validation(required = true)
    public String location;

    public static SetDataCNameRequest build(java.util.Map<String, ?> map) throws Exception {
        SetDataCNameRequest self = new SetDataCNameRequest();
        return TeaModel.build(map, self);
    }

    public SetDataCNameRequest setDataCname(String dataCname) {
        this.dataCname = dataCname;
        return this;
    }
    public String getDataCname() {
        return this.dataCname;
    }

    public SetDataCNameRequest setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

    public SetDataCNameRequest setLocation(String location) {
        this.location = location;
        return this;
    }
    public String getLocation() {
        return this.location;
    }

}
