// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * report_event request
 */
public class ReportEventRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    /**
     * <p>event_type</p>
     */
    @NameInMap("event_type")
    public String eventType;

    @NameInMap("media_play")
    public ReportMediaPlayEventRequest mediaPlay;

    @NameInMap("share_link")
    public ReportShareLinkEventRequest shareLink;

    @NameInMap("share_link_access")
    public ReportShareLinkAccessEventRequest shareLinkAccess;

    public static ReportEventRequest build(java.util.Map<String, ?> map) throws Exception {
        ReportEventRequest self = new ReportEventRequest();
        return TeaModel.build(map, self);
    }

    public ReportEventRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public ReportEventRequest setEventType(String eventType) {
        this.eventType = eventType;
        return this;
    }
    public String getEventType() {
        return this.eventType;
    }

    public ReportEventRequest setMediaPlay(ReportMediaPlayEventRequest mediaPlay) {
        this.mediaPlay = mediaPlay;
        return this;
    }
    public ReportMediaPlayEventRequest getMediaPlay() {
        return this.mediaPlay;
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
