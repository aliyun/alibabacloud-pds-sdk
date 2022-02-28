// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * report_event request
 */
public class ReportEventRequest extends TeaModel {
    // event_type
    @NameInMap("event_type")
    public String eventType;

    @NameInMap("share_link")
    public ReportShareLinkEventRequest shareLink;

    @NameInMap("share_link_access")
    public ReportShareLinkAccessEventRequest shareLinkAccess;

    public static ReportEventRequest build(java.util.Map<String, ?> map) throws Exception {
        ReportEventRequest self = new ReportEventRequest();
        return TeaModel.build(map, self);
    }

    public ReportEventRequest setEventType(String eventType) {
        this.eventType = eventType;
        return this;
    }
    public String getEventType() {
        return this.eventType;
    }

    public ReportEventRequest setShareLink(ReportShareLinkEventRequest shareLink) {
        this.shareLink = shareLink;
        return this;
    }
    public ReportShareLinkEventRequest getShareLink() {
        return this.shareLink;
    }

    public ReportEventRequest setShareLinkAccess(ReportShareLinkAccessEventRequest shareLinkAccess) {
        this.shareLinkAccess = shareLinkAccess;
        return this;
    }
    public ReportShareLinkAccessEventRequest getShareLinkAccess() {
        return this.shareLinkAccess;
    }

}
