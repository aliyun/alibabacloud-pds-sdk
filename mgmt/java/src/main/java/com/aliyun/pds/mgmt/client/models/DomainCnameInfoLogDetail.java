// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class DomainCnameInfoLogDetail extends TeaModel {
    /**
     * <p>cert_name</p>
     */
    @NameInMap("cert_name")
    public String certName;

    /**
     * <p>cname</p>
     */
    @NameInMap("cname")
    public String cname;

    public static DomainCnameInfoLogDetail build(java.util.Map<String, ?> map) throws Exception {
        DomainCnameInfoLogDetail self = new DomainCnameInfoLogDetail();
        return TeaModel.build(map, self);
    }

    public DomainCnameInfoLogDetail setCertName(String certName) {
        this.certName = certName;
        return this;
    }
    public String getCertName() {
        return this.certName;
    }

    public DomainCnameInfoLogDetail setCname(String cname) {
        this.cname = cname;
        return this;
    }
    public String getCname() {
        return this.cname;
    }

}
