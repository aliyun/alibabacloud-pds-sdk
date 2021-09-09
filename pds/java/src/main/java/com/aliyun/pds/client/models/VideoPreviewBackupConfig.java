// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 转码备份配置（当前仅运维会用到）
 */
public class VideoPreviewBackupConfig extends TeaModel {
    @NameInMap("count_once")
    public Long countOnce;

    @NameInMap("store")
    public Store store;

    @NameInMap("store_id_map")
    public java.util.Map<String, ?> storeIdMap;

    public static VideoPreviewBackupConfig build(java.util.Map<String, ?> map) throws Exception {
        VideoPreviewBackupConfig self = new VideoPreviewBackupConfig();
        return TeaModel.build(map, self);
    }

    public VideoPreviewBackupConfig setCountOnce(Long countOnce) {
        this.countOnce = countOnce;
        return this;
    }
    public Long getCountOnce() {
        return this.countOnce;
    }

    public VideoPreviewBackupConfig setStore(Store store) {
        this.store = store;
        return this;
    }
    public Store getStore() {
        return this.store;
    }

    public VideoPreviewBackupConfig setStoreIdMap(java.util.Map<String, ?> storeIdMap) {
        this.storeIdMap = storeIdMap;
        return this;
    }
    public java.util.Map<String, ?> getStoreIdMap() {
        return this.storeIdMap;
    }

}
