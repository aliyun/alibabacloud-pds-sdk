// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class DomainCNameResponse extends TeaModel {
    /**
     * <p>data cname list</p>
     */
    @NameInMap("data_cname_list")
    @Validation(required = true)
    public java.util.List<DataCName> dataCnameList;

    /**
     * <p>domain ID</p>
     */
    @NameInMap("domain_id")
    @Validation(required = true)
    public String domainId;

    public static DomainCNameResponse build(java.util.Map<String, ?> map) throws Exception {
        DomainCNameResponse self = new DomainCNameResponse();
        return TeaModel.build(map, self);
    }

    public DomainCNameResponse setDataCnameList(java.util.List<DataCName> dataCnameList) {
        this.dataCnameList = dataCnameList;
        return this;
    }
    public java.util.List<DataCName> getDataCnameList() {
        return this.dataCnameList;
    }

    public DomainCNameResponse setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

}
