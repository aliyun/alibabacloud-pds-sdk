// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 清空回收站
 */
public class ClearRecycleBinRequest extends TeaModel {
    /**
     * <p>addition_data</p>
     */
    @NameInMap("addition_data")
    public java.util.Map<String, ?> additionData;

    /**
     * <p>drive_id</p>
     */
    @NameInMap("drive_id")
    @Validation(pattern = "[0-9]+")
    public String driveId;

    @NameInMap("task_category")
    public String taskCategory;

    public static ClearRecycleBinRequest build(java.util.Map<String, ?> map) throws Exception {
        ClearRecycleBinRequest self = new ClearRecycleBinRequest();
        return TeaModel.build(map, self);
    }

    public ClearRecycleBinRequest setAdditionData(java.util.Map<String, ?> additionData) {
        this.additionData = additionData;
        return this;
    }
    public java.util.Map<String, ?> getAdditionData() {
        return this.additionData;
    }

    public ClearRecycleBinRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public ClearRecycleBinRequest setTaskCategory(String taskCategory) {
        this.taskCategory = taskCategory;
        return this;
    }
    public String getTaskCategory() {
        return this.taskCategory;
    }

}
