// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.standard.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class VideoPreviewSprite extends TeaModel {
    // col
    @NameInMap("col")
    public Long col;

    // count
    @NameInMap("count")
    public Long count;

    // frame_count
    @NameInMap("frame_count")
    public Long frameCount;

    // frame_height
    @NameInMap("frame_height")
    public Long frameHeight;

    // frame_width
    @NameInMap("frame_width")
    public Long frameWidth;

    // row
    @NameInMap("row")
    public Long row;

    // status
    @NameInMap("status")
    public String status;

    public static VideoPreviewSprite build(java.util.Map<String, ?> map) throws Exception {
        VideoPreviewSprite self = new VideoPreviewSprite();
        return TeaModel.build(map, self);
    }

    public VideoPreviewSprite setCol(Long col) {
        this.col = col;
        return this;
    }
    public Long getCol() {
        return this.col;
    }

    public VideoPreviewSprite setCount(Long count) {
        this.count = count;
        return this;
    }
    public Long getCount() {
        return this.count;
    }

    public VideoPreviewSprite setFrameCount(Long frameCount) {
        this.frameCount = frameCount;
        return this;
    }
    public Long getFrameCount() {
        return this.frameCount;
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

    public VideoPreviewSprite setRow(Long row) {
        this.row = row;
        return this;
    }
    public Long getRow() {
        return this.row;
    }

    public VideoPreviewSprite setStatus(String status) {
        this.status = status;
        return this;
    }
    public String getStatus() {
        return this.status;
    }

}
