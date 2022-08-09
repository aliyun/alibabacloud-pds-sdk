// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 *
 */
public class DriveLogSettingDetail extends TeaModel {
    // name
    @NameInMap("name")
    public String name;

    // owner_id
    @NameInMap("owner_id")
    public String ownerId;

    // owner_name
    @NameInMap("owner_name")
    public String ownerName;

    // owner_type
    @NameInMap("owner_type")
    public String ownerType;

    // total_size
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
