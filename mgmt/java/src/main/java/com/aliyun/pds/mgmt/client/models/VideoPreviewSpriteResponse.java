// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class VideoPreviewSpriteResponse extends TeaModel {
    /**
     * <p>col</p>
     */
    @NameInMap("col")
    public Long col;

    /**
     * <p>count</p>
     */
    @NameInMap("count")
    public Long count;

    /**
     * <p>frame_count</p>
     */
    @NameInMap("frame_count")
    public Long frameCount;

    /**
     * <p>frame_height</p>
     */
    @NameInMap("frame_height")
    public Long frameHeight;

    /**
     * <p>frame_width</p>
     */
    @NameInMap("frame_width")
    public Long frameWidth;

    /**
     * <p>row</p>
     */
    @NameInMap("row")
    public Long row;

    /**
     * <p>status</p>
     */
    @NameInMap("status")
    public String status;

    public static VideoPreviewSpriteResponse build(java.util.Map<String, ?> map) throws Exception {
        VideoPreviewSpriteResponse self = new VideoPreviewSpriteResponse();
        return TeaModel.build(map, self);
    }

    public VideoPreviewSpriteResponse setCol(Long col) {
        this.col = col;
        return this;
    }
    public Long getCol() {
        return this.col;
    }

    public VideoPreviewSpriteResponse setCount(Long count) {
        this.count = count;
        return this;
    }
    public Long getCount() {
        return this.count;
    }

    public VideoPreviewSpriteResponse setFrameCount(Long frameCount) {
        this.frameCount = frameCount;
        return this;
    }
    public Long getFrameCount() {
        return this.frameCount;
    }

    public VideoPreviewSpriteResponse setFrameHeight(Long frameHeight) {
        this.frameHeight = frameHeight;
        return this;
    }
    public Long getFrameHeight() {
        return this.frameHeight;
    }

    public VideoPreviewSpriteResponse setFrameWidth(Long frameWidth) {
        this.frameWidth = frameWidth;
        return this;
    }
    public Long getFrameWidth() {
        return this.frameWidth;
    }

    public VideoPreviewSpriteResponse setRow(Long row) {
        this.row = row;
        return this;
    }
    public Long getRow() {
        return this.row;
    }

    public VideoPreviewSpriteResponse setStatus(String status) {
        this.status = status;
        return this;
    }
    public String getStatus() {
        return this.status;
    }

}
