// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.hostingmode.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class StoreFile extends TeaModel {
    @NameInMap("domain_id")
    public String domainId;

    @NameInMap("name")
    public String name;

    @NameInMap("parent_file_path")
    public String parentFilePath;

    @NameInMap("store_id")
    public String storeId;

    @NameInMap("type")
    public String type;

    public static StoreFile build(java.util.Map<String, ?> map) throws Exception {
        StoreFile self = new StoreFile();
        return TeaModel.build(map, self);
    }

    public StoreFile setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

    public StoreFile setName(String name) {
        this.name = name;
        return this;
    }
    public String getName() {
        return this.name;
    }

    public StoreFile setParentFilePath(String parentFilePath) {
        this.parentFilePath = parentFilePath;
        return this;
    }
    public String getParentFilePath() {
        return this.parentFilePath;
    }

    public StoreFile setStoreId(String storeId) {
        this.storeId = storeId;
        return this;
    }
    public String getStoreId() {
        return this.storeId;
    }

    public StoreFile setType(String type) {
        this.type = type;
        return this;
    }
    public String getType() {
        return this.type;
    }

}
