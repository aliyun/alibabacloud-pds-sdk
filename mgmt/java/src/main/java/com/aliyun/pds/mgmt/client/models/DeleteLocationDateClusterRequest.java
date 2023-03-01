// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * delete locationCluster request
 */
public class DeleteLocationDateClusterRequest extends TeaModel {
    @NameInMap("cluster_id")
    public String clusterId;

    /**
     * <p>drive_id</p>
     */
    @NameInMap("drive_id")
    @Validation(required = true, pattern = "[0-9]+")
    public String driveId;

    public static DeleteLocationDateClusterRequest build(java.util.Map<String, ?> map) throws Exception {
        DeleteLocationDateClusterRequest self = new DeleteLocationDateClusterRequest();
        return TeaModel.build(map, self);
    }

    public DeleteLocationDateClusterRequest setClusterId(String clusterId) {
        this.clusterId = clusterId;
        return this;
    }
    public String getClusterId() {
        return this.clusterId;
    }

    public DeleteLocationDateClusterRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

}
