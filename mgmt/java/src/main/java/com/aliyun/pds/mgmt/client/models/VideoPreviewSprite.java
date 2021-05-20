// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class VideoPreviewSprite extends TeaModel {
    @NameInMap("auto_scale")
    public VideoPreviewAutoScale autoScale;

    // col
    @NameInMap("col")
    public Long col;

    // frame_height
    @NameInMap("frame_height")
    public Long frameHeight;

    // frame_width
    @NameInMap("frame_width")
    public Long frameWidth;

    @NameInMap("interval")
    public VideoPreviewSpriteInterval interval;

    // row
    @NameInMap("row")
    public Long row;

    public static VideoPreviewSprite build(java.util.Map<String, ?> map) throws Exception {
        VideoPreviewSprite self = new VideoPreviewSprite();
        return TeaModel.build(map, self);
    }

    public VideoPreviewSprite setAutoScale(VideoPreviewAutoScale autoScale) {
        this.autoScale = autoScale;
        return this;
    }
    public VideoPreviewAutoScale getAutoScale() {
        return this.autoScale;
    }

    public VideoPreviewSprite setCol(Long col) {
        this.col = col;
        return this;
    }
    public Long getCol() {
        return this.col;
    }

    public VideoPreviewSprite setFrameHeight(Long frameHeight) {
        this.frameHeight = frameHeight;
        return this;
    }
    public Long getFrameHeight() {
        return this.frameHeight;
    }

    public VideoPreviewSprite setFrameWidth(Long frameWidth) {
        this.frameWidth = frameWidth;
        return this;
    }
    public Long getFrameWidth() {
        return this.frameWidth;
    }

    public VideoPreviewSprite setInterval(VideoPreviewSpriteInterval interval) {
        this.interval = interval;
        return this;
    }
    public VideoPreviewSpriteInterval getInterval() {
        return this.interval;
    }

    public VideoPreviewSprite setRow(Long row) {
        this.row = row;
        return this;
    }
    public Long getRow() {
        return this.row;
    }

}
