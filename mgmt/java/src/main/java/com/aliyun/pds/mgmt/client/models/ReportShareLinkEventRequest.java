// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * report_share_link_event request
 */
public class ReportShareLinkEventRequest extends TeaModel {
    // share_id
    @NameInMap("share_id")
    public String shareId;

    // sub_type
    @NameInMap("sub_type")
    public String subType;

    public static ReportShareLinkEventRequest build(java.util.Map<String, ?> map) throws Exception {
        ReportShareLinkEventRequest self = new ReportShareLinkEventRequest();
        return TeaModel.build(map, self);
    }

    public ReportShareLinkEventRequest setShareId(String shareId) {
        this.shareId = shareId;
        return this;
    }
    public String getShareId() {
        return this.shareId;
    }

    public ReportShareLinkEventRequest setSubType(String subType) {
        this.subType = subType;
        return this;
    }
    public String getSubType() {
        return this.subType;
    }

}
