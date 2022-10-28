// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * delete locationCluster response
 */
public class DeleteLocationDateClusterResponse extends TeaModel {
    @NameInMap("cluster_id")
    public String clusterId;

    @NameInMap("drive_id")
    public String driveId;

    public static DeleteLocationDateClusterResponse build(java.util.Map<String, ?> map) throws Exception {
        DeleteLocationDateClusterResponse self = new DeleteLocationDateClusterResponse();
        return TeaModel.build(map, self);
    }

    public DeleteLocationDateClusterResponse setClusterId(String clusterId) {
        this.clusterId = clusterId;
        return this;
    }
    public String getClusterId() {
        return this.clusterId;
    }

    public DeleteLocationDateClusterResponse setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

}
