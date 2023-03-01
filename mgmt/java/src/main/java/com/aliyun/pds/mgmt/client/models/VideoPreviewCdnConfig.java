// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class VideoPreviewCdnConfig extends TeaModel {
    @NameInMap("cache_store")
    public Store cacheStore;

    @NameInMap("enable_m3u8_cache")
    public Boolean enableM3u8Cache;

    @NameInMap("enabled")
    public Boolean enabled;

    @NameInMap("gray_config")
    public ApiConfig grayConfig;

    public static VideoPreviewCdnConfig build(java.util.Map<String, ?> map) throws Exception {
        VideoPreviewCdnConfig self = new VideoPreviewCdnConfig();
        return TeaModel.build(map, self);
    }

    public VideoPreviewCdnConfig setCacheStore(Store cacheStore) {
        this.cacheStore = cacheStore;
        return this;
    }
    public Store getCacheStore() {
        return this.cacheStore;
    }

    public VideoPreviewCdnConfig setEnableM3u8Cache(Boolean enableM3u8Cache) {
        this.enableM3u8Cache = enableM3u8Cache;
        return this;
    }
    public Boolean getEnableM3u8Cache() {
        return this.enableM3u8Cache;
    }

    public VideoPreviewCdnConfig setEnabled(Boolean enabled) {
        this.enabled = enabled;
        return this;
    }
    public Boolean getEnabled() {
        return this.enabled;
    }

    public VideoPreviewCdnConfig setGrayConfig(ApiConfig grayConfig) {
        this.grayConfig = grayConfig;
        return this;
    }
    public ApiConfig getGrayConfig() {
        return this.grayConfig;
    }

}
