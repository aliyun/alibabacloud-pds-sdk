// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * update locationCluster response
 */
public class UpdateLocationDateClusterResponse extends TeaModel {
    @NameInMap("cluster_id")
    public String clusterId;

    @NameInMap("drive_id")
    public String driveId;

    public static UpdateLocationDateClusterResponse build(java.util.Map<String, ?> map) throws Exception {
        UpdateLocationDateClusterResponse self = new UpdateLocationDateClusterResponse();
        return TeaModel.build(map, self);
    }

    public UpdateLocationDateClusterResponse setClusterId(String clusterId) {
        this.clusterId = clusterId;
        return this;
    }
    public String getClusterId() {
        return this.clusterId;
    }

    public UpdateLocationDateClusterResponse setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

}
