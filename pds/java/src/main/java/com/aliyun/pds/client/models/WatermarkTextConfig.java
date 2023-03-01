// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * WatermarkTextConfig 文字水印配置
 */
public class WatermarkTextConfig extends TeaModel {
    @NameInMap("bold")
    public Boolean bold;

    @NameInMap("fill_style")
    public String fillStyle;

    @NameInMap("font")
    public String font;

    @NameInMap("horizontal")
    public Long horizontal;

    @NameInMap("rotate")
    public Long rotate;

    @NameInMap("size")
    public Long size;

    @NameInMap("vertical")
    public Long vertical;

    public static WatermarkTextConfig build(java.util.Map<String, ?> map) throws Exception {
        WatermarkTextConfig self = new WatermarkTextConfig();
        return TeaModel.build(map, self);
    }

    public WatermarkTextConfig setBold(Boolean bold) {
        this.bold = bold;
        return this;
    }
    public Boolean getBold() {
        return this.bold;
    }

    public WatermarkTextConfig setFillStyle(String fillStyle) {
        this.fillStyle = fillStyle;
        return this;
    }
    public String getFillStyle() {
        return this.fillStyle;
    }

    public WatermarkTextConfig setFont(String font) {
        this.font = font;
        return this;
    }
    public String getFont() {
        return this.font;
    }

    public WatermarkTextConfig setHorizontal(Long horizontal) {
        this.horizontal = horizontal;
        return this;
    }
    public Long getHorizontal() {
        return this.horizontal;
    }

    public WatermarkTextConfig setRotate(Long rotate) {
        this.rotate = rotate;
        return this;
    }
    public Long getRotate() {
        return this.rotate;
    }

    public WatermarkTextConfig setSize(Long size) {
        this.size = size;
        return this;
    }
    public Long getSize() {
        return this.size;
    }

    public WatermarkTextConfig setVertical(Long vertical) {
        this.vertical = vertical;
        return this;
    }
    public Long getVertical() {
        return this.vertical;
    }

}
