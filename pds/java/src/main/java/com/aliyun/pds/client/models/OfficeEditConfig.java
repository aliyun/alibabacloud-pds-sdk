// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * OfficeEditConfig 文档编辑配置
 */
public class OfficeEditConfig extends TeaModel {
    @NameInMap("cross_region_pds_endpoint")
    public String crossRegionPdsEndpoint;

    @NameInMap("enabled")
    public Boolean enabled;

    @NameInMap("encode_user_id")
    public Boolean encodeUserId;

    @NameInMap("role")
    public String role;

    public static OfficeEditConfig build(java.util.Map<String, ?> map) throws Exception {
        OfficeEditConfig self = new OfficeEditConfig();
        return TeaModel.build(map, self);
    }

    public OfficeEditConfig setCrossRegionPdsEndpoint(String crossRegionPdsEndpoint) {
        this.crossRegionPdsEndpoint = crossRegionPdsEndpoint;
        return this;
    }
    public String getCrossRegionPdsEndpoint() {
        return this.crossRegionPdsEndpoint;
    }

    public OfficeEditConfig setEnabled(Boolean enabled) {
        this.enabled = enabled;
        return this;
    }
    public Boolean getEnabled() {
        return this.enabled;
    }

    public OfficeEditConfig setEncodeUserId(Boolean encodeUserId) {
        this.encodeUserId = encodeUserId;
        return this;
    }
    public Boolean getEncodeUserId() {
        return this.encodeUserId;
    }

    public OfficeEditConfig setRole(String role) {
        this.role = role;
        return this;
    }
    public String getRole() {
        return this.role;
    }

}
