// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class ShareLinkCountResponse extends TeaModel {
    // access_count
    @NameInMap("access_count")
    public Long accessCount;

    // 下载次数
    @NameInMap("download_count")
    public Long downloadCount;

    // preview_count
    @NameInMap("preview_count")
    public Long previewCount;

    // 举报次数
    @NameInMap("report_count")
    public Long reportCount;

    // 转存次数
    @NameInMap("save_count")
    public Long saveCount;

    // 音视频播放次数
    @NameInMap("video_preview_count")
    public Long videoPreviewCount;

    public static ShareLinkCountResponse build(java.util.Map<String, ?> map) throws Exception {
        ShareLinkCountResponse self = new ShareLinkCountResponse();
        return TeaModel.build(map, self);
    }

    public ShareLinkCountResponse setAccessCount(Long accessCount) {
        this.accessCount = accessCount;
        return this;
    }
    public Long getAccessCount() {
        return this.accessCount;
    }

    public ShareLinkCountResponse setDownloadCount(Long downloadCount) {
        this.downloadCount = downloadCount;
        return this;
    }
    public Long getDownloadCount() {
        return this.downloadCount;
    }

    public ShareLinkCountResponse setPreviewCount(Long previewCount) {
        this.previewCount = previewCount;
        return this;
    }
    public Long getPreviewCount() {
        return this.previewCount;
    }

    public ShareLinkCountResponse setReportCount(Long reportCount) {
        this.reportCount = reportCount;
        return this;
    }
    public Long getReportCount() {
        return this.reportCount;
    }

    public ShareLinkCountResponse setSaveCount(Long saveCount) {
        this.saveCount = saveCount;
        return this;
    }
    public Long getSaveCount() {
        return this.saveCount;
    }

    public ShareLinkCountResponse setVideoPreviewCount(Long videoPreviewCount) {
        this.videoPreviewCount = videoPreviewCount;
        return this;
    }
    public Long getVideoPreviewCount() {
        return this.videoPreviewCount;
    }

}
