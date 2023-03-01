// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * List drive request
 */
public class ListDriveRequest extends TeaModel {
    /**
     * <p>每页大小限制</p>
     */
    @NameInMap("limit")
    @Validation(maximum = 100, minimum = 1)
    public Integer limit;

    /**
     * <p>翻页标记, 接口返回的标记值</p>
     */
    @NameInMap("marker")
    public String marker;

    /**
     * <p>所属者</p>
     */
    @NameInMap("owner")
    public String owner;

    /**
     * <p>owner_type</p>
     * <p>所述者类型</p>
     */
    @NameInMap("owner_type")
    public String ownerType;

    /**
     * <p>Subdomain ID</p>
     */
    @NameInMap("subdomain_id")
    public String subdomainId;

    public static ListDriveRequest build(java.util.Map<String, ?> map) throws Exception {
        ListDriveRequest self = new ListDriveRequest();
        return TeaModel.build(map, self);
    }

    public ListDriveRequest setLimit(Integer limit) {
        this.limit = limit;
        return this;
    }
    public Integer getLimit() {
        return this.limit;
    }

    public ListDriveRequest setMarker(String marker) {
        this.marker = marker;
        return this;
    }
    public String getMarker() {
        return this.marker;
    }

    public ListDriveRequest setOwner(String owner) {
        this.owner = owner;
        return this;
    }
    public String getOwner() {
        return this.owner;
    }

    public ListDriveRequest setOwnerType(String ownerType) {
        this.ownerType = ownerType;
        return this;
    }
    public String getOwnerType() {
        return this.ownerType;
    }

    public ListDriveRequest setSubdomainId(String subdomainId) {
        this.subdomainId = subdomainId;
        return this;
    }
    public String getSubdomainId() {
        return this.subdomainId;
    }

}
