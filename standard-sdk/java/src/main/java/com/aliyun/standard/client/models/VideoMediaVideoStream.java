// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.standard.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class VideoMediaVideoStream extends TeaModel {
    // bitrate 视频比特率 单位：bps
    @NameInMap("bitrate")
    public String bitrate;

    // clarity 清晰度（扫描）
    @NameInMap("clarity")
    public String clarity;

    // code_name 视频编码模式
    @NameInMap("code_name")
    public String codeName;

    // duration 单位 秒
    @NameInMap("duration")
    public String duration;

    // fps 视频平均帧率
    @NameInMap("fps")
    public String fps;

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

}
