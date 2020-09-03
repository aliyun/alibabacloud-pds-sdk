// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.hosting.mode.models;

import com.aliyun.tea.*;

/**
 * 获取视频雪碧图地址 url response
 */
public class GetVideoPreviewSpriteURLResponse extends TeaModel {
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

    // sprite_url_list
    @NameInMap("sprite_url_list")
    public java.util.List<String> spriteUrlList;

    public static GetVideoPreviewSpriteURLResponse build(java.util.Map<String, ?> map) throws Exception {
        GetVideoPreviewSpriteURLResponse self = new GetVideoPreviewSpriteURLResponse();
        return TeaModel.build(map, self);
    }

    public GetVideoPreviewSpriteURLResponse setCol(Long col) {
        this.col = col;
        return this;
    }
    public Long getCol() {
        return this.col;
    }

    public GetVideoPreviewSpriteURLResponse setCount(Long count) {
        this.count = count;
        return this;
    }
    public Long getCount() {
        return this.count;
    }

    public GetVideoPreviewSpriteURLResponse setFrameCount(Long frameCount) {
        this.frameCount = frameCount;
        return this;
    }
    public Long getFrameCount() {
        return this.frameCount;
    }

    public GetVideoPreviewSpriteURLResponse setFrameHeight(Long frameHeight) {
        this.frameHeight = frameHeight;
        return this;
    }
    public Long getFrameHeight() {
        return this.frameHeight;
    }

    public GetVideoPreviewSpriteURLResponse setFrameWidth(Long frameWidth) {
        this.frameWidth = frameWidth;
        return this;
    }
    public Long getFrameWidth() {
        return this.frameWidth;
    }

    public GetVideoPreviewSpriteURLResponse setRow(Long row) {
        this.row = row;
        return this;
    }
    public Long getRow() {
        return this.row;
    }

    public GetVideoPreviewSpriteURLResponse setSpriteUrlList(java.util.List<String> spriteUrlList) {
        this.spriteUrlList = spriteUrlList;
        return this;
    }
    public java.util.List<String> getSpriteUrlList() {
        return this.spriteUrlList;
    }

}
