// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class ShareLinkCountResponse extends TeaModel {
    /**
     * <p>access_count</p>
     */
    @NameInMap("access_count")
    public Long accessCount;

    /**
     * <p>下载次数</p>
     */
    @NameInMap("download_count")
    public Long downloadCount;

    /**
     * <p>preview_count</p>
     */
    @NameInMap("preview_count")
    public Long previewCount;

    /**
     * <p>举报次数</p>
     */
    @NameInMap("report_count")
    public Long reportCount;

    /**
     * <p>转存次数</p>
     */
    @NameInMap("save_count")
    public Long saveCount;

    /**
     * <p>音视频播放次数</p>
     */
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
