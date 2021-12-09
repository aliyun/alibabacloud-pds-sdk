// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 前端判断是否可以播放视频流程
if OnlineVideoTranscodeEnable then do video_preview play  // 如果是离线转码, 那么用OfflineVideoTranscodeEnable代替, 音频类似
else if appConfig.VideoPlayEnable then do source file play // 音频用AudioPlayEnable代替
else notify user the function not support
 */
public class VideoPreviewAppConfig extends TeaModel {
    @NameInMap("offline_audio_transcode_enable")
    public Boolean offlineAudioTranscodeEnable;

    @NameInMap("offline_video_transcode_enable")
    public Boolean offlineVideoTranscodeEnable;

    @NameInMap("online_audio_transcode_enable")
    public Boolean onlineAudioTranscodeEnable;

    @NameInMap("online_video_transcode_enable")
    public Boolean onlineVideoTranscodeEnable;

    public static VideoPreviewAppConfig build(java.util.Map<String, ?> map) throws Exception {
        VideoPreviewAppConfig self = new VideoPreviewAppConfig();
        return TeaModel.build(map, self);
    }

    public VideoPreviewAppConfig setOfflineAudioTranscodeEnable(Boolean offlineAudioTranscodeEnable) {
        this.offlineAudioTranscodeEnable = offlineAudioTranscodeEnable;
        return this;
    }
    public Boolean getOfflineAudioTranscodeEnable() {
        return this.offlineAudioTranscodeEnable;
    }

    public VideoPreviewAppConfig setOfflineVideoTranscodeEnable(Boolean offlineVideoTranscodeEnable) {
        this.offlineVideoTranscodeEnable = offlineVideoTranscodeEnable;
        return this;
    }
    public Boolean getOfflineVideoTranscodeEnable() {
        return this.offlineVideoTranscodeEnable;
    }

    public VideoPreviewAppConfig setOnlineAudioTranscodeEnable(Boolean onlineAudioTranscodeEnable) {
        this.onlineAudioTranscodeEnable = onlineAudioTranscodeEnable;
        return this;
    }
    public Boolean getOnlineAudioTranscodeEnable() {
        return this.onlineAudioTranscodeEnable;
    }

    public VideoPreviewAppConfig setOnlineVideoTranscodeEnable(Boolean onlineVideoTranscodeEnable) {
        this.onlineVideoTranscodeEnable = onlineVideoTranscodeEnable;
        return this;
    }
    public Boolean getOnlineVideoTranscodeEnable() {
        return this.onlineVideoTranscodeEnable;
    }

}
