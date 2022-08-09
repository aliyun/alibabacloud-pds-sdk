// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * report_media_play_event request
 */
public class ReportMediaPlayEventRequest extends TeaModel {
    // duration
    @NameInMap("duration")
    public Long duration;

    // error
    @NameInMap("error")
    public String error;

    // file_id
    @NameInMap("file_id")
    public String fileId;

    // player_version
    @NameInMap("player_version")
    public String playerVersion;

    // sub_type
    @NameInMap("sub_type")
    public String subType;

    // template_id
    @NameInMap("template_id")
    public String templateId;

    // wait_count
    @NameInMap("wait_count")
    public Long waitCount;

    public static ReportMediaPlayEventRequest build(java.util.Map<String, ?> map) throws Exception {
        ReportMediaPlayEventRequest self = new ReportMediaPlayEventRequest();
        return TeaModel.build(map, self);
    }

    public ReportMediaPlayEventRequest setDuration(Long duration) {
        this.duration = duration;
        return this;
    }
    public Long getDuration() {
        return this.duration;
    }

    public ReportMediaPlayEventRequest setError(String error) {
        this.error = error;
        return this;
    }
    public String getError() {
        return this.error;
    }

    public ReportMediaPlayEventRequest setFileId(String fileId) {
        this.fileId = fileId;
        return this;
    }
    public String getFileId() {
        return this.fileId;
    }

    public ReportMediaPlayEventRequest setPlayerVersion(String playerVersion) {
        this.playerVersion = playerVersion;
        return this;
    }
    public String getPlayerVersion() {
        return this.playerVersion;
    }

    public ReportMediaPlayEventRequest setSubType(String subType) {
        this.subType = subType;
        return this;
    }
    public String getSubType() {
        return this.subType;
    }

    public ReportMediaPlayEventRequest setTemplateId(String templateId) {
        this.templateId = templateId;
        return this;
    }
    public String getTemplateId() {
        return this.templateId;
    }

    public ReportMediaPlayEventRequest setWaitCount(Long waitCount) {
        this.waitCount = waitCount;
        return this;
    }
    public Long getWaitCount() {
        return this.waitCount;
    }

}
