// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class VideoPreviewAutoCategoryConfig extends TeaModel {
    @NameInMap("default_audio_category")
    public String defaultAudioCategory;

    @NameInMap("default_video_category")
    public String defaultVideoCategory;

    public static VideoPreviewAutoCategoryConfig build(java.util.Map<String, ?> map) throws Exception {
        VideoPreviewAutoCategoryConfig self = new VideoPreviewAutoCategoryConfig();
        return TeaModel.build(map, self);
    }

    public VideoPreviewAutoCategoryConfig setDefaultAudioCategory(String defaultAudioCategory) {
        this.defaultAudioCategory = defaultAudioCategory;
        return this;
    }
    public String getDefaultAudioCategory() {
        return this.defaultAudioCategory;
    }

    public VideoPreviewAutoCategoryConfig setDefaultVideoCategory(String defaultVideoCategory) {
        this.defaultVideoCategory = defaultVideoCategory;
        return this;
    }
    public String getDefaultVideoCategory() {
        return this.defaultVideoCategory;
    }

}
