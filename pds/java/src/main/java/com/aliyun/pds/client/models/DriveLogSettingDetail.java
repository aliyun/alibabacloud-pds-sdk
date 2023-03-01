// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class DriveLogSettingDetail extends TeaModel {
    /**
     * <p>name</p>
     */
    @NameInMap("name")
    public String name;

    /**
     * <p>owner_id</p>
     */
    @NameInMap("owner_id")
    public String ownerId;

    /**
     * <p>owner_name</p>
     */
    @NameInMap("owner_name")
    public String ownerName;

    /**
     * <p>owner_type</p>
     */
    @NameInMap("owner_type")
    public String ownerType;

    /**
     * <p>total_size</p>
     */
    @NameInMap("total_size")
    public Long totalSize;

    public static DriveLogSettingDetail build(java.util.Map<String, ?> map) throws Exception {
        DriveLogSettingDetail self = new DriveLogSettingDetail();
        return TeaModel.build(map, self);
    }

    public DriveLogSettingDetail setName(String name) {
        this.name = name;
        return this;
    }
    public String getName() {
        return this.name;
    }

    public DriveLogSettingDetail setOwnerId(String ownerId) {
        this.ownerId = ownerId;
        return this;
    }
    public String getOwnerId() {
        return this.ownerId;
    }

    public DriveLogSettingDetail setOwnerName(String ownerName) {
        this.ownerName = ownerName;
        return this;
    }
    public String getOwnerName() {
        return this.ownerName;
    }

    public DriveLogSettingDetail setOwnerType(String ownerType) {
        this.ownerType = ownerType;
        return this;
    }
    public String getOwnerType() {
        return this.ownerType;
    }

    public DriveLogSettingDetail setTotalSize(Long totalSize) {
        this.totalSize = totalSize;
        return this;
    }
    public Long getTotalSize() {
        return this.totalSize;
    }

}
