// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 启动视频转码请求
 */
public class HostingVideoTranscodeRequest extends TeaModel {
    /**
     * <p>drive_id</p>
     */
    @NameInMap("drive_id")
    @Validation(pattern = "[0-9]+")
    public String driveId;

    /**
     * <p>file_path</p>
     */
    @NameInMap("file_path")
    @Validation(required = true, maxLength = 1000, minLength = 1)
    public String filePath;

    /**
     * <p>hls_time</p>
     */
    @NameInMap("hls_time")
    public Long hlsTime;

    /**
     * <p>protection_scheme</p>
     */
    @NameInMap("protection_scheme")
    public String protectionScheme;

    /**
     * <p>remarks</p>
     */
    @NameInMap("remarks")
    public String remarks;

    /**
     * <p>share_id</p>
     */
    @NameInMap("share_id")
    @Validation(pattern = "[0-9a-zA-Z-]+")
    public String shareId;

    /**
     * <p>transcode</p>
     */
    @NameInMap("transcode")
    public Boolean transcode;

    public static HostingVideoTranscodeRequest build(java.util.Map<String, ?> map) throws Exception {
        HostingVideoTranscodeRequest self = new HostingVideoTranscodeRequest();
        return TeaModel.build(map, self);
    }

    public HostingVideoTranscodeRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public HostingVideoTranscodeRequest setFilePath(String filePath) {
        this.filePath = filePath;
        return this;
    }
    public String getFilePath() {
        return this.filePath;
    }

    public HostingVideoTranscodeRequest setHlsTime(Long hlsTime) {
        this.hlsTime = hlsTime;
        return this;
    }
    public Long getHlsTime() {
        return this.hlsTime;
    }

    public HostingVideoTranscodeRequest setProtectionScheme(String protectionScheme) {
        this.protectionScheme = protectionScheme;
        return this;
    }
    public String getProtectionScheme() {
        return this.protectionScheme;
    }

    public HostingVideoTranscodeRequest setRemarks(String remarks) {
        this.remarks = remarks;
        return this;
    }
    public String getRemarks() {
        return this.remarks;
    }

    public HostingVideoTranscodeRequest setShareId(String shareId) {
        this.shareId = shareId;
        return this;
    }
    public String getShareId() {
        return this.shareId;
    }

    public HostingVideoTranscodeRequest setTranscode(Boolean transcode) {
        this.transcode = transcode;
        return this;
    }
    public Boolean getTranscode() {
        return this.transcode;
    }

}
