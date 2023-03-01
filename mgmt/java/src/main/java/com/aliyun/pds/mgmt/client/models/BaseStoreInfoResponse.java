// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class BaseStoreInfoResponse extends TeaModel {
    /**
     * <p>bucket名称</p>
     */
    @NameInMap("bucket")
    public String bucket;

    /**
     * <p>自定义Public访问地址</p>
     */
    @NameInMap("customized_endpoint")
    public String customizedEndpoint;

    /**
     * <p>Public访问地址</p>
     */
    @NameInMap("endpoint")
    public String endpoint;

    /**
     * <p>存储归属，system表示系统提供，custom表示使用自己的存储</p>
     */
    @NameInMap("ownership")
    public String ownership;

    /**
     * <p>store ID</p>
     */
    @NameInMap("store_id")
    public String storeId;

    /**
     * <p>是否开启传输加速</p>
     */
    @NameInMap("transfer_acc_enabled")
    public Boolean transferAccEnabled;

    /**
     * <p>存储类型，当前只支持oss</p>
     */
    @NameInMap("type")
    public String type;

    public static BaseStoreInfoResponse build(java.util.Map<String, ?> map) throws Exception {
        BaseStoreInfoResponse self = new BaseStoreInfoResponse();
        return TeaModel.build(map, self);
    }

    public BaseStoreInfoResponse setBucket(String bucket) {
        this.bucket = bucket;
        return this;
    }
    public String getBucket() {
        return this.bucket;
    }

    public BaseStoreInfoResponse setCustomizedEndpoint(String customizedEndpoint) {
        this.customizedEndpoint = customizedEndpoint;
        return this;
    }
    public String getCustomizedEndpoint() {
        return this.customizedEndpoint;
    }

    public BaseStoreInfoResponse setEndpoint(String endpoint) {
        this.endpoint = endpoint;
        return this;
    }
    public String getEndpoint() {
        return this.endpoint;
    }

    public BaseStoreInfoResponse setOwnership(String ownership) {
        this.ownership = ownership;
        return this;
    }
    public String getOwnership() {
        return this.ownership;
    }

    public BaseStoreInfoResponse setStoreId(String storeId) {
        this.storeId = storeId;
        return this;
    }
    public String getStoreId() {
        return this.storeId;
    }

    public BaseStoreInfoResponse setTransferAccEnabled(Boolean transferAccEnabled) {
        this.transferAccEnabled = transferAccEnabled;
        return this;
    }
    public Boolean getTransferAccEnabled() {
        return this.transferAccEnabled;
    }

    public BaseStoreInfoResponse setType(String type) {
        this.type = type;
        return this;
    }
    public String getType() {
        return this.type;
    }

}
