// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * report_media_play_event request
 */
public class ReportMediaPlayEventRequest extends TeaModel {
    /**
     * <p>duration</p>
     */
    @NameInMap("duration")
    public Long duration;

    /**
     * <p>error</p>
     */
    @NameInMap("error")
    public String error;

    /**
     * <p>file_id</p>
     */
    @NameInMap("file_id")
    public String fileId;

    /**
     * <p>player_version</p>
     */
    @NameInMap("player_version")
    public String playerVersion;

    /**
     * <p>sub_type</p>
     */
    @NameInMap("sub_type")
    public String subType;

    /**
     * <p>template_id</p>
     */
    @NameInMap("template_id")
    public String templateId;

    /**
     * <p>wait_count</p>
     */
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
