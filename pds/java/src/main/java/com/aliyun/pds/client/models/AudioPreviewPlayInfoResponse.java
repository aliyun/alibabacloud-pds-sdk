// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 音频转码信息响应
 */
public class AudioPreviewPlayInfoResponse extends TeaModel {
    @NameInMap("meta")
    public AudioPreviewPlayInfoMetaResponse meta;

    // 离线转码有效
    @NameInMap("offline_audio_list")
    public java.util.List<VideoPreviewOfflineAudioTranscodingTaskResponse> offlineAudioList;

    public static AudioPreviewPlayInfoResponse build(java.util.Map<String, ?> map) throws Exception {
        AudioPreviewPlayInfoResponse self = new AudioPreviewPlayInfoResponse();
        return TeaModel.build(map, self);
    }

    public AudioPreviewPlayInfoResponse setMeta(AudioPreviewPlayInfoMetaResponse meta) {
        this.meta = meta;
        return this;
    }
    public AudioPreviewPlayInfoMetaResponse getMeta() {
        return this.meta;
    }

    public AudioPreviewPlayInfoResponse setOfflineAudioList(java.util.List<VideoPreviewOfflineAudioTranscodingTaskResponse> offlineAudioList) {
        this.offlineAudioList = offlineAudioList;
        return this;
    }
    public java.util.List<VideoPreviewOfflineAudioTranscodingTaskResponse> getOfflineAudioList() {
        return this.offlineAudioList;
    }

}
