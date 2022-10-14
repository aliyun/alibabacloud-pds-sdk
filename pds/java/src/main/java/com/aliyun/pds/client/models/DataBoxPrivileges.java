// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 *
 */
public class DataBoxPrivileges extends TeaModel {
    // feature_attr_id
    @NameInMap("feature_attr_id")
    public String featureAttrId;

    // feature_id
    @NameInMap("feature_id")
    public String featureId;

    // quota
    @NameInMap("quota")
    public Long quota;

    public static DataBoxPrivileges build(java.util.Map<String, ?> map) throws Exception {
        DataBoxPrivileges self = new DataBoxPrivileges();
        return TeaModel.build(map, self);
    }

    public DataBoxPrivileges setFeatureAttrId(String featureAttrId) {
        this.featureAttrId = featureAttrId;
        return this;
    }
    public String getFeatureAttrId() {
        return this.featureAttrId;
    }

    public DataBoxPrivileges setFeatureId(String featureId) {
        this.featureId = featureId;
        return this;
    }
    public String getFeatureId() {
        return this.featureId;
    }

    public DataBoxPrivileges setQuota(Long quota) {
        this.quota = quota;
        return this;
    }
    public Long getQuota() {
        return this.quota;
    }

}
