// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * report_share_link_access_event request
 */
public class ReportShareLinkAccessEventRequest extends TeaModel {
    /**
     * <p>share_id</p>
     */
    @NameInMap("share_id")
    public String shareId;

    /**
     * <p>sub_type</p>
     */
    @NameInMap("sub_type")
    public String subType;

    public static ReportShareLinkAccessEventRequest build(java.util.Map<String, ?> map) throws Exception {
        ReportShareLinkAccessEventRequest self = new ReportShareLinkAccessEventRequest();
        return TeaModel.build(map, self);
    }

    public ReportShareLinkAccessEventRequest setShareId(String shareId) {
        this.shareId = shareId;
        return this;
    }
    public String getShareId() {
        return this.shareId;
    }

    public ReportShareLinkAccessEventRequest setSubType(String subType) {
        this.subType = subType;
        return this;
    }
    public String getSubType() {
        return this.subType;
    }

}
