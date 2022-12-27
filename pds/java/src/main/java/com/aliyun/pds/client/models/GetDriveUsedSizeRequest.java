// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 查询 Drive 使用空间
 */
public class GetDriveUsedSizeRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    /**
     * <p>drive_id</p>
     */
    @NameInMap("drive_id")
    @Validation(required = true, pattern = "[0-9]+")
    public String driveId;

    /**
     * <p>subdomain</p>
     */
    @NameInMap("subdomain_id")
    public String subdomainId;

    public static GetDriveUsedSizeRequest build(java.util.Map<String, ?> map) throws Exception {
        GetDriveUsedSizeRequest self = new GetDriveUsedSizeRequest();
        return TeaModel.build(map, self);
    }

    public GetDriveUsedSizeRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public GetDriveUsedSizeRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public GetDriveUsedSizeRequest setSubdomainId(String subdomainId) {
        this.subdomainId = subdomainId;
        return this;
    }
    public String getSubdomainId() {
        return this.subdomainId;
    }

}
