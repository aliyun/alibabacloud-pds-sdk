// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class VideoPreviewAudioConfig extends TeaModel {
    @NameInMap("support_ext")
    public java.util.List<String> supportExt;

    @NameInMap("template")
    public java.util.List<VideoPreviewAudioTemplate> template;

    public static VideoPreviewAudioConfig build(java.util.Map<String, ?> map) throws Exception {
        VideoPreviewAudioConfig self = new VideoPreviewAudioConfig();
        return TeaModel.build(map, self);
    }

    public VideoPreviewAudioConfig setSupportExt(java.util.List<String> supportExt) {
        this.supportExt = supportExt;
        return this;
    }
    public java.util.List<String> getSupportExt() {
        return this.supportExt;
    }

    public VideoPreviewAudioConfig setTemplate(java.util.List<VideoPreviewAudioTemplate> template) {
        this.template = template;
        return this;
    }
    public java.util.List<VideoPreviewAudioTemplate> getTemplate() {
        return this.template;
    }

}
