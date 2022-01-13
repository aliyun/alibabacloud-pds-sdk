// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 清理所有回收站文件元数据请求
 */
public class ClearAllRecycleBinRequest extends TeaModel {
    // addition_data
    @NameInMap("addition_data")
    public java.util.Map<String, ?> additionData;

    @NameInMap("file_path_type")
    public String filePathType;

    public static ClearAllRecycleBinRequest build(java.util.Map<String, ?> map) throws Exception {
        ClearAllRecycleBinRequest self = new ClearAllRecycleBinRequest();
        return TeaModel.build(map, self);
    }

    public ClearAllRecycleBinRequest setAdditionData(java.util.Map<String, ?> additionData) {
        this.additionData = additionData;
        return this;
    }
    public java.util.Map<String, ?> getAdditionData() {
        return this.additionData;
    }

    public ClearAllRecycleBinRequest setFilePathType(String filePathType) {
        this.filePathType = filePathType;
        return this;
    }
    public String getFilePathType() {
        return this.filePathType;
    }

}
