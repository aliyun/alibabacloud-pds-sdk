// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class LiveTranscodingSubtitleTaskResponse extends TeaModel {
    /**
     * <p>language, 字幕语言</p>
     */
    @NameInMap("language")
    public String language;

    /**
     * <p>status</p>
     */
    @NameInMap("status")
    public String status;

    /**
     * <p>url, finished 的时候才存在</p>
     */
    @NameInMap("url")
    public String url;

    public static LiveTranscodingSubtitleTaskResponse build(java.util.Map<String, ?> map) throws Exception {
        LiveTranscodingSubtitleTaskResponse self = new LiveTranscodingSubtitleTaskResponse();
        return TeaModel.build(map, self);
    }

    public LiveTranscodingSubtitleTaskResponse setLanguage(String language) {
        this.language = language;
        return this;
    }
    public String getLanguage() {
        return this.language;
    }

    public LiveTranscodingSubtitleTaskResponse setStatus(String status) {
        this.status = status;
        return this;
    }
    public String getStatus() {
        return this.status;
    }

    public LiveTranscodingSubtitleTaskResponse setUrl(String url) {
        this.url = url;
        return this;
    }
    public String getUrl() {
        return this.url;
    }

}
