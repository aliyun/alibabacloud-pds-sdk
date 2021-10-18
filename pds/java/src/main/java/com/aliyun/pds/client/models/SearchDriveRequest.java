// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * Search drive request
 */
public class SearchDriveRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    // Drive Fuzz Name
    @NameInMap("drive_name")
    @Validation(required = true)
    public String driveName;

    // 每页大小限制
    @NameInMap("limit")
    @Validation(maximum = 100, minimum = 1)
    public Integer limit;

    // 翻页标记, 接口返回的标记值
    @NameInMap("marker")
    public String marker;

    // 所属者
    @NameInMap("owner")
    public String owner;

    // owner_type
    // 所述者类型
    @NameInMap("owner_type")
    public String ownerType;

    // Subdomain ID
    @NameInMap("subdomain_id")
    public String subdomainId;

    public static SearchDriveRequest build(java.util.Map<String, ?> map) throws Exception {
        SearchDriveRequest self = new SearchDriveRequest();
        return TeaModel.build(map, self);
    }

    public SearchDriveRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public SearchDriveRequest setDriveName(String driveName) {
        this.driveName = driveName;
        return this;
    }
    public String getDriveName() {
        return this.driveName;
    }

    public SearchDriveRequest setLimit(Integer limit) {
        this.limit = limit;
        return this;
    }
    public Integer getLimit() {
        return this.limit;
    }

    public SearchDriveRequest setMarker(String marker) {
        this.marker = marker;
        return this;
    }
    public String getMarker() {
        return this.marker;
    }

    public SearchDriveRequest setOwner(String owner) {
        this.owner = owner;
        return this;
    }
    public String getOwner() {
        return this.owner;
    }

    public SearchDriveRequest setOwnerType(String ownerType) {
        this.ownerType = ownerType;
        return this;
    }
    public String getOwnerType() {
        return this.ownerType;
    }

    public SearchDriveRequest setSubdomainId(String subdomainId) {
        this.subdomainId = subdomainId;
        return this;
    }
    public String getSubdomainId() {
        return this.subdomainId;
    }

}
