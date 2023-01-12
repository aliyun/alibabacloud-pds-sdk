// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class VideoMediaVideoStream extends TeaModel {
    /**
     * <p>bitrate 视频比特率 单位：bps</p>
     */
    @NameInMap("bitrate")
    public String bitrate;

    /**
     * <p>clarity 清晰度（扫描）</p>
     */
    @NameInMap("clarity")
    public String clarity;

    /**
     * <p>code_name 视频编码模式</p>
     */
    @NameInMap("code_name")
    public String codeName;

    /**
     * <p>duration 单位 秒</p>
     */
    @NameInMap("duration")
    public String duration;

    /**
     * <p>fps 视频平均帧率</p>
     */
    @NameInMap("fps")
    public String fps;

    /**
     * <p>rotate 视频横屏 竖屏</p>
     */
    @NameInMap("rotate")
    public String rotate;

    public static VideoMediaVideoStream build(java.util.Map<String, ?> map) throws Exception {
        VideoMediaVideoStream self = new VideoMediaVideoStream();
        return TeaModel.build(map, self);
    }

    public VideoMediaVideoStream setBitrate(String bitrate) {
        this.bitrate = bitrate;
        return this;
    }
    public String getBitrate() {
        return this.bitrate;
    }

    public VideoMediaVideoStream setClarity(String clarity) {
        this.clarity = clarity;
        return this;
    }
    public String getClarity() {
        return this.clarity;
    }

    public VideoMediaVideoStream setCodeName(String codeName) {
        this.codeName = codeName;
        return this;
    }
    public String getCodeName() {
        return this.codeName;
    }

    public VideoMediaVideoStream setDuration(String duration) {
        this.duration = duration;
        return this;
    }
    public String getDuration() {
        return this.duration;
    }

    public VideoMediaVideoStream setFps(String fps) {
        this.fps = fps;
        return this;
    }
    public String getFps() {
        return this.fps;
    }

    public VideoMediaVideoStream setRotate(String rotate) {
        this.rotate = rotate;
        return this;
    }
    public String getRotate() {
        return this.rotate;
    }

}
