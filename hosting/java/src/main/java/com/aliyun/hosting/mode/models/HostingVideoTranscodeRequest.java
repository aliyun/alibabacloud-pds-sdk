// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.hosting.mode.models;

import com.aliyun.tea.*;

/**
 * 启动视频转码请求
 */
public class HostingVideoTranscodeRequest extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    // drive_id
    @NameInMap("drive_id")
    @Validation(pattern = "[0-9]+")
    public String driveId;

    // file_path
    @NameInMap("file_path")
    @Validation(required = true, maxLength = 1000, minLength = 1)
    public String filePath;

    // hls_time
    @NameInMap("hls_time")
    public Long hlsTime;

    // protection_scheme
    @NameInMap("protection_scheme")
    public String protectionScheme;

    // remarks
    @NameInMap("remarks")
    public String remarks;

    // share_id
    @NameInMap("share_id")
    @Validation(pattern = "[0-9a-zA-Z-]+")
    public String shareId;

    // transcode
    @NameInMap("transcode")
    public Boolean transcode;

    public static HostingVideoTranscodeRequest build(java.util.Map<String, ?> map) throws Exception {
        HostingVideoTranscodeRequest self = new HostingVideoTranscodeRequest();
        return TeaModel.build(map, self);
    }

    public HostingVideoTranscodeRequest setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
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
