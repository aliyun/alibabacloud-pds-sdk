// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 视频雪碧图配置
 */
public class VideoPreviewSpriteConfig extends TeaModel {
    @NameInMap("auto_scale")
    public VideoPreviewAutoScaleConfig autoScale;

    @NameInMap("col")
    public Long col;

    @NameInMap("frame_height")
    public Long frameHeight;

    @NameInMap("frame_width")
    public Long frameWidth;

    @NameInMap("interval")
    public VideoPreviewSpriteIntervalConfig interval;

    @NameInMap("row")
    public Long row;

    public static VideoPreviewSpriteConfig build(java.util.Map<String, ?> map) throws Exception {
        VideoPreviewSpriteConfig self = new VideoPreviewSpriteConfig();
        return TeaModel.build(map, self);
    }

    public VideoPreviewSpriteConfig setAutoScale(VideoPreviewAutoScaleConfig autoScale) {
        this.autoScale = autoScale;
        return this;
    }
    public VideoPreviewAutoScaleConfig getAutoScale() {
        return this.autoScale;
    }

    public VideoPreviewSpriteConfig setCol(Long col) {
        this.col = col;
        return this;
    }
    public Long getCol() {
        return this.col;
    }

    public VideoPreviewSpriteConfig setFrameHeight(Long frameHeight) {
        this.frameHeight = frameHeight;
        return this;
    }
    public Long getFrameHeight() {
        return this.frameHeight;
    }

    public VideoPreviewSpriteConfig setFrameWidth(Long frameWidth) {
        this.frameWidth = frameWidth;
        return this;
    }
    public Long getFrameWidth() {
        return this.frameWidth;
    }

    public VideoPreviewSpriteConfig setInterval(VideoPreviewSpriteIntervalConfig interval) {
        this.interval = interval;
        return this;
    }
    public VideoPreviewSpriteIntervalConfig getInterval() {
        return this.interval;
    }

    public VideoPreviewSpriteConfig setRow(Long row) {
        this.row = row;
        return this;
    }
    public Long getRow() {
        return this.row;
    }

}
